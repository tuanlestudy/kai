#sudo pip install facebook-sdk 
#!/usr/bin/python
# -*-coding:Utf-8 -*
import json
import os
import pickle
import sys
import time
import urllib
import requests
from io import open as iopen
import sys
import facebook

ID = 'ID_PAGE'

TOKEN = '552786928418483|Q-mNVw-3-FiwEHB7lA4TR618VtA'  # access token - replace this with token value before running .

SAFE_CHARS = '-_() abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

def save(res, name='data'):
    """Save data to a file"""
    with open('%s.lst' % name, 'w') as f:
        pickle.dump(res, f)

def read(name='data'):
    """Read data from a file"""
    with open('%s.lst' % name, 'r') as f:
        res = pickle.load(f)
    return res

def fetch(limit=100000, depth=10, last=None, id=ID, token=TOKEN):
    """Fetch the data using Facebook's Graph API"""
    lst = []
    graph = facebook.GraphAPI(token)
    url = '%s/photos?type=uploaded' % id

    args = {'fields': ['images','name'], 'limit': limit}
    res = graph.request('%s/photos?type=uploaded' % id, args)
    # continue fetching till all photos are found
    while bool(res.get('paging',{}).get('next')):
        try:
            url = res['paging']['next']
            response=json.loads(urllib.urlopen(url).read())
            res['data'].extend(response.get('data'))
            res['paging']['next']=response.get('paging',{}).get('next',"")
            #process(lst, res['data'])
        except:
            break
    # setup toolbar
    lenData=len(res['data'])        
    print('Reading %s images..' % lenData)
    toolbar_width = 40
    step=lenData / toolbar_width
    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['
    for j,i in enumerate(res['data']):
        dataPhoto=graph.request(i.get('id'))
        i['source']=dataPhoto.get('images')[0].get('source') 
        i['name']=dataPhoto.get('name')
        if not bool(j % step):
            sys.stdout.write("-")
            sys.stdout.flush()
    sys.stdout.write("]\n")
    process(lst, res['data'])



    save(url, 'last_url')

    return lst

def process(res, dat):
    """Extract required data from a row"""
    err = []
    for d in dat:
        if not d.get('source'):
            err.append(d)
            continue
        src = d['source']
        if d.get('name'):
            name = ''.join(c for c in d['name'][:99] if c in SAFE_CHARS) + src[-4:]
        else:
            name = src[src.rfind('/')+1:]
        res.append({'name': name, 'src': src})
    if err:
        print '%d errors.' % len(err)
        print err
    print '%d photos found.' % len(dat)

def download(res):
    """Download the list of files"""
    start = time.clock()
    if not os.path.isdir(ID):
        os.mkdir(ID)
    os.chdir(ID)
    """ Using an counter to download 100 divisible photos & wait for some time  """
    delayCounter =1

    for i,p in enumerate(res):
        if delayCounter % 100 ==0 :
            #print "x - Downloaded %s picture " %delayCounter
            time.sleep(3)

        response = requests.get(p.get('src'))
        ext=response.headers.get('Content-Type').split('/')[-1]
        file_name='%s.%s' %(i,ext)
        if response.status_code == requests.codes.ok:
            with iopen(file_name, 'wb') as file:
                file.write(response.content)
        #print delayCounter
        delayCounter = delayCounter + 1

    print "Downloaded %s pictures in %.3f sec." % (len(res), time.clock()-start)

if __name__ == '__main__':
    # download 500 photos, fetch details about 100 at a time
    lst = fetch(limit=100000, depth=5000)
    save(lst, 'photos')
    #lst=read('photos')
    download(lst)
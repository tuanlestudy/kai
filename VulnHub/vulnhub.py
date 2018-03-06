import urllib2
import httplib
import urlparse
import short_url

def openlink(urllink):
    print('Reading pages')
    try:
        response = urllib2.urlopen(urllink)
        html = response.url.read()
        print(html)
    except IOError, e:
        print 'Failed to open "%s".' % urllink
        if hasattr(e, 'code'):
            print 'We failed with error code - %s.' % e.code
        elif hasattr(e, 'reason'):
            print "The error object has the following 'reason' attribute :"
            print e.reason
            print "This usually means the server doesn't exist,",
            print "is down, or we don't have an internet connection."
            return False
    print('Complete...')
    return html

def openfile(member, threads, count):
    string = member + " " +threads + "\n"
    check = False
    try:
        fileopen=open("data/data.txt","r")
    except ValueError:
        print("No such file")
    for line in fileopen:
        if (string == line):
            check = True
            break
        else: 
            check = False
    if(check == False):
        writefile(member, threads)
        count+=1
    fileopen.close()
    return count
    

def writefile(member, threads):
    try:
        f=open("data/data.txt","a")
    except ValueError:
        print("No such file")
    print (member + '     ' + threads)
    f.write(member + " " + threads+"\n")
    f.close()
            
def getcontent(html):
    #/entry/damn-vulnerable-arm-router-dvar-tinysploitarm,224/
    for x in range(0,len(html)-1):
        if ( html[x] == '/'):
            #find '/entry/'
            if(html[x:x+7]=='/entry/'):
                for y in range(x+8,len(html)-1):
                    if(html[n]=='/'):
                        linkentry = html[m:n]
                        print (linkentry)
                        break
                    #y+=1
        #x+=1

if __name__ == "__main__":
    #openfile("test","test")

    urllink="https://www.vulnhub.com/entry/damn-vulnerable-arm-router-dvar-tinysploitarm,224/"
    
    #https://www.vulnhub.com/?page=2

    html = openlink(urllink)




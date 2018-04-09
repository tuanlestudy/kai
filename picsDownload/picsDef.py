import cv2
import urllib
import urllib2
import numpy as np


def check_url(url_link):
    count = 0
    for c in range (0, len(url_link)-5):
        if (url_link[c:c+4] == 'http'):
            newlink = url_link[c:len(url_link)]
    return newlink


def read_url(url_link):
    response = urllib2.urlopen(url_link)
    html = response.read()
    beg = 0
    end = 0
    get = False
    listS = []
    check = False
    j = 0
    url_image = ""
    for i in range (0, len(html)-5):
        if(html[i:i+3] == 'jpg' or html[i:i+3] == 'png' or html[i:i+3] == 'raw' or html[i:i+3] == 'gif' or html[i:i+4] == 'jpeg'):
            end = i
            while True:
                if (html[end]=='"'):
                    break
                else:
                    end += 1
            j = i
            while True:
                j = j -1
                if(html[j] == '"'):
                    beg = j + 1
                    break    
            #print beg, end, end - beg
            url_imageS = html[beg:end]
            for c in range(0, end-beg):
                if (url_imageS[c:c+4] == 'http'):
                    url_image = url_imageS[c:end-beg-c]   
            if (url_image[0:4] == 'http'):
                for c in range(0, len(listS)):
                    if(listS[c] == url_image):
                        check = True
                if (check == False):
                    listS.append(url_image)
                check = False
    for d in range(0, len(listS)):
        print listS[d]
        try:
            get_image(listS[d])
        except:
            print 'error'

def get_image(url_image):  
    req = urllib.urlopen(url_image)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img = cv2.imdecode(arr, -1) # 'Load it as it is' 
    height, width, channels = img.shape
    #print height, width, channels
    if (height > 300):
        rate = height / 300
        heightS = 300
        widthS = width / rate
        imgS = cv2.resize(img, (widthS, heightS))
        cv2.imshow('image', imgS)
        cv2.waitKey(50)
    elif (width > 300):
        rate = width / 300
        widthS = 300
        heightS = height / rate
        imgS = cv2.resize(img, (widthS, heightS))
        cv2.imshow('image', imgS)
        cv2.waitKey(50)
    else:
        cv2.imshow('image', img)
        cv2.waitKey(50)
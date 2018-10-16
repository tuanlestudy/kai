import os
import urllib.request
import webbrowser
import os.path

def downloadPics():
    fr = open('tempLink.txt', 'a')

    os.system('mkdir pics/' + pages)

    with urllib.request.urlopen(url) as response:
        html = response.read()
    fw = open("temp", 'wb')
    fw.write(html)
    fw.close()
    fr = open("temp", encoding="utf8")
    count = 100
    for x in fr:
        for i in range (0, len(x)):
            if (x[i:i + 3] == 'jpg'):
                end = i + 3
                j = i
                while True:
                    j = j - 1
                    if (x[j:j+4] == 'http'):
                        beg = j
                        break
                url_imageS = x[beg:end]
                #print(url_imageS)
                print('wget ' + url_imageS + ' -P ./pics/luna/')
                print()
                os.system('wget ' + url_imageS + ' -O ./pics/' + pages + '/' + str(count) + '.jpg')
                count = count + 1
    fr.close()


def write2file(link):
    fw = open('link.txt', 'w')
    fw.write(link)
    fw.close()

def checkPages():
    pages = input('Start Number: ')
    a=0
    b=1
    for k in range(int(pages), int(pages) + 10):
        url = 'https://hdasianpics.com/album/' + str(k) + '/'
        with urllib.request.urlopen(url) as response:
            html = response.read()
        fw = open("temp", 'wb')
        fw.write(html)
        fw.close()
        fr = open("temp", encoding="utf8")
        for x in fr:
            for i in range(0, len(x)):
                if (x[i:i+7] == '<title>'):
                    a = i
                if (x[i:i + 8] == '</title>'):
                    b = i + 8
                    break
            if(len(x[a:b]) > 10):
                print(url + "   "+ x[a:b])
                a=0
                b=1
                break
        fr.close()

print('Choose:')
print(' 1. Check pages')
print(' 2. Download')
choose = input('Choose = ')
if(int(choose) == 1):
    checkPages()
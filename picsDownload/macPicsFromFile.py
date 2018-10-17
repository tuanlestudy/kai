import os
import webbrowser
import os.path
import urllib
import sys
#import urllib.request

def write2file(link, strWrite):
    fw = open(link, 'w')
    fw.write(strWrite)
    fw.close()

def add2file(link, strWrite):
    fw = open(link, 'a')
    fw.write(strWrite)
    fw.write('\n')
    fw.close()

def checkPages():
    pageS = input('Start Number: ')
    pageE = input('End Number: ')
    fileSave = "./files/link"+str(pageS)+"-"+str(pageE)+".txt"
    fw = open(fileSave, 'w')
    fw.close()
    a=0
    b=1
    fa = open(fileSave, 'a')
    for k in range(int(pageS), int(pageE)):
        print(k)
        url = 'https://hdasianpics.com/album/' + str(k) + '/'
        response = urllib.urlopen(url)
        html = response.read()

        fw = open("./files/temp", 'w')
        fw.write(html)
        fw.close()
        fr = open("./files/temp", 'r')
        for x in fr:
            for i in range(0, len(x)):
                if (x[i:i+7] == '<title>'):
                    a = i
                if (x[i:i + 8] == '</title>'):
                    b = i + 8
                    break
            if(len(x[a:b]) > 10):
                if(x[a:b] != "<title>HD Asian Pics | Hot Girls, Sexy Models, High Quality Photos</title>"):
                    sys.stdout.write("\033[F")
                    print(url + "   "+ x[a:b])
                    fa.write(k + "   " + url + "   "+ x[a:b])
                    fw.write('\n')
                    print(k)
                #print(url + "   " + x[a:b])
                a=0
                b=1
                break
        fr.close()

        sys.stdout.write("\033[F")
    fa.close()

def openPages():
    webbrowser_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"
    fr = open("./files/link2000-2999.txt", 'r')
    count = 0
    for x in fr:
        count = count + 1
        for i in range(0, len(x)):
            if(x[i] == " "):
                url = x[0:i]
                print(url)
                webbrowser.open_new_tab(url)
                break
        if(count == 10):
            check = input("Continous? ")
            if(check == 'n'):
                break
            else:
                count = 0
    fr.close()

def cutHtml(file, filetemp, wordS, wordE):
    checkIn = False
    checkOut = False
    fw = open(filetemp, 'w')
    fw.close()
    fr = open(file, 'r')
    fa = open(filetemp, 'a')
    ini = 0
    for x in fr:
        for i in range(0, len(x)):
            if (x[i:i+len(wordS)] == wordS):
                checkIn = True
            if (x[i:i+len(wordE)] == wordE):
                checkOut = True
                ini = i
                break
        if (checkOut == True):
            fa.write(x[0:ini])
            break
        if (checkIn == True):
            #print(x)
            fa.write(x)

    fa.close()
    fr.close()

    fw = open(file, 'w')
    fr = open(filetemp, 'r')
    for x in fr:
        fw.write(x)
    fw.close()
    fr.close()

def getHtml(url):
    if (len(url) > 1):
        response = urllib.urlopen(url)
        html = response.read()
        print("Completed get source from " + url)

        fw = open("./files/html", 'w')
        fw.write(html)
        fw.close()
        print("Completed write source to tempHtml.html")

def copy2file(file, fileTemp):
    fr = open(file, 'r')
    fa = open(fileTemp, 'w')
    for x in fr:
        for i in range(0, len(x)):
            if (x[i] == " "):
                url = x[0:i]
                #print(url)
                fa.write(url + '\n')
                break
    fa.close()
    fr.close()
    print('Completed copy to temp file')

def downloadTotal():
    #copy2file('./files/linkTotal.txt', './files/linkTotalTemp.txt')
    #check = input("Continous? ")
    fr = open('./files/linkTotalTemp.txt', 'r')
    for x in fr:
        getHtml(x)
        cutHtml('./files/html','./files/tempHtml', 'post-content entry-content', 'post-meta entry-meta')
        frhtml = open("./files/html", 'r')
        for a in range(len(x)-1, 0, -1):
            if(x[a] == "/"):
                pages=x[a-4:a]
                break
        os.system('mkdir ./pics/' + pages)
        fw = open('./pics/' + pages + '/link.txt', 'w')
        fw.write(x + '\n')
        print (pages)
        check = False
        beg = 0
        end = 0
        count = 100
        for ht in frhtml:
            for i in range(0, len(ht)):
                if (ht[i:i + 3] == 'jpg'):
                    end = i + 3
                    j = i
                    while True:
                        j = j - 1
                        if (ht[j:j + 4] == 'http'):
                            beg = j
                            check = True
                            break
                if (check == True):
                    url_imageS = ht[beg:end]
                    fw.write(str(count) + ' ' + url_imageS+'\n')
                    # print(url_imageS)
                    print('wget ' + url_imageS + ' -O ./pics/' + pages + '/' + str(count) + '.jpg')
                    os.system('wget ' + url_imageS + ' -O ./pics/' + pages + '/' + str(count) +  '.jpg')
                    count = count + 1
                    check = False
        fw.close()
        frhtml.close()
    fr.close()


print('Choose:')
print(' 1. Check pages')
print(' 2. Open pages')
print(' 3. Download Total')
choose = input('Choose = ')
if(int(choose) == 1):
    checkPages()
if(int(choose) == 2):
    openPages()
if(int(choose) == 3):
    downloadTotal()
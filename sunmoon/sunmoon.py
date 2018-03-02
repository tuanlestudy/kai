import urllib2

def sunmoon(urllink):
    x=0
    y=0
    m=0
    n=0
    o=0
    p=0
    countnew=0
    response = urllib2.urlopen(urllink)
    html = response.read()
    print ('Reading pages')
    for x in range(0,len(html)-1):
        if ( html[x] == 'N'):
            if(html[x:x+14]=='Normal Threads'):
                break
        x+=1
    x+=14
    for y in range(x,len(html)-1):
        if ( html[y] == '<'):
            if(html[y:y+5]=='</ol>'):
                break
        y+=1
    y= y + 5
    member = ""
    threads = ""
    print("Complete Reading")
    print("Checking new threads")
    for m in range(x,y):
        if(html[m] == 'm'):
            if(html[m:m+8]=='members/'):
                #find member name and id
                for n in range(m+8,y):
                    if(html[n]=='/'):
                        member = html[m:n]
                        break
                #find threads
                for o in range(n+1,y):
                    if(html[o]=='t'):
                        if(html[o:o+8]=='threads/'):
                            for p in range(o+8,y):
                                if(html[p]=='"'):
                                    threads= html[o:p]
                                    break
                            break
                #print (member + '     ' + threads)
                countnew = openfile(member, threads, countnew)
    print("\n")
    print (str(countnew) + " new threads")

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
            

if __name__ == "__main__":
    #openfile("test","test")

    urllink="http://thiendia.com/diendan/forums/phim-sex-viet-nam-vietnamese-sex-video.19/"
    #print("\n\n")
    sunmoon(urllink)
    print("\n\n")
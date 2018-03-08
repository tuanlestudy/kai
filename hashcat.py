import os

cm = "hashcat64 -m 2500 -w 3  --status "
filecap = raw_input("File hccapx: ")
total = 0
for file_type in ['passwordlist']:
    for pwd in os.listdir(file_type):
        total = total + 1
count = 1            
for file_type in ['passwordlist']:
    for pwd in os.listdir(file_type):
        pwdPath = "E:/KaiHacker/passwordlist"+'/'+pwd
        print ("Processing..... (" + str(count) + "/" + str(total) + ")")
        print(pwd)
        os.system(cm + filecap + pwdPath)
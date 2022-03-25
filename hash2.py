'''
Young Sol Kim
SY402
Citation: In lab sheet
Some code has been copied and adapted from online resources.

'''


import os 
import hashlib
import time
def baseline():
    print('Scanning...')
    path = '/'
    filelist = []
    skiplist = ['dev/', 'usr/','proc/', 'run/', 'sys/', 'tmp/','var/lib', 'var/run/', 'var/', 'bin/', 'etc/', 'lib/']
    #the code below to walk through the files were taken from an online resource which was cited in the citations
    for root, dirs, files in os.walk(path):
        for file in files:
            if any(ele in os.path.join(root,file) for ele in skiplist) == False:
                filelist.append(os.path.join(root,file))
    log = '/home/sy402/hashlist.txt'
    print("Your host has " + str(len(filelist)) + " files")
    with open(log, 'w') as f:
        for file in filelist:
            try: 
                #the code below to get time format and the hashing was taken from an online resource which was cited.
                with open(file, 'rb') as g:
                    m = hashlib.sha256()
                    chunk = 0
                    while chunk!=b'':
                        chunk = g.read(4096)
                        m.update(chunk)
                modTime = os.path.getmtime(file)
                modTimeS = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(modTime))
                f.write((str(file) + '\t' + m.hexdigest() + '\t' + str(modTimeS) + '\n'))
            except:
                f.write((str(file) + '\t' + 'unhashable' + '\t' + 'unhashable' + '\n'))
                continue
    print('Completed baseline')
    return

def checks():
    print('Checking...')
    with open('/home/sy402/hashlist.txt') as f:
        data = f.readlines()
    dic = {}
    for i in data:
        temp = i.split()
        dic[temp[0]] = [temp[1], temp[2], 0]
    path ='/'

    skiplist = ['dev/', 'usr/', 'proc/', 'run/', 'sys/', 'tmp/', 'var/lib/','var/run/', 'var/', 'bin/', 'etc/', 'lib/']
    print('Summary:')
    #the code below to iterate through the files and get the absolute path was taken from a website and was cited in citations.
    for root, dirs, files in os.walk(path):
        for file in files:
            if any(ele in os.path.join(root,file) for ele in skiplist) == True:
                continue
            file = os.path.join(root,file)
            if file not in dic:
                print(file, " is new/moved")
                continue
            else: 
                if dic[file][0] == 'unhashable':
                    dic[file][2] = 1
                    continue

                #the code below to hash was taken from an online resource and was cited in the citations.
                with open(file, 'rb') as g:
                    m = hashlib.sha256()
                    chunk=0
                    while(chunk!=b''):
                        chunk = g.read(1024)
                        m.update(chunk)
                has= m.hexdigest()
                if has!= dic[file][0]:
                    print(file, " integrity was loss due to different hash")
                dic[file][2] = 1
    for i in dic:
        if dic[i][2]!=1:
            print(dic[i][2])
            print(i, " is a missing file in the system")
                #modTime = os.path.getmtime(file)
                #modTimeS = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(modTime))
                #if modTimeS != dic[file][1]:
                #    print(file, " has a new modification date")
    print('Summary Completed.')
    return


    
    



def main():
    mes = 0
    while(mes!='3'):
        mes = input('Enter (1) for baseline or (2) for checks or (3) to exit: ')
        if mes == '1':
            baseline()
        if mes == '2':
            checks()
main()
        

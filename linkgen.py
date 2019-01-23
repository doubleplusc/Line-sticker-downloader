import webbrowser
import sticker_dl as sd
import os
import subprocess as sp

def proper(s):
    p = ''.join(c for c in s if (c.isalnum() or c==' '))
    return p

print('Reading numbers.txt file...\n')
dirs = os.listdir()
if (not os.path.isfile('numbers.txt')):
    print('Could not find the numbers.txt file, Exiting...')
    exit()

source=open("numbers.txt", 'r')
ids=[]
#dest=open("links.txt", 'w')
for line in source:
    pid = line.strip()
    if pid not in ids:
        ids.append(pid)
source.close()

print('-'*25)
dirs = os.listdir()
if "_static" not in dirs:
    sp.call(["mkdir", "_static"])
print("\nDownloading static stickers\n")
i=1
for pid in ids:
    print(i, "/", len(ids), end=':\t')
    i+=1
    sd.dwnl(pid, 0)

#for d in dirs:
#    if (d[0]!='.' and '.py' not in d and d!='_animated' and d!='_static' and d!='__pycache__' and '.txt' not in d and '.sh' not in d):
#        sp.call(['rsync', '-r', '--remove-source-files', d, '_static'])


print('\n'+'-'*25)
dirs = os.listdir()
if "_animated" not in dirs:
    sp.call(["mkdir", "_animated"])
print("\nDownloading animated stickers\n")
i=1
for pid in ids:
    print(i, "/", len(ids), end=':\t')
    i+=1
    sd.dwnl(pid, 1)

#for d in dirs:
#    if (d[0]!='.' and '.py' not in d and d!='_animated' and d!='_static' and d!='__pycache__' and '.txt' not in d and '.sh' not in d):
#        sp.call(['rsync', '-r', '--remove-source-files', d, '_animated'])

print("\nDo you want to convert animated packs to gif? [y/n]")
c = input()
if(c=='y' or c=='Y'):
    #print("Converting animated stickers from apng to gif")
    dirs = os.listdir('_animated')
    for d in dirs:
        if d[0]!='.':
            files = os.listdir('_animated/'+d)
            print('Converting', d)
            for f in files:
                if "apng" in f:
                    sp.call(["apng2gif", '_animated/'+d+"/"+f, '_animated/'+d+"/"+f[:-4]+"gif"])  
                    sp.call(["mogrify", "-loop", "0", '_animated/'+d+"/"+f[:-4]+"gif"])
                    sp.call(["rm", '_animated/'+d+"/"+f])
            
print("Do you want to split static packs at 30 limit? [y/n]")
c = input()
if(c=='y' or c=='Y'):
    dirs = os.listdir('_static')
    nf = 0
    for d in dirs:
        if d[0]!='.':
            files = os.listdir('_static/'+d)
            nf = len(files)
            if (nf>30):
                sd = proper(d)+"extra"
                print("extras exist in ", d)
                sp.call(["mkdir", '_static/'+d+"/"+sd])
                #print("directory made")
                for i in range (30, nf):
                    f = files[i]
                    sp.call(["mv", '_static/'+d+'/'+f, '_static/'+d+'/'+sd])
            #print ("moved")
#print('Removing empty folders')
#sp.call(['find', '.', '-type', 'd', '-empty', '-delete'])

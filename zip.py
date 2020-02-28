import os, sys, tarfile, os.path

from pip._vendor.distlib.compat import raw_input

'''
def unzip():
    my_tar= tarfile.open('0.zip')
    my_tar.extractall(r'C:\Users\rbazan536\Desktop\test')
    my_tar.close()


path=r"C:\Users\rbazan536\Desktop\rename_test"
files = os.listdir(path)
i = 1
for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(index), '.zip'])))
    unzip()
'''
print("Enter the INC")
IncName = raw_input()
path = r'C:\Users\rbazan536\Desktop\test'
checkDir = path + "\\" + IncName

#print (checkDir)
isdir = os.path.isdir(checkDir)
print(isdir)

def createDir():
    print("What is the INC number you are working on?")
    Inc = raw_input()


if os.path.isdir(checkDir):
    print("hello")
else:
    print("would you like to create one")
    answer = raw_input()
    if answer == 'yes':
        createDir()

    else:
        print("bye")


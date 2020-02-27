import os, sys, tarfile

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

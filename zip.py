import os, sys, tarfile

my_tar= tarfile.open('test.tgz')
my_tar.extractall(r'C:\Users\rbazan536\Desktop\test')
my_tar.close()
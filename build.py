#!/usr/bin/env python


import zipfile
import os,stat


FILEZIP='Emerge.zip'
DESTFILE="EmergeStats.py"

#

os.chdir('src')
with zipfile.ZipFile("../"+FILEZIP, 'w', zipfile.ZIP_DEFLATED) as myzip:
    myzip.write('__main__.py')
    myzip.write('emerge.py')
    myzip.write('MainWin.py')
    myzip.close()

os.chdir('..')
a=open(DESTFILE,"wb")
a.write(b"#!/usr/bin/env python\n")
a.write(open(FILEZIP,'rb').read())
os.chmod('EmergeStats.py',stat.S_IRWXU|stat.S_IRGRP|stat.S_IXGRP|stat.S_IROTH|stat.S_IXOTH)
os.unlink(FILEZIP)

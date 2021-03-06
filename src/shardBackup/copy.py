from subprocess import run
from sys import exit
from shutil import copy2
import os # for unclear reasons importing just os.stat and os.chown doesn't work
import stat

def rsync(fobject0, fobject1): # takes two file objects and transmits 0 to 1
    """
    a call to copying using rsync
    >>>rsync('./.gitkeep','/other/')
    rsync output....
    """
    try:
        run(['rsync', #rsync is a major program
            '-avzz', #a = archive, v= verbose, zz=compress 
            '-n', # n = simulate
            '--info=progress2', # prints info such as how fast it is downloading
            fobject0,
            fobject1
            ])
    except:
        print(f"Unable to launch rsync copying - despite finding rsync installed")
        exit(1)

def copy(fobject0, fobject1): #copies file and then changes perms/owner - https://stackoverflow.com/questions/19787348/copy-file-keep-permissions-and-owner
    """
    a function that copies and keeps group and owner attributes
    >>>copy("file0", "file1")
    
    """
    try:
        copy2(fobject0, fobject1) # copy file
        st = os.stat(fobject0) # make variable of source file attributes
        os.chown(fobject1, st[stat.ST_UID], st[stat.ST_GID]) # 
    except:
        print(f"Unable to copy {fobject0} to {fobject1}. I told you it was in alpha.")
        exit(1)
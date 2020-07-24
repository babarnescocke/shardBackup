import subprocess
import sys

def rsync(fobject0, fobject1):
    """
    a call to copying using rsync
    """
    try:
        subprocess.run(['rsync', #rsync is a major program
            '-avzz', #a = archive, v= verbose, zz=compress 
            '-n', # n = simulate
            '--info=progress2' # prints info such as how fast it is downloading
            'fobject0'
            'fobject1'
            ])
    except:
        print(f"Unable to launch rsync copying - despite finding rsync installed")
        sys.exit(1)
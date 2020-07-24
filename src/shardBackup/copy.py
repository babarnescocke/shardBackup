import subprocess

def rsync():
    """
    a call to copying using rsync
    """
    try:
        return subprocess.Popen(['rsync','-avzz','-v',''])
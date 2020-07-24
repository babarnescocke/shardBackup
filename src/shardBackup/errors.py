from os import access, R_OK, W_OK
from shutil import which

"""
series of functions to process errors, check sanity
"""

def dirReadable(dirname):
	return access(dirname, R_OK)

def dirWritable(dirname):
	return access(dirname, W_OK)

def progExists(progname):
    return which(progname) is not None


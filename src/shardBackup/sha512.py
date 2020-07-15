import hashlib
## this is an added feature to ensure a disk that hasn't been in use for a while is still worth trusting


file = "cli.py"  ## NEED TO CHANGE
BLOCK_SIZE = 65536 

with open(file, 'rb') as f: # Open the file to read it's bytes
    fb = f.read(BLOCK_SIZE) # Read from the file. Take in the amount declared above
    while len(fb) > 0: # While there is still data being read from the file
        file_hash.update(fb)
        fb = f.read(BLOCK_SIZE) 

print (file_hash.hexdigest())

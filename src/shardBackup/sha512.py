import hashlib

# https://stackoverflow.com/a/44873382

def sha512sum(filename): #named after linux util of same name
    """
    takes a filename and then iterates over that file adding to the sha512 hash until completed - returns sha512
    using sha512 to prevent colisions
    
    below code is within 20% of sha512sum util on files tested between 2K and 8G

    >>>sha512sum("somefile")
    '10943f902f1760d7ff458f10ecfa8f790d6b0988455a5e8a545473abc53454294874c88e2e1ece57f6b7b353716a441f31a1af555b130125a827557ce436fe50'
    """
    h  = hashlib.sha512() 
    b  = bytearray(128*1024)
    mv = memoryview(b)
    with open(filename, 'rb', buffering=0) as f: # stop buffering in open itself
        for n in iter(lambda : f.readinto(mv), 0):
            h.update(mv[:n])
    return h.hexdigest()
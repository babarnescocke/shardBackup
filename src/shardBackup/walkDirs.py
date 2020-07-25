import os

# Print every file with its size recursing through dirs // https://www.devdungeon.com/content/walk-directory-python
def recurse_dir(root_dir):
    """
    Used to walk a given dir. recursively and print out files
    >>>
    >>>root_dir("")
    shardBackup/Pipfile - 138 bytes
    """
    root_dir = os.path.relpath(root_dir)
    for item in os.listdir(root_dir):
        item_full_path = os.path.join(root_dir, item)
        if os.path.isdir(item_full_path):
            recurse_dir(item_full_path)
        else:
            print(f"{os.stat(item_fu    ll_path).st_size}   {item_full_path}")


""" pseudo code:
size = 0b
dsize = 4k
targsize = lots of bytes
walk dir
  if file
    fsize = file_size + 131 bytes + len("basename of file".encode('utf-8'))
    if fsize + size <= targetsize
  if dir
    dsize + 
"""

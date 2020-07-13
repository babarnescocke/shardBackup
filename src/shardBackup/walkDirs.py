import os

# Print every file with its size recursing through dirs // https://www.devdungeon.com/content/walk-directory-python
def recurse_dir(root_dir):
    """
    Used to walk a given dir. recursively and print out files
    >>>
    >>>root_dir("")
    shardBackup/Pipfile - 138 bytes
    """
    root_dir = os.path.abspath(root_dir)
    for item in os.listdir(root_dir):
        item_full_path = os.path.join(root_dir, item)

        if os.path.isdir(item_full_path):
            recurse_dir(item_full_path)
        else:
            print("%s - %s bytes" % (item_full_path, os.stat(item_full_path).st_size))
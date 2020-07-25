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
        if os.path.isdir(item_full_path): #if current object being iterated over is dir, keep iterating inthat subfolder
            try:
                recurse_dir(item_full_path)
            except PermissionError:
                print(f"Permission Denied in {item_full_path}") # this covers instances where the root source dir may be readabl/permissible but some subdir isn't
        else: # if an object isn't a dir we treat it as a file
            obj = {'fobject' : item_full_path, 'fobject_size' : os.stat(item_full_path).st_size}
            print(f"{obj}")

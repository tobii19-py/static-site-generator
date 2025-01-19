import os, shutil

def copy_static(src_path, dest_path):
    copied_paths = []

    if os.path.exists(src_path):
        if os.path.exists(dest_path):
            shutil.rmtree(dest_path)

        os.mkdir(dest_path)
        items = os.listdir(src_path)
        
        for item in items:
            file = os.path.join(src_path, item)

            if os.path.isfile(file) == True:
                shutil.copy2(file, dest_path)
                copied_paths.append(file)
            else:
                dest_path = os.path.join(dest_path, item)
                cp = copy_static(file, dest_path)
                copied_paths.extend(cp)         
    else:
        raise ValueError("Invalid: Enter a valid source directory")
    
    return copied_paths
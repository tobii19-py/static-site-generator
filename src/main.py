from textnode import TextNode, TextType
import os, shutil

def copy_static(src_path, dest_path):

    if os.path.exists(src_path):
        if os.path.exists(dest_path):
            shutil.rmtree(dest_path)

        os.mkdir(dest_path)
        files = os.listdir(src_path)
        print(files)
        
        for content in files:
            file = os.path.isfile(os.path.join(src_path, content))
            print(file)
            if file:
                shutil.copy2(file, dest_path)
            
    else:
        raise ValueError("Invalid: Enter a valid source directory")

def main():
    test = TextNode("This is a test", TextType.BOLD, "https://www.boot.dev")
    print(test)

    src = "static"
    dest = "public"
    copy_static(src, dest)

    

if __name__ == "__main__":
    main()
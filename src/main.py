from textnode import TextNode, TextType
from copystatic import copy_static

def main():
    src = "static"
    dest = "public"
    print("Deleting public directory...")
    copied_files = copy_static(src, dest)
    print("Copying static files to public directory...")
    print("\nFiles copied:")

    for file in copied_files:
        print(f" - {file}")

    

if __name__ == "__main__":
    main()
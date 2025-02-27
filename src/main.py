from textnode import TextNode, TextType
from copystatic import copy_static
from generatepage import generate_pages_recursive

def main():
    src = "static"
    dest = "public"
    print("Deleting public directory...")
    copied_files = copy_static(src, dest)
    print("Copying static files to public directory...")
    print("\nFiles copied:")

    for file in copied_files:
        print(f" - {file}")

    
    generate_pages_recursive("content/", "template.html", "public/")
    

if __name__ == "__main__":
    main()
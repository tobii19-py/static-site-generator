from textnode import TextNode, TextType
import os

def main():
    test = TextNode("This is a test", TextType.BOLD, "https://www.boot.dev")
    print(test)

    src_path = "static"
    dest_path = "public"
    if os.path.exists(src_path):
        if os.path.exists(dest_path):
            print(dest_path)
        else:
            raise ValueError("Invalid: Enter a valid destination directory")
    else:
        raise ValueError("Invalid: Enter a valid source directory")
    

if __name__ == "__main__":
    main()
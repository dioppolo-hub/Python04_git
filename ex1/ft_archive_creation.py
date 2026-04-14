import sys


def transform_data():
    print("Transform Data:")
    text = (
        "---\n\n"
        "[FRAGMENT 001] Digital preservation protocols established 2087#\n"
        "[FRAGMENT 002] Knowledge must survive the entropy wars#\n"
        "[FRAGMENT 003] Every byte saved is a victory against oblivion#\n\n"
        "---\n"
    )
    f = open(sys.argv[1], "w")
    f.write(text)
    print(text, end="")
    f.close()


def new_file():
    print("Enter new file name (or empty): ", end="")
    new_file = input()
    if new_file == "":
        print("Not saving data")
        f.close()
    else:
        print(f"Saving data to '{new_file}'")
        n = open(new_file, "w")
        n.write(
            "[FRAGMENT 001] Digital preservation protocols established 2087#\n"
            "[FRAGMENT 002] Knowledge must survive the entropy wars#\n"
            "[FRAGMENT 003] Every byte saved is a victory against oblivion#\n"
        )
        n.close()
        print(f"Data saved in file '{new_file}'\n")


if __name__ == "__main__":
    f = None
    try:
        argc = len(sys.argv)
        if argc == 1:
            raise Exception
        print("=== Cyber Archives Recovery ===")
        f = open(sys.argv[1])
        cont = f.read()
        print(cont, end="")
        transform_data()
        new_file()
    except PermissionError:
        print(f"Accessing file '{sys.argv[1]}'")
        print(
            f"Error opening file '{sys.argv[1]}':"
            f"[Errno 13] permission denied: '{sys.argv[1]}'\n"
            )
    except FileNotFoundError:
        print(f"Accessing file '{sys.argv[1]}'")
        print(
            f"Error opening file '{sys.argv[1]}':"
            f"[Errno 2] No such file or directory: '{sys.argv[1]}'\n"
            )
    except Exception:
        print(f"Usage: '{sys.argv[0]}' <file>\n")
    finally:
        if f is not None:
            f.close()
            print(f"File '{sys.argv[1]}' closed\n")
        else:
            exit()

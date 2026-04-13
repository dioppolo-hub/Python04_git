import sys


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
            print(f"File '{sys.argv[1]}' closed")

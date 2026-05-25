import sys
from typing import TextIO


def transform_data() -> str:
    print("Transform Data:")
    print(f"Accessing file: {sys.argv[1]}")
    f = open(sys.argv[1])
    newf: str = ""
    for line in f:
        newf += line.strip() + '#\n'
    print("---\n")
    print(newf)
    print("---")
    f.close()
    return newf


def new_file(f: TextIO, newf: str) -> None:
    print("Enter new file name (or empty): ", end="")
    new_file = input()
    if new_file == "":
        print("Not saving data")
        f.close()
    else:
        print(f"Saving data to '{new_file}'")
        n = open(new_file, "w")
        n.write(newf)
        n.close()
        print(f"Data saved in file '{new_file}'\n")


def main() -> None:
    f = None
    try:
        argc = len(sys.argv)
        if argc == 1:
            raise Exception
        print("=== Cyber Archives Recovery ===")
        f = open(sys.argv[1])
        cont = f.read()
        print(cont)
        f.close()
        newf = transform_data()
        new_file(f, newf)
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


if __name__ == "__main__":
    main()

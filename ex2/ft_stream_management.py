import sys
from typing import TextIO


def transform_data() -> str:
    sys.stdout.write("\nTransform Data:\n")
    sys.stdout.write(f"Accessing file: {sys.argv[1]}")
    f = open(sys.argv[1])
    newf: str = ""
    for line in f:
        newf += line.strip() + '#\n'
    sys.stdout.write("---\n")
    sys.stdout.write(newf)
    sys.stdout.write("---")
    f.close()
    return newf


def new_file(f: TextIO, newf: str) -> None:
    sys.stdout.write("\nEnter new file name (or empty): ")
    new_file = input()
    if new_file == "":
        sys.stdout.write("Not saving data")
        f.close()
    else:
        sys.stdout.write(f"Saving data to '{new_file}'\n")
        n = open(new_file, "w")
        n.write(newf)
        n.close()
        sys.stdout.write(f"Data saved in file '{new_file}'\n")


def main() -> None:
    f = None
    try:
        argc = len(sys.argv)
        if argc == 1:
            raise Exception
        sys.stdout.write("=== Cyber Archives Recovery ===\n")
        f = open(sys.argv[1])
        cont = f.read()
        print(cont)
        f.close()
        newf = transform_data()
        new_file(f, newf)
    except PermissionError:
        sys.stderr.write(f"Accessing file '{sys.argv[1]}'\n")
        sys.stderr.write(
            f"[STDERR] Error opening file '{sys.argv[1]}': "
            f"[Errno 13] permission denied: '{sys.argv[1]}'\n"
            )
    except FileNotFoundError:
        sys.stderr.write(f"Accessing file '{sys.argv[1]}'\n")
        sys.stderr.write(
            f"[STDERR] Error opening file '{sys.argv[1]}': "
            f"[Errno 2] No such file or directory: '{sys.argv[1]}'\n"
            )
    except Exception:
        sys.stderr.write(f"[STDERR] Usage: '{sys.argv[0]}' <file>\n")
    finally:
        if f is not None:
            f.close()
            sys.stdout.write(f"File '{sys.argv[1]}' closed\n")
        else:
            exit()


if __name__ == "__main__":
    main()

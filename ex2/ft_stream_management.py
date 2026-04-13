import sys


def transform_data():
    sys.stdout.write("\nTransform Data:\n")
    text = (
        "---\n\n"
        "[FRAGMENT 001] Digital preservation protocols established 2087#\n"
        "[FRAGMENT 002] Knowledge must survive the entropy wars#\n"
        "[FRAGMENT 003] Every byte saved is a victory against oblivion#\n\n"
        "---\n"
    )
    f = open(sys.argv[1], "w")
    f.write(text)
    sys.stdout.write(text)
    f.close()


def new_file():
    sys.stdout.write("\nEnter new file name (or empty): ")
    new_file = sys.stdin.readline().strip()
    if new_file == "":
        sys.stdout.write("Not saving data")
        f.close()
    else:
        sys.stdout.write(f"Saving data to '{new_file}'\n")
        n = open(new_file, "w")
        n.write(
            "[FRAGMENT 001] Digital preservation protocols established 2087#\n"
            "[FRAGMENT 002] Knowledge must survive the entropy wars#\n"
            "[FRAGMENT 003] Every byte saved is a victory against oblivion#\n"
        )
        n.close()
        sys.stdout.write(f"Data saved in file '{new_file}'\n")


if __name__ == "__main__":
    f = None
    try:
        argc = len(sys.argv)
        if argc == 1:
            raise Exception
        sys.stdout.write("=== Cyber Archives Recovery ===\n")
        f = open(sys.argv[1])
        cont = f.read()
        sys.stdout.write(cont)
        transform_data()
        new_file()
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

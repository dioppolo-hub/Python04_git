def secure_archive(file: str, wr: str, cont: str) -> tuple[bool, str]:
    try:
        if wr == "r":
            with open(file, wr) as f:
                r = f.read()
            return (True, r)
        elif wr == "w":
            with open(file, wr) as f:
                f.write(cont)
            return (True, cont)
        elif not wr == "w" or not wr == "r":
            raise Exception
        else:
            return (False, "Error")
    except FileNotFoundError:
        print("Using 'secure_archive' to read a nonexistent file:")
        return (False, "[Errno 2] No such file or directory")
    except PermissionError:
        print("Using 'secure_archive' to read an inaccessible file:")
        return (False, "[Errno 13] Permission denied")
    except Exception:
        print("Wrong action to perform, please retry with 'r' or 'w'")
        exit()


if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")
    cont = (
        "[FRAGMENT 001] Digital preservation protocols established 2087\n"
        "[FRAGMENT 002] Knowledge must survive the entropy wars\n"
        "[FRAGMENT 003] Every byte saved is a victory against oblivion\n"
    )
    file = "ancient_fragment.txt"
    wr = "r"
    t: tuple[bool, str] = secure_archive(file, wr, cont)
    if wr == "r" and t[0]:
        print("Using 'secure_archive' to read from a regular file:")
        print(f"{t[0]}, {t[1]}\n")
    elif wr == "r" and not t[0]:
        print(f"{t[0]}, {t[1]}")
    elif wr == "w" and t[0]:
        print(
            "Using 'secure_archive'"
            "to write previous content to a new file:"
        )
        print(f"{t[0]}, Content successfully written to file\n")
    elif wr == "w" and not t[0]:
        print(f"{t[0]}, {t[1]}")

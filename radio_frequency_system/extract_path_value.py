import sys


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} filename key")
        sys.exit(1)

    filename = sys.argv[1]
    key = sys.argv[2]

    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line.startswith(f"{key}:"):
                    parts = line.split(':', 1)
                    if len(parts) == 2:
                        value = parts[1].strip()
                        print(value)
                        return

        print(f"Key '{key}' not found in file.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)


if __name__ == "__main__":
    main()

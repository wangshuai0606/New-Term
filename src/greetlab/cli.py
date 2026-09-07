import argparse
import sys

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--name", required=True)
    a = p.parse_args()
    name = a.name.strip()
    if not name:
        print("Error: --name cannot be empty or whitespace only", file=sys.stderr)
        sys.exit(2)
    print(f"Hello, {name}!")

if __name__ == "__main__":
    main()

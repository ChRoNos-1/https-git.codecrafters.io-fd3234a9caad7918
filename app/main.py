import sys


def main():
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")

    # Wait for user input
    command = input()
    if command == "exit 0":
        sys.exit(0)
    elif command[0:3]=="echo":
        print(command[5::])
    else:
        print(f"{command}: command not found")
    
    main()
    


if __name__ == "__main__":
    main()

import sys


def main():
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")

    # Wait for user input
    command,  = input()
    argv = command.split()
    if argv[0] == "exit":
        exit(int(argv[1]))
    elif argv[0] == "echo":
        print ("".join(argv[1:]))
        #print(command[5::])
    else:
        print(f"{command}: command not found")
    
    main()
    


if __name__ == "__main__":
    main()

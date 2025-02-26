import sys


def main():
    # Uncomment this block to pass the first stage
    while True:
        sys.stdout.write("$ ")

    # Wait for user input
        command  = input()
        argv = command.split()
        if argv[0] == "type":
            if argv[1]=="exit" or argv[1]=="echo" or argv[1]=="type":
                print (f"{argv[1]} is a shell builtin")
            else:
                print(f"{argv[5:]}: not found")
        elif argv[0] == "exit":
            exit(int(argv[1]))
        elif argv[0] == "echo":
            print (" ".join(argv[1:]))
            #print(command[5::])
        else:
            print(f"{command}: command not found")
    


if __name__ == "__main__":
    main()

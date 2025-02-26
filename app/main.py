import sys
import shutil

def main():
    # Uncomment this block to pass the first stage
    while True:
        sys.stdout.write("$ ")

    # Wait for user input
        command  = input()
        argv = command.split()
        if path := shutil.which(argv[0]):
            print (f"Arg #0 (program name): {argv[0]}/n")
            print (f"Arg #1: {argv[1]}")
        if argv[0] == "type":
            if argv[1]=="exit" or argv[1]=="echo" or argv[1]=="type":
                print (f"{argv[1]} is a shell builtin")
            elif path := shutil.which(argv[1]):
                print(f"{command[5:]} is {path}")
            else:
                print(f"{command[5:]}: not found")
        elif argv[0] == "exit":
            exit(int(argv[1]))
        elif argv[0] == "echo":
            print (" ".join(argv[1:]))
            #print(command[5::])
        else:
            print(f"{command}: command not found")
    


if __name__ == "__main__":
    main()

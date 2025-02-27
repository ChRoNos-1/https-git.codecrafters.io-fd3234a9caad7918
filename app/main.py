import sys
import shutil
import subprocess
import os
import shlex

def main():
    # Uncomment this block to pass the first stage
    while True:
        sys.stdout.write("$ ")
        #sys.stdout.flush()

    # Wait for user input
        command  = input()
        argv = shlex.split(command)
        if ">" in argv or "1>" in argv:
            if '>' in argv:
                rin = argv.index('>')
            else:
                rin = argv.index('1>')
            opfl = argv[rin + 1]
            argv = argv[:rin]
            with open (opfl,"w") as file:
                subprocess.run(argv, stdout=file, stderr=sys.stderr)
            continue
        elif '2>' in argv:
            rin = argv.index("2>")
            opfl = argv[rin + 1]
            argv = argv[:rin]
            
            with open (opfl,"w") as file:
                subprocess.run (argv, stderr=file)
                continue
            
        elif '1>>' in argv or '>>' in argv:
            if '>>' in argv:
                rin = argv.index('>>')
            else:
                rin = argv.index('1>>')
            opfl = argv[rin + 1]
            argv = argv[:rin]
            with open (opfl,"w") as file:
                subprocess.run(argv, stdout=file, stderr=sys.stderr)
        
        elif path := shutil.which(argv[0]):
            subprocess.run(argv)
            
        elif argv[0] == "cd":
            path = argv[1]
            path = os.path.expanduser(path)
            if os.path.isdir(path):
                os.chdir(path)
            else:
                print(f"cd: {path}: No such file or directory")
            
        elif argv[0]== "pwd":
            print (f"{os.getcwd()}")
            
        elif argv[0] == "type":
            if argv[1]=="exit" or argv[1]=="echo" or argv[1]=="type" or argv[1]=="pwd" or argv[1]=="cd" :
                print (f"{argv[1]} is a shell builtin")
            elif path := shutil.which(argv[1]):
                print(f"{command[5:]} is {path}")
            else:
                print(f"{command[5:]}: not found")
                
        elif argv[0] == "exit":
            exit(int(argv[1]))
            
        elif argv[0] == "echo":
            print (" ".join(argv[1:]))
            #print(command[7:-2:])
            
        else:
            print(f"{command}: command not found")
    


if __name__ == "__main__":
    main()

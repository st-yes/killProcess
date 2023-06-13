import subprocess
import sys

# run ps aux
# catch line where process name is found
def	catchProcess(processName):
    line = ""
    theLine = ""
    processes = subprocess.run(['ps', 'aux'], capture_output=True)
    if (processes.returncode != 0):
        sys.stderr.write("error: ")
        sys.stderr.write(processes.stderr)
    else:
        for i in processes.stdout.decode():
            if (i != "\n"):
                line += i
            else:
                if processName in line:
                    theLine = line
                    break
                line = ""
    if theLine == "":
        sys.stderr.write("ERROR: no process found\n")
    else:
        parts = theLine.split()
        killProc = subprocess.run (['kill', parts[1]])
        if (killProc.returncode != 0):
            sys.stderr.write("error: ")
            sys.stderr.write(killProc.stderr)
        else:
            print(processName, " killed successfully.")

if (__name__ == "__main__"):
    numberOfArguments = len(sys.argv)
    i = 1
    processName = ""
    if numberOfArguments == 1:
        processName = input("input name of the process: ")
    else:
        while (i < numberOfArguments):
            processName += sys.argv[i]
            processName += " "
            i += 1
    catchProcess(processName)
    
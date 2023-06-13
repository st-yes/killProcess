import os
import subprocess
import sys

if (__name__ == "__main__"):
    # get value of environment variable SHELL i.e: /bin/zsh, then store last element, i.e: zsh
    shellName = os.environ.get("SHELL").split('/')[-1]
    configFile = "~/."+ shellName + "rc" # ~/.zshrc or ~/.bashrc depending on the shell
    pwd = subprocess.run(['pwd'], capture_output=True)
    if (pwd.returncode != 0):
        sys.stderr.write("error: ")
        sys.stderr.write(pwd.stderr)
    scriptPlacement=pwd.stdout.decode()
    aliasCommand = 'alias kp="python3.7 ' +  scriptPlacement.strip() + '/killProcess.py"'
    # add alias to config file i.e .zshrc
    with open(os.path.expanduser(configFile), 'r') as file:
        fileContent = file.read()
    if "alias kp=" in fileContent:
        print(configFile, "already have a kp alias")
    else:
        with open(os.path.expanduser(configFile), 'a') as file:
            file.write(aliasCommand + '\n')
    # Execute a new zsh process with the -l flag to start a login shell and thus reload .zshrc
    os.execvp(shellName, [shellName, '-l'])

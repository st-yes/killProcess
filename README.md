
<p align="center">
  <a href="#BUILT WITH">BUILT WITH</a> •
  <a href="#INSTALLATION">INSTALLATION</a> •
  <a href="#USAGE">USAGE</a> •
</p>

<p>
a small python script used to found a running process by name and kill it, additionally an alias <strong>kp</strong> is created for a more convenient use
</p>

## BUILT WITH
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## INSTALLATION
1. Clone the repository to your local machine:
```bash
git clone https://github.com/st-yes/killProcess.git
```
2. Navigate to killProcess directory:
```bash
cd killProcess
```
3. Compile
```bash
make
```
## USAGE

- an alias is created and appended to your shell config file i.e .zshrc
### running the script:
1. with command line arguments
```bash
kp <name of process>
```
2. without command line arguments

```bash
kp
```
<em>This will prompt you to enter the name of the process, simply input the name:</em>
<small>
```
input name of the process: <name of process>
``` 
</small>
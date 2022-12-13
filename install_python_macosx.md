## Install in mac osx

### Install brew 
To install Homebrew, open Terminal or your favorite OS X terminal emulator and run
```
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```
The script will explain what changes it will make and prompt you before the installation begins. Once you’ve installed Homebrew, insert the Homebrew directory at the top of your PATH environment variable. You can do this by adding the following line at the bottom of your ~/.profile file
```
export PATH="/usr/local/opt/python/libexec/bin:$PATH"
```
If you have OS X 10.12 (Sierra) or older use this line instead
```
export PATH=/usr/local/bin:/usr/local/sbin:$PATH
```
Now, we can install Python 3:
```
$ brew install python
```





### Working with Python 3
At this point, you have the system Python 2.7 available, potentially the Homebrew version of Python 2 installed, and the Homebrew version of Python 3 as well.
```
$ python 
```
will launch the Homebrew-installed Python 3 interpreter.
```
$ python2 
```
will launch the Homebrew-installed Python 2 interpreter (if any).
```
$ python3 
```
will launch the Homebrew-installed Python 3 interpreter.

If the Homebrew version of Python 2 is installed then pip2 will point to Python 2. If the Homebrew version of Python 3 is installed then pip will point to Python 3.

The rest of the guide will assume that python references Python 3.

Do I have a Python 3 installed?
``` 
$ python --version
Python 3.7.1 # Success! 
```

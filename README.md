[toc]

# Python PM
##1.1 PM infomation
**This PM is practice python**
```
Part one
	create a public repo on github.com
	Add README, LICENSE, requirements.txt
	Add some practice py file for Python Basic Syntax

Part two
   Text Editor:
```
##1.2 PM Requirements Analysis
1. **System:Ubuntu**
2. **Python version: pyhon 3**

###1.3 Install
 - **apt-get install python3-venv**
 - **apt install git**

##1.3 How to create repo to github with python venv

**1. Create the python3 venv**
>root@ubuntu:~/Desktop# **`cd Python_flask/`**
root@ubuntu:~/Desktop/Python_flask# **`python3 -m venv .env`**
root@ubuntu:~/Desktop/Python_flask# **`ls -a `**
.  .. **`.env`**

**2.  Active the venv**

>root@ubuntu:~/Desktop/Python_flask# **`source .env/bin/activate`**
**`(.env)`** root@ubuntu:~/Desktop/Python_flask# 

**3.  Make sure the python version:**

>(.env) root@ubuntu:~/Desktop/Python_flask# **`python`**
**`Python 3.5.2`** (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
\>>> 
\>>> 

**4.  Add the file to github web**
>(.env) root@ubuntu:~/Desktop/Python_flask# **`echo "#This is a test" > README.md`**
(.env) root@ubuntu:~/Desktop/Python_flask# ls
**README.md**
(.env) root@ubuntu:~/Desktop/Python_flask# **`git init`**
**Initialized empty Git repository in /root/Desktop/Python_flask/.git/**
(.env) root@ubuntu:~/Desktop/Python_flask# **`git add README.md`** 
(.env) root@ubuntu:~/Desktop/Python_flask# **`git config --global user.email "zhanghaichao31@sohu.com"`**
(.env) root@ubuntu:~/Desktop/Python_flask# **`git config --global user.name "sevenzhang7"`**
```
(.env) root@ubuntu:~/Desktop/Python_flask# git status

On branch master
Initial commit
Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

        new file:   README.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        .env/
```
>(.env) root@ubuntu:~/Desktop/Python_flask# **`git commit -c "add the readme.md to github"`**
**fatal: could not lookup commit add the readme.md to github**
(.env) root@ubuntu:~/Desktop/Python_flask# **`git commit -m "add the readme.md to github"`**
>[master (root-commit) 7012c4c] add the readme.md to github
 1 file changed, 1 insertion(+)
 create mode 100644 README.md
(.env) root@ubuntu:~/Desktop/Python_flask# **`git remote add origin https://github.com/sevenzhang7/Python_flask.git`**
(.env) root@ubuntu:~/Desktop/Python_flask# **`git push -u origin master`**
Username for 'https://github.com': **`sevenzhang7`**
Password for 'https://sevenzhang7@github.com': 
Counting objects: 3, done.
Writing objects: 100% (3/3), 240 bytes | 0 bytes/s, done.
Total 3 (delta 0), reused 0 (delta 0)
remote: 
remote: Create a pull request for 'master' on GitHub by visiting:
remote:      https://github.com/sevenzhang7/Python_flask/pull/new/master
remote: 
To https://github.com/sevenzhang7/Python_flask.git
 \* [new branch]      master -> master
Branch master set up to track remote branch master from origin.
(.env) root@ubuntu:~/Desktop/Python_flask# 

**5.  Log out the venv** 
 >(.env) root@ubuntu:~/Desktop/Python_flask# **deactivate**
root@ubuntu:~/Desktop/Python_flask# 


##1.4 Setup the webpage with flask
**1.  git clone https://github.com/miguelgrinberg/flasky.git** 


##1.4 Links
- Website: https://github.com/sevenzhang7/Python_flask.git

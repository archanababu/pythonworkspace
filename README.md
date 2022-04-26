# pythonworkspace

python workspace on github

Welcome to the pythonworkspace wiki!

Follow the instruction provided in the below link, to install python and visual studio code.

https://code.visualstudio.com/docs/python/python-tutorial 

I've followed the same steps to create my first hello world program in python.

After successful setup of python in visual studio, now lets configure it to github repository by following these steps 

1. Goto https://git-scm.com/downloads and download the latest version for your operating system. 

2. Install git client by selecting all the default options.

3. After installation is complete, now restart the visual studio code and do cntrl+shift+p to open command pallet and type git and you will be able to see the git options

4. Now goto your github site and create a new repository

5. In the the new repository, click on clone or download button to copy your repository url

6. In VS code, open command pallet and enter git: clone and hit enter

7. Paste the repository url from github and hit enter. Now you will get a popup to open your github repository in new window. Click open repository button.

Note : Git: Clone is just one time setup and can be used for multiple push/commit.

8. Before doing any change to your github repository make sure you set the global user.name and global user.email value in your git client. 

     $ git config --global user.name "user name"

     $ git config --global user.email email address

8. Create a simple hello world python file in your git repository. And now you will be able to see your changes in source control tab.

9. To commit your changes, just enter any message/short description for the change you made and click cntrl+enter. And you will get a pop window to automatically stage all your changes and commit, just click "Always" button and continue.

10. After the commit step, now you have to push your changes to git repository. So, open command pallet and type git: push and hit enter.

11. For the first time you will be prompted for authenticating. So, enter your GitHub credentials and click ok.

12. Now refresh your github repository page and you will be able to see the your commits.


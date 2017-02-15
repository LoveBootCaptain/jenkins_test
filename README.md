# build executable files for mac, windows, linux from your python scripts

this is a basic test project to build an executable from your python script with all dependencies and python interpreter 
included using pyinstaller. you can build a binary, mac.app or windows.exe.

i created this to have something to build using jenkins running on a raspberry pi as a build and deployment server.
the executable can be deployed on other raspberry nodes in my network without having the hassle to have python version,
installed modules and stuff in sync from developing machine, staging environment or production. 
it creates a single executable file which is able to run independent. 
nice for multi-platform pygame-games or Tkinder dashboards.

the .spec file is used to build the python application.

you can try it without jenkins just by using following terminal commands:

install pyinstaller

`sudo pip3 install pyinstaller`

change into project directory

`cd jenkins_test`

run the compiler

`pyinstaller jenkins_test.spec`

this will create a `/build` and a `/dist` folder inside the project directory. 
inside the `/dist` folder you can find the executable/app/exe after successful build.


tested for:

- raspberry pi (raspbian)
- MacBook Pro / iMac (Mac OS)

still untested:

- Windows (don't have a windows machine, need time to set up a VM for testing)

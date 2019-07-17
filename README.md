# Docker: JOE

## ENV variables

| ENV Variable      |       Description                    |                Default Value                             | Required        |
|:------------:     |:----------------------------------:  |:------------------------------------------------:        |:-------------:  |
| HOST_IP            |      Ip address of host machine                    |  _nil_                                                   |     true        |
| SOURCE_WORK_DIR       |      Working dir where jobscheduler objects are               |  _nil_                                                   |     true        |


## Prep your envioronment. 

To build and run it locally you can do the following:

- Install docker from self service in mac.

- Download and Install xquartz  X.Org X Window System from https://www.xquartz.org/index.html version 2.7.11.dmg

- Open xquartx in applications and navigate to preferences > security > make sure to 
	un-check "Authenticate connections:
	check "Allow network from network clients" is true

- Resart your computer -- Important to restart after installing xquartz 

Follow the commands below to build the container.

cd into the docker-joe/

```bash
#RUN X11 server if not running already
open -a xquartz
```

# To build the container with specific JOE_VERSION u can use the included python script.

Install python

```bash
#install python 
sudo brew install python3

#install pip package manager if not installed already
sudo easy_install pip

#install docker sdk for python 
pip install docker
```
## run the included puthon script. Run this everytime u need to start JOE also supports multiple versions like 1.11.5,1.12.9

```bash
python joe_build_run.py --joe_version 1.12.9 --workdir <YOUR SOURCE_WORK_DIR> --image_name <new name>
```

# For users familliar with docker you can use the below steps instead of using the above python scripts.

```bash
#build docker image using the command below. NOTE: One off step to build the image with JOE_VERSION. Repeat only if u need to switch JOE versions.
docker build -t joe . --build-arg JOE_VERSION='1.12.9'
```

set the env variables first

```bash
#SET HOST_IP variable (Ethernet connection only) If using wifi replace en5 with en0 on the below command
export HOST_IP=$(ifconfig en5 | grep inet | awk '$1=="inet" {print $2}')

#Set work directory This is usually where the cloned git projects are. Joe will be able to navigate into subdirectories for jobscheduler hotfolder
export SOURCE_WORK_DIR=~  #FOLDERS SUBFOLDERS WHERE JOBSCHEDULER OBJECTS ARE
```

To run latest version 1.12.9

```bash
docker run -d --rm -e DISPLAY=$HOST_IP:0 --name joe -v $SOURCE_WORK_DIR:/opt/sos-berlin.com/joe/config/live:cached catchhster/jobscheduler-joe
```

To run specific version 1.11.5

```bash
docker run -d --rm -e DISPLAY=$HOST_IP:0 --name joe_1.11.5 -v $SOURCE_WORK_DIR:/opt/sos-berlin.com/joe/config/live:cached catchhster/jobscheduler-joe:joe_1.11.5
```

***
Notes:
  - Use iterm in mac
  - The xserver needs to be running in mac for hosting the GUI. Mac might sometimes close the server due to inactivity or when logged off so please save the work as often as possible.
  - In JOE SOURCE_WORK_DIR will be binded to /opt/sos-berlin.com/joe/config/live. you will find your projects there.

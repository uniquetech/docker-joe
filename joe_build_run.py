#!/usr/bin/python

import argparse
import docker
import socket
import os
import logging
from os.path import expanduser


class DockerContainers(object):
	def __init__(self,JOE_VERSION,SOURCE_DIR):
		self.JOE_VERSION = JOE_VERSION
		self.SOURCE_DIR = SOURCE_DIR
		self.HOST_IP = socket.gethostbyname(socket.gethostname())
		print("Your env variables are JOE_VERSION {0} SOURCE_DIR {1} HOST_IP {2}".format(JOE_VERSION,SOURCE_DIR,self.HOST_IP))
	
	def docker_init(self):
		return docker.from_env()

	def run_container(self,IMG_NAME,DOCKER_FILE):
		client=self.docker_init()
		img_name_tag = IMG_NAME
		client.images.build(path=DOCKER_FILE,tag=img_name_tag,buildargs={"JOE_VERSION":self.JOE_VERSION},rm=True)
		run_log=client.containers.run(img_name_tag,environment=["DISPLAY={0}:0".format(self.HOST_IP)],volumes={"{0}".format(self.SOURCE_DIR):{"bind":"/opt/sos-berlin.com/joe/config/live","mode":"rw"}},detach=True,remove=True,name='joe')
		print(run_log)
		
def main():
	home = expanduser("~")
	pwd = cwd = os.getcwd()
	parser = argparse.ArgumentParser()
	parser.add_argument('--joe_version',default='1.12.9')
	parser.add_argument('--workdir', default='{0}/'.format(home))
	parser.add_argument('--image_name')
	args = vars(parser.parse_args())

	env = DockerContainers(args['joe_version'],args['workdir'])
	
	env.run_container(args['image_name'],pwd)

if __name__ == '__main__':
    main()

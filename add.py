#!/usr/bin/env python2

import os, sys, subprocess, shutil
import argparse
from argparse import RawTextHelpFormatter

#Prints help message and quits
def help(parser):
	print ""
	parser.print_help()
	print ""
	sys.exit(1)


#Prints error and quits
def error(msg, parser):
	print "ERROR: " + msg
	help(parser)


#Useful finish method
def finish():
	print "\nSUCCESSFULLY FINISHED\n"
	sys.exit(0)


#Useful methods (to keep in mind)
#	map(function, list): Apply a function to list
#	filter(function, list): Filter a list by function



#Useful Wrapper terminal commands
def cd(path=os.environ['HOME']):
	os.chdir(path)
def ls(path='.'):
	return os.listdir(path)
def dirs(path='.'):
	return os.walk(path).next()[1]
def mkdir(path):
	os.mkdir(path)
def rm(path):
	os.remove(path)
def rmr(path):
	os.rmdir(path)
def mv(src, dest):
	shutil.move(src, dest)
def cp(src, dest):
	shutil.copy(src, dest)
def pwd():
	return os.getcwd()
def chmod(path, mode):
	os.chmod(path, mode)


parser = argparse.ArgumentParser(description="Description: Adds urls to the file Batch_Image_Downloader reads from", epilog="********Example Usages*********:\n\npython add.py <link>\n\npython urls_to_download <link> <link>", formatter_class=RawTextHelpFormatter)
parser._optionals.title = "Flag Arguments"
parser.add_argument("file", help="OPTIONAL: the file name that want to add to", nargs="?", default="urls")
parser.add_argument("urls", help="REQUIRED: enter the url that you want to add to the file", nargs="+")

#Print help if no arguments given (use if required arguments)
if len(sys.argv) == 1:
	print ""
	parser.print_help()
	print ""
	sys.exit(1)

args = parser.parse_args()


#Check if input file exists
if not os.exists(args.file):
	error("Input file (default is urls) does not exist")


#Append the urls to the file
for url in args.urls:
	f = subprocess.open(args.file)
	f.append(url+'/n')
f.close()


finish()
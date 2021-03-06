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
	print "\nERROR: " + msg + "\n"
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


parser = argparse.ArgumentParser(description="Description: ", epilog="********Example Usages*********: \n\n", formatter_class=RawTextHelpFormatter)
parser._optionals.title = "Flag Arguments"
parser.add_argument("argument", help="OPTIONAL/REQUIRED: help message")
#Add more arguments here

#Print help if no arguments given (use if required arguments)
# if len(sys.argv) == 1:
# 	help(parser)

#Parse Arguments
args = parser.parse_args()


#>>>>START HERE<<<<<


finish()
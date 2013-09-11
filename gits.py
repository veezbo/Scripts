import os, sys, subprocess
import argparse
from argparse import RawTextHelpFormatter


parser = argparse.ArgumentParser(description="Description: \n\tApplies an action to all git repos in a certain directory", epilog="Example Usage: \n\npython recursive_git.py status\npython recursive_git diff", formatter_class=RawTextHelpFormatter) 
parser.add_argument("command", help="OPTIONAL: git command to execute; default is status", nargs='?', default="status")
parser.add_argument("arguments", help="OPTIONAL: git command's arguments", nargs="*")
parser.add_argument("-d", "--dirs", help="specific directories to run command in", nargs="*")


#Parse arguments
args = parser.parse_args()

#Determines if a directory is a git repository
def isGitRepo(dir):
	return '.git' in os.walk(dir).next()[1]

#Will hold all the git directories
dirs=[]

#Get all Git Repositories from Given List
if args.dirs:
	dirs = filter(isGitRepo, args.dirs)

#Get all Git Repositories in Current Folder if not given list
else:
	dirs = filter(isGitRepo, os.walk('.').next()[1])


#Make the call for each
for dir in dirs:
	os.chdir(dir)
	print "\nDIRECTORY: " + dir
	r = subprocess.call(['git', args.command] + args.arguments)
	os.chdir('..')


#Finish
print "\nSUCCESSFULLY FINISHED\n"
sys.exit(0)

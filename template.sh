#!/bin/bash

#Very Useful Template File for Shell Scripts


#Usage Statement
usage()
{
	echo "
USAGE:


Required Arguments:
	-

Optional Arguments: 
	-u displays this usage statement
	-h displays this usage statement

Examples Uses:
	here
	"
}


#Generates Nice Error Messages
error()
{
	error_message="ERROR "
	error_message+="$1"
	len=${#error_message}
	diff=$(( (80-len) / 2 ))
	if (( diff <= 0 )); then
		echo ""
		echo "$error_message"
		usage
	else
		astString=$(getAstString $diff)
		error_message="${astString}${error_message}${astString}"
		if (( $len%2 == 1 )); then
			error_message+="*"
		fi
		echo ""
		echo "$error_message"
		usage
	fi
}
getAstString()
{
	str=""
	num="$1"
	for (( i=1; i <= num ; i++ ))
	do
		str+="*"
	done
	echo "$str"
}


#Useful for Determining if an Array Contains an Element
containsElement () 
{
  for val in "${@:2}"; do [[ "$val" == "$1" ]] && echo "true"; done
  echo "false"
}


#Generates nice calling messages
call()
{
	echo ""
	echo Calling: $1
	$1
}


#Generates a nice finish message
finish()
{
	echo ""
	echo FINISHED
	echo ""
}

#set -e #Use if you want to exit on any error in the script


#OPTIND=1 #Necessary in a Sourced Script
#Additionally, do returns instead of exists in a sourced script

#Read in Arguments
while getopts ":hu" opt; do
	case $opt in
		h)
			usage
			exit 1
			;;
		u)
			usage
			exit 1
			;;
		:)
			error "Option -$OPTARG requires an argument"
			exit 1
			;;
		\?)
			echo "Invalid Argument: -$OPTARG" >&2
			usage
			exit 1
			;;
	esac
done
shift $(( OPTIND - 1 ))


#call STUFF


finish
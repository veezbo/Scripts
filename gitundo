#!/bin/bash


#Usage Statement
usage()
{
	echo "
USAGE:
Use for Undoing Commits for git (which by the way should have this functionality built in)

Optional Arguments:
	-u displays this usage statement
	-h displays this usage statement
	-n <#> the number of commits to undo (default is 1)
	-H do a hard undo/reset instead (overwrites any local changes since)


Examples Uses:
	bash undo_commit.sh (undoes last commit)
	bash undo_commit.sh -n 4 (undoes last 4 commits)
	bash undo_commit.sh -n 2 -H (undoes last 2 commits, hard)
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
	echo SUCCESSFULLY FINISHED
	echo ""
}


#Read in Arguments
num=1
hardness="soft"
while getopts ":uhn:H" opt; do
	case $opt in
		h)
			usage
			exit 1
			;;
		u)
			usage
			exit 1
			;;
		n)
			arg=$OPTARG
			if [[ ! "$arg" =~ [0-9]+ ]]; then
				error "argument after -n must be a number"
				exit 1
			fi
			num="$arg"
			;;
		H)
			hardness="hard"
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


call "git reset --$hardness HEAD~$num"
finish
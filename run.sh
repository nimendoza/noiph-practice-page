#!/bin/bash

set -e

path=$1

if [ -z "$path" ]; then
    echo "Usage: $0 <path> <command>"
    echo "     <path> is the path to the problem directory"
    echo "     <command> is the command to run the program"
    echo "         (optional, defaults to './output.exe')"
    exit 1
fi

if [ ! -d "$path" ]; then
    echo "Error: $path is not a directory"
    exit 1
fi

g++ "$path/solution.cpp" -o "$path/output.exe"

command=$2

if [ -z "$command" ]; then
    eval "./$path/output.exe"
elif [ "$command" == "debug" ]; then
    eval "gdb ./$path/output.exe"
elif [ "$command" == "in-out" ]; then
    eval "./$path/output.exe < $path/input.txt > $path/output.txt"
elif [ "$command" == "out" ]; then
    eval "./$path/output.exe > $path/output.txt"
else
    echo "Error: unknown command '$command'"
fi

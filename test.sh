#!/bin/bash

choice=$1
argument1=$2
argument2=$3
argument3=$4
argument4=$5
if [ "$choice" == "print" ]
then
	python crud.py print > file.txt
elif [ "$choice" == "create" ]
then
	python crud.py create $argument1 $argument2 > file.txt 
elif [ "$choice" == "update" ]
then
	python crud.py update $argument1 $argument2 $argument3 > file.txt
elif [ "$choice" == "delete" ]
then
	python crud.py delete $argument1 > file.txt
fi


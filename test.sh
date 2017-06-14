#!/bin/bash

choice=$1
argument1=$2
argument2=$3
argument3=$4
argument4=$5
argument5=$6
argument6=$7
argument7=$8
argument8=$9

if [ "$choice" == "printip" ]
then
	python crud.py printip > file.txt

elif [ "$choice" == "createip" ]
then
	python crud.py createip $argument1 $argument2 > file.txt 

elif [ "$choice" == "updateip" ]
then
	python crud.py updateip $argument1 $argument2 $argument3 > file.txt

elif [ "$choice" == "deleteip" ]
then
	python crud.py deleteip $argument1 > file.txt

elif [ "$choice" == "createvlan" ]
then
        python crud.py createvlan $argument1 $argument2 $argument3 $argument4 $argument5 > file.txt

elif [ "$choice" == "readvlan" ]
then
        python crud.py readvlan  > file.txt
elif [ "$choice" == "updatevlan" ]
then
        python crud.py updatevlan $argument1 $argument2 $argument3 $argument4 > file.txt

elif [ "$choice" == "deletevlan" ]
then
        python crud.py deletevlan $argument1 $argument2 > file.txt

elif [ "$choice" == "printrule" ]
then
	python crud.py printrule > file.txt

elif [ "$choice" == "createrule" ]
then
	python crud.py createrule $argument1 $argument2 $argument3 $argument4 $argument5 $argument6 $argument7 > file.txt

elif [ "$choice" == "updaterule" ]
then
 	python crud.py updaterule $argument1 $argument2 $argument3 $argument4 $argument5 $argument6 $argument7 $argument8 > file.txt

elif [ "$choice" == "deleterule" ]
then
        python crud.py deleterule $argument1 > file.txt

elif [ "$choice" == "printuser" ]
then
	python crud.py printuser > file.txt

elif [ "$choice" == "createuser" ]
then
	python crud.py create $argument1 $argument2 $argument3 > file.txt 

elif [ "$choice" == "updateuser" ]
then
	python crud.py updateuser $argument1 $argument2 $argument3 $argument4 > file.txt

elif [ "$choice" == "deleteuser" ]
then
	python crud.py deleteuser $argument1 > file.txt

elif [ "$choice" == "printroute" ]
then
	python crud.py printroute > file.txt

elif [ "$choice" == "createroute" ]
then
	python crud.py createroute $argument1 $argument2 $argument3 > file.txt

elif [ "$choice" == "updateroute" ]
then 
        python crud.py updateroute $argument1 $argument2 $argument3 $argument4 > file.txt

elif [ "$choice" == "deleteroute" ]
then 
        python crud.py deleteroute $argument1 > file.txt
fi


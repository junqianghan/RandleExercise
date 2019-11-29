#!/bin/bash

for_func(){
	for i in A B C D; do
		echo $i
	done
}

for_func_1(){
	for i in {A..Z}; do
		echo $i
	done
}

for_func_2(){
	for i in *.sh; do
		echo $i
	done
}

for_func_3(){
	txt="hello world randle han"
	for word in $txt;do
		echo $word
	done
}

for_func_4(){
	for (( i=0;i<5;i++ ));do
		echo $i
	done
}
#for_func
#for_func_1
# for_func_2
# for_func_3
for_func_4

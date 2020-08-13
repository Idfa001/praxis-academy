#!/bin/bash
#Str="Ada file .java pada "
#find ../ -name '*.java'

function cari(){

search=$(find ../ -name '*.java')
str="Ada file java pada $search"
echo $str
}

val=$(cari)
echo "$val"

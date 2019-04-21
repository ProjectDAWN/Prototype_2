#!/bin/bash

#  bash
#  manager.sh
#  SOFTWARE_PROTO2
#  V1.0
#  DAWN
#
###############################################################################
#
#                       DATA MANAGER
#
###############################################################################


d0=`find . -name "20*" |\
cut -d '/' -f 2 |\
cut -c-10 |\
sort -u |\
tail -n 1`
if [ -z "$d0" ]
then
  num=3
else
  l0=`tail -n 1 $d0.csv`
  num=$(grep -n $l0 $1 | cut -d: -f1 | tail -1)
  let "num=num+1"
fi

tail -n +$num $1 | \
while read line
do
  date=`echo $line | cut -d',' -f 1 `
  echo $line  >> $date.csv
done

#!/bin/bash

echo "Welcome to SimpleNews"
#script_dir=`dirname $0`
#cd $script_dir
source ENV/bin/activate
python SimpleNews.py; exec /bin/bash -i

#!/bin/sh

OLD_PWD=$(pwd)

cd $BEEHIVE_HOME/dataserver

if [ ! -e venv ]
then 
  pyvenv venv 
fi

export FLASK_APP=data_server.py
venv/bin/flask run

cd $OLD_PWD


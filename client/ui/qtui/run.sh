#!/bin/bash

pyuic5 -x -o out/login.py login.ui
pyuic5 -x -o out/register.py register.ui
pyuic5 -x -o out/new_room.py new_room.ui
pyuic5 -x -o out/room_list.py room_list.ui
pyuic5 -x -o out/room.py room.ui
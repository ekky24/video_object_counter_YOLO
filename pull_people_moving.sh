#!/bin/bash
git fetch
git pull
git checkout origin/master -- people_moving.py
git checkout origin/master -- config_people_moving.py
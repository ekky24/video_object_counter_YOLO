#!/bin/bash
git fetch
git pull
git checkout origin/master -- visitor_counter.py
git checkout origin/master -- config_visitor_counter.py
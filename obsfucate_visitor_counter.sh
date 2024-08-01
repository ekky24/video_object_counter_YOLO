#!/bin/bash
pyarmor gen config_visitor_counter.py
pyarmor gen visitor_counter.py
rm -f config_visitor_counter.py
rm -f visitor_counter.py
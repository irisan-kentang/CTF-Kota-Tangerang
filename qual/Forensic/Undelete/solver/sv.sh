#!/bin/bash
fls disk.img
icat disk.img 4 > flag.zip
icat disk.img 6 > password.txt
7z x -so -p$(cat password.txt) flag.zip

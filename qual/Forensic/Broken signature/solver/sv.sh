#!/bin/bash
sed -i 's/CTF/PNG/g' flag.png
exiftool -Comment flag.png

#!/bin/bash
git reflog | grep Add | awk '{print $1}' | xargs -Iz bash -c 'git diff z | tail -1' | tr -d '-' | paste -sd '' | rev

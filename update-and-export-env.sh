#!/bin/bash -l

mamba env update -n learnpy -f environment.yml
mamba env export -n learnpy -f environment.lock.yml

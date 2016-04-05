#!/bin/sh
set -x
sudo mount --bind $1 $1 
sudo mount --make-shared $1
#sudo fusermount -uz $1 

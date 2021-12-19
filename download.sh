#!/bin/bash

echo -n url:
read str

rm -rf test
oj d $str
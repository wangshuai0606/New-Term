#!/bin/bash
file="test.txt"
echo "hello" > $file
echo "world" >> $file
echo "Lines: $(wc -l < $file)"

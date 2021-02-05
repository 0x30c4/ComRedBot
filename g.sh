#!/bin/bash

for i in $(seq 100); do
    echo >> README.md;git add README.md;git commit -m ".";git push;
    done

#!/bin/bash


dataset_dir="$1"
output_file="$2"

/static/package_unpack.sh "$dataset_dir"

python /static/main.py --dataset_dir "$dataset_dir" --output_file "$output_file"

#!/bin/bash

unpack_recursive(){
        local dir="$1"
        for file in "$dir"/*; do
                if [[ -d "$file" ]]; then
                        unpack_recursive "$file"
                elif [[ "$file" =~ \.zip$ ]]; then
                        unzip "$file" -d "${file%.*}" && rm "$file"
                        unpack_recursive "${file%.*}"
                elif [[ "$file" =~ \.tar\.gz$ || "$file" =~ \.tgz$ ]]; then
                        mkdir "${file%.*}" && tar -xzf "$file" -C "${file%.*}" && rm "$file"
                        unpack_recursive "${file%.*}"
                elif [[ "$file" =~ \.tar$ ]]; then
                        mkdir "${file%.*}" && tar -xf "$file" -C "${file%.*}" && rm "$file"
                        unpack_recursive "${file%.*}"
                elif [[ "$file" =~ \.gem$ ]]; then
                        gem unpack "$file" --target="${file%.*}" && rm "$file"
                        unpack_recursive "${file%.*}"
                fi
        done
}

unpack_recursive "$1"

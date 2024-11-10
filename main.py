import os
import argparse
import pandas as pd
from dataset_processor import process_package
from parser_utils import pattern_matches


def main(dataset_directory, output_file):
    for package_name in os.listdir(dataset_directory):
        package_path = os.path.join(dataset_directory, package_name)
        if os.path.isdir(package_path):
            print("Processing package: ", package_name)
            process_package(package_path, package_name)

    df = pd.DataFrame(pattern_matches)
    df.to_csv(output_file, index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset_dir", type=str, required=True)
    parser.add_argument("--output_file", type=str, required=True)
    args = parser.parse_args()
    main(args.dataset_dir, args.output_file)
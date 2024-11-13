import os
import argparse
import csv
from utils.dataset_processor import process_package
from utils.parser_utils import pattern_matches  # pattern_matches 가져오기

def main(dataset_directory, output_file):
    fieldnames = ["package_name", "file_name", "type", "full_name", "function_name", "call_expression"]
    
    # CSV 파일 열기 (append 모드 처럼 작동 )
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csv_writer.writeheader()  # 헤더 작성

        # 한번 CSV 파일 열어놓고 패키지 하나씩 결과 기록
        for package_name in os.listdir(dataset_directory):
            package_path = os.path.join(dataset_directory, package_name)
            if os.path.isdir(package_path):
                print("Processing package: ", package_name)
                process_package(package_path, package_name)
                
                # 현재 패키지의 pattern_matches를 CSV 파일에 기록
                for match in pattern_matches:
                    csv_writer.writerow(match)
                
                # pattern_matches 리스트 비우기 >> 리스트 버퍼 많이 차는거 방지
                pattern_matches.clear()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset_dir", type=str, required=True)
    parser.add_argument("--output_file", type=str, required=True)
    args = parser.parse_args()
    main(args.dataset_dir, args.output_file)

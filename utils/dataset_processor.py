import os
from tree_sitter import Parser
from utils.config import LANGUAGES
from utils.parser_utils import ASTNode_pattern_match  # pattern_matches는 가져오지 않음


# 패키지 내의 모든 소스코드 파일 처리
def process_package(package_path, package_name):
    for root, _, files in os.walk(package_path):
        for file in files:
            file_extension = os.path.splitext(file)[-1].strip(".")
            if file_extension in LANGUAGES:
                file_path = os.path.join(root, file)
                if not os.path.isfile(file_path):
                    print("Not a file: ", file_path)
                    continue
                process_file(file_path, package_name, file, file_extension)
            else:
                print("unsupported extension: ",file_extension)

def process_file(file_path, package_name, file_name, language_extension):
    language_key = LANGUAGES[language_extension]
    parser = Parser(language_key)

    try:
        with open(file_path, "rb") as f:
            source_code = f.read()
        print("Source Code: ", file_path)

        tree = parser.parse(source_code)
        root_node = tree.root_node

        ASTNode_pattern_match(root_node, source_code, language_extension, package_name, file_name)
    except Exception as e:
        print(f"Processing Error : {file_path}: {e}")
        pass

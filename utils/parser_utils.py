from utils.patterns import get_patterns
pattern_matches = []

def ASTNode_pattern_match(node, source_code, language_extension, package_name, file_name):
    extract_type = {'identifier', 'constant', 'function', 'class', 'method', 'module', 'alias', 'call', 'string'} # 추출할 노드 타입 (실제 사용하는건 call, idenifier, constant) 
    node_name = None
    patterns = get_patterns(language_extension)

    if node.type in extract_type:
        try:
            node_name = source_code[node.start_byte:node.end_byte].decode("utf-8", errors='ignore').strip() # 노드 이름 추출
        except UnicodeDecodeError:
            node_name = ''

    # call 노드일 경우
    if node.type == 'call': 
        func_name_parts = []
        matched_type = None
        function_name = None

        for child in node.children:
            if child.type == 'call':
                ASTNode_pattern_match(child, source_code, language_extension, package_name, file_name)
                continue
            if child.type in {'constant', 'identifier'}:
                try:
                    part_name = source_code[child.start_byte:child.end_byte].decode("utf-8", errors='ignore').strip()
                except UnicodeDecodeError:
                    part_name = ''
                func_name_parts.append(part_name)
                
                # 정규표현식으로 패턴 매칭하는 방식으로 수정
                if matched_type is None:
                    full_name = ".".join(func_name_parts)
                    for pattern_type, pattern_list in patterns.items():
                        for pattern in pattern_list:
                            if pattern.search(full_name):  # 정규표현식 패턴 매칭
                                matched_type = pattern_type
                                break
                        if matched_type:
                            break

            if child.type == 'identifier': # 마지막 identifier를 함수 이름으로 설정
                function_name = part_name

        if matched_type:
            full_function_name = ".".join(func_name_parts)
            try:
                call_expression = source_code[node.start_byte:node.end_byte].decode("utf-8", errors='ignore').strip()
            except UnicodeDecodeError:
                call_expression = ''
            pattern_matches.append({
                "package_name": package_name,
                "file_name": file_name,
                "type": matched_type,
                "full_name": full_function_name,
                "function_name": function_name,
                "call_expression": call_expression
            })

    # 하위 노드들에 대해 재귀 호출
    for child in node.children:
        ASTNode_pattern_match(child, source_code, language_extension, package_name, file_name)

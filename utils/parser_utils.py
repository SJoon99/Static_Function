from utils.patterns import get_patterns
pattern_matches = []

def ASTNode_pattern_match(node, source_code, language_extension, package_name, file_name, func_name_parts=None):
    extract_type = {'identifier', 'constant', 'function', 'class', 'method', 'module', 'alias', 'call', 'string'}
    node_name = None
    patterns = get_patterns(language_extension)

    if func_name_parts is None:
        func_name_parts = []

    if node.type in extract_type:
        try:
            node_name = source_code[node.start_byte:node.end_byte].decode("utf-8", errors='ignore').strip()
        except UnicodeDecodeError:
            node_name = ''

    if node.type == 'call':
        local_func_name_parts = func_name_parts.copy()
        matched_type = None
        function_name = None

        for child in node.children:
            if child.type == 'call':
                # 현재의 func_name_parts를 전달하여 재귀 호출
                ASTNode_pattern_match(child, source_code, language_extension, package_name, file_name, local_func_name_parts)
                continue
            if child.type in {'constant', 'identifier'}:
                try:
                    part_name = source_code[child.start_byte:child.end_byte].decode("utf-8", errors='ignore').strip()
                except UnicodeDecodeError:
                    part_name = ''
                local_func_name_parts.append(part_name)
                if matched_type is None:
                    full_name = ".".join(local_func_name_parts)
                    for pattern_type, pattern_list in patterns.items():
                        for pattern in pattern_list:
                            if pattern.search(full_name): # 정규표현식 패턴 매칭
                                matched_type = pattern_type
                                break
                        if matched_type:
                            break
            if child.type == 'identifier':
                function_name = part_name

        if matched_type:
            full_function_name = ".".join(local_func_name_parts)
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
        ASTNode_pattern_match(child, source_code, language_extension, package_name, file_name, func_name_parts.copy())

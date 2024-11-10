from patterns import get_patterns
pattern_matches = []

def ASTNode_pattern_match(node, source_code, language_extension, package_name, file_name):
    extract_type =  {'identifier', 'constant', 'function', 'class', 'method', 'module', 'alias', 'call','string'} # 추출할 노드 타입 ( 사실 사용하는건 identifier, constant, call )
    node_name = None
    patterns = get_patterns(language_extension) # 언어별 패턴 불러오기

    if node.type in extract_type:
        node_name = source_code[node.start_byte:node.end_byte].decode("utf-8").strip() # 노드 이름 추출 (공백 제거)

    if node.type == 'call':
        # 데이터셋 컬럼값들 저장할 변수들 정의
        func_name_parts = []
        matched_type = None
        function_name = None

        for child in node.children: # 한 계층의 자식 노드
            if child.type == 'call': # call 노드가 있으면 재귀호출 -> call 노드 안에 call 노드가 있을 경우 대비
                ASTNode_pattern_match(child, source_code, language_extension, package_name, file_name)
                continue
            if child.type in {'constant', 'identifier'}:
                part_name = source_code[child.start_byte:child.end_byte].decode("utf-8").strip() # 마지막 identifier 노드를 찾아서 함수명으로 저장
                func_name_parts.append(part_name)
                if matched_type is None: # 아직 매칭된 타입이 없다면
                    for pattern_type, pattern_list in patterns.items():
                        if part_name in pattern_list: # 패턴 비교
                            matched_type = pattern_type
                            break # 패턴 매칭되면 루프 탈출
                        # 현재 정확한 문자열 비교 방식으로 구현되어 있어서, 패턴이 포함되어 있을 경우에도 매칭이 안됨 
                        # 대소문자 구분없이 패턴이 포함되어 있는지 비교하는 방식으로 수정한다면 적은 패턴으로도 많은 패턴 매칭 함수 결과를 반영할 수 있을 것
                        # 하지만 계산량 증가로 인한 성능 저하 있을 수 있음
                        # for pattern_type, pattern_list in patterns.items():
                        #     for pattern in pattern_list:
                        #         # 대소문자 무시하고 포함 관계로 비교
                        #         if pattern.lower() in part_name.lower(): # 문자열 자체를 비교 -> 패턴 비교
                        #             matched_type = pattern_type
                        #             break  # 패턴 매칭되면 루프 탈출
                        #     if matched_type:
                        #         break  # 첫 번째 for문도 탈출
            if child.type == 'identifier': # 마지막 identifier 노드를 찾아서 함수명으로 저장
                function_name = part_name

        if matched_type:
            full_function_name = ".".join(func_name_parts)
            call_expression = source_code[node.start_byte:node.end_byte].decode("utf-8").strip()
            pattern_matches.append({
                "package_name": package_name,
                "file_name": file_name,
                "type": matched_type,
                "full_name": full_function_name,
                "function_name": function_name,
                "call_expression": call_expression
            })

    for child in node.children:
        ASTNode_pattern_match(child, source_code, language_extension, package_name, file_name)


                


        


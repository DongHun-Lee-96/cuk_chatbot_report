
# 질문과 데이터 셋의 질문의 레벤슈타인 거리 구하는 함수
# 출력으로 두 문장의 거리의 값이 담긴 리스트 리턴
def calculate_lev_distance(input_sentence, questions_set):
    similarities = []
    
    for question in questions_set:
        if input_sentence == question: 
            similarities.append(0) # 같으면 0으로 유사도 지정
        else:
            input_sentence_len = len(input_sentence) # 사용자 입력 질문 길이
            question_len = len(question) # 질문 셋의 길이

            matrix = [[] for i in range(input_sentence_len+1)] # 리스트 컴프리헨션을 사용하여 1차원 초기화
            for i in range(input_sentence_len+1): # 0으로 초기화
                matrix[i] = [0 for j in range(question_len+1)]  # 리스트 컴프리헨션을 사용하여 2차원 초기화
            
            # 0일 때 초깃값을 설정
            for i in range(input_sentence_len+1):
                matrix[i][0] = i
            for j in range(question_len+1):
                matrix[0][j] = j

            # 문장의 한 글자씩 비교
            for i in range(1, input_sentence_len+1):
                input_sentence_letter = input_sentence[i-1]
                for j in range(1, question_len+1):
                    possible_answer_letter = question[j-1] 
                    cost = 0 if (input_sentence_letter == possible_answer_letter) else 1

                    matrix[i][j] = min([
                        matrix[i-1][j] + 1,     # 문자 제거는 위쪽에서 +1
                        matrix[i][j-1] + 1,     # 문자 삽입은 왼쪽 수에서 +1   
                        matrix[i-1][j-1] + cost # 문자 변경은 대각선에서 +1 동일하면 대각선 숫자 복사
                    ])
            # 유사도를 리스트에 저장
            similarities.append(matrix[input_sentence_len][question_len])

    return similarities

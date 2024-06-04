import pandas as pd

from levenshtein_distance import calculate_lev_distance

class ChatBot:
    # 챗봇 객체를 초기화, 질문과 답변 데이터 셋을 로드
    def __init__(self, filepath):
        self.questions, self.answers = self.load_data(filepath)

    # CSV 파일로부터 질문과 답변 데이터를 불러오는 함수
    def load_data(self, filepath):
        data = pd.read_csv(filepath)
        questions = data['Q'].tolist()
        answers = data['A'].tolist()
        return questions, answers

    # 입력 문장에 가장 잘 맞는 답변을 찾는 함수로서, 입력 질문에 대한 레벤슈타인 거리를 모든 질문과 비교
    # 비슷한 문장일 수록 거리의 값이 작으므로 가장 작은 거리에 대한 답변을 리턴
    def find_best_answer(self, input_sentence):
        similarities = calculate_lev_distance(input_sentence, self.questions)
        # 가장 적합한 답의 인덱스
        best_match_index = similarities.index(min(similarities))
        
        # 가장 유사한 질문에 해당하는 답변을 리턴
        return self.answers[best_match_index]

# 데이터 파일의 경로를 지정, 현재 경로의 ChatbotData.csv를 찾음
filepath = './ChatbotData.csv'

# 챗봇 객체 생성
chatbot = ChatBot(filepath)

# '종료'라는 입력이 나올 때까지 사용자의 입력에 따라 챗봇의 응답을 출력하는 무한 루프를 실행
# 입력 없이 빈 문자열이 들어오면 질문을 입력하라는 메시지 출력
while True:
    input_sentence = input('USER: ')
    if input_sentence.lower() == '종료':
        break
    elif input_sentence.replace(" ", "") == "":
        response = "질문을 입력하세요"
        print("Chatbot: ", response)
    else:
        response = chatbot.find_best_answer(input_sentence)
        print('Chatbot:', response)

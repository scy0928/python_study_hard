import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
# todo - 1 : 남은 목숨 수를 추적하기 위한 'lives'라는 변수를 선언하고, 6으로 초기화하세요.
lives = 6
display = []
word_list = ["apple", "banana", "camel"]
chosen_word = random.choice(word_list)
print(f"테스트 코드 = (chosen_word)")

for letter in chosen_word:
    display. append("_")

while not end_of_game:
    guess = input("알파벳 입력하세요>>>").lower()

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
        # else:
        #     lives -= 1
        #     print(f"당신의 기회는 {lives}만 님았습니다. ")
        #     if lives == 0:
        #         print(f"모든 기회를 잃었습니다")
        #         end_of_game = True
        #라고 작성하시면 안됩니다 -> 알파벳을 하나 입력할 떄마다 모든 단어에서 알파벳이 맞는지
        #확인하는 조건문이 선행되기 떄문
        #-> 즉, 반복문 내부에 조건문이 있기 때문에 guess는 한 번만 입력하고도
        #lives가 여러분 -= 1이 이루어집니다.

    # todo - 2 : 추측한 알파벳이 chosen_word에 없으면 lives를 1 감소시키세요.
    #  lives가 0이 되면 "모든 기회를 잃었습니다."를 출력하고 게임을 끝내세요.

    #이상을 이우로 for반복문을 바깥에서 (즉 들여쓰기 적용 안함) guess 가 chosen_word 에 속하지
    #많은지를 확인하는 조건문을 작성해야 함

    if guess not in chosen_word:
        lives -= 1
        print(f"당신의 기회는 {lives}만 님았습니다. ")
        if lives == 0:
            print(f"모든 기회를 잃었습니다")
            end_of_game = True
            print(f"정답은 {chosen_word}입니다.")
        # 더 맞췄을 때는 어떻게 판별하고 어떻게 반복문을 종료시킬 것인가
    # todo - 4 : 사용자가 모든 문자를 맞췄는지 확인하세요 -> 정답을 맞췄다면 "정답입니다!!:)"를 출력하세요
    if "_" not in display:
        print("정답입니다!!")
        end_of_game = True

    #  print(display)
    # todo - 3 : display list의 모든 요소를 결합하여 문자열로 변환하세요,

     print(" ".join(display))
     print(stages[lives])

    # 여기까지 작성했을 떄 비어있는 점
    # 1. 로고
    # 2. word_list 부족하다
    # 3. 혹시 테스트해보고 유지 보수 및 리팩토링 지정이 있는지 확인할 필요가 있다. -> 함수화





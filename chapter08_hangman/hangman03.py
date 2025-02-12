import random     #특정 모듈을 사용한다는 것을 맨 처음레 명시합니다.

'''
"".join(반복가능객체) method :  . 앞에 있는 문자열을 기준으로 반복가능객체의 요소들을 
합쳐서 str으로 변환함
'''
temp = ["안","녕","하","세","요"]
hello = "".join(temp)
print(hello)
print("/".join(temp))
print(" ".join(temp))

words_list = ["apple","banana","camel"]
chosen_word = random.choice(words_list)

display = []
#todo - 1 : "_"기 적용된 display 구현하세요

for letter in chosen_word:
    display. append("_")


#todo - 2 : 사용자가 추측을 반복할 수 있도옥 while반복문을 작성하세요
# 사용자가 chosen_word의 모든 문자열을 마주쳤을 때
# 즉, display에 더 이상 "_"가 없을 때 반복문이 멈추도록 작성합니다.
# 반복문 종료 후 print("정답입니다!")를 출력하도록 작성하십시오.

while "_" in display :
    guess = input("알파벳 입력하세요>>>").lower()

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
        print(display)

print(" ".join(display))
print("정답입니다!!")
food = float(input("음식의 가격은 얼마입니까? >>> $"))
percent = float(input("몇 퍼센트(%)의 팁을 내실 예정입니까? 10, 12, 15%중에서 선택하세요. >>> "))
people = int(input("몇 명의 인원이 나누어 내나요? >>> "))

percent = percent / 100
result = ((food * percent) + food) / people
result = round(result, 1)

print(f"당신이 내야할 전체 음식의 금액은 ${result}달러 입니다.")
print(f"당신이 내야할 전체 음식의 금액은 ${((food * (1+percent)) / people):.2f}달러 입니다.")
# 10번 라인의 경우는 round() 함수와 달리 어떤 상황에서도 소수점 둘째자리까지 표기되도록 강제하는 코드
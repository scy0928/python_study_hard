'''
round() -> 반올림
'''

height = float(input("당신의 키는 몇 cm입니까? >>> "))
weight = float(input("당신의 몸무게는 몇 kg입니까? >>> "))
m_height = height/100
bmi = weight / (m_height**2)
bmi_int = int(bmi)
bmi_round = round(bmi,2)
print(f"당신의 bmi 지수는 {bmi_round}입니다.")
print(f"당신의 bmi지수는 {bmi_int}입니다")

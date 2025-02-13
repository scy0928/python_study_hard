logo = '''

  o                                                         
 <|>                                                        
 / >                                                        
 \o__ __o       o__ __o      o__ __o    \o__ __o__ __o      
  |     v\     /v     v\    /v     v\    |     |     |>     
 / \     <\   />       <\  />       <\  / \   / \   / \     
 \o/      /   \         /  \         /  \o/   \o/   \o/     
  |      o     o       o    o       o    |     |     |      
 / \  __/>     <\__ __/>    <\__ __/>   / \   / \   / \     


'''

print(logo)
height = float(input("당신의 키는 몇 cm입니까? >>> ")) / 100
weight = float(input("당신의 몸무게는 몇 kg입니까? >>> "))
print(f"당신의 bmi지수는 {round(weight/(height**2), 2)}입니다.") # 반복적으로 나오게 되는 연산의 경우에는 간단한 변수명에 대입하는 것이
                                                               # 가독성 높은 코드를 작성하는 방식에 해당함.
bmi = round(weight/(height**2), 2)

'''
업그레이드 관련 지시 사항 

1. 크롬에서 사이트를 확인하신 후 bmi가 특정 구간일 때마다
당신의 bmi지수는 ㅇㅇ 이고 저체중/정상/과체중/비만입니다. 가 출력될 수 있도록
조건문을 작성하여 반영하시오.
'''

if bmi < 18.5 :
    print(f"당신의 bmi지수는 {bmi}이고 저체중입니다. ")
elif bmi < 23 :
    print(f"당신의 bmi지수는 {bmi}이고 정상입니다.")
elif bmi < 25 :
    print(f"당신의 bmi지수는 {bmi}이고 과체중입니다.")
else:
    print(f"당신의 bmi지수는 {bmi}이고 비만입니다.")
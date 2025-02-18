MENU = {
    "에스프레소": {
        "재료": {
            "물": 50,
            "커피": 18,
        },
        "가격": 1.5,
    },
    "라떼": {
        "재료": {
            "물": 200,
            "우유": 150,
            "커피": 24,
        },
        "가격": 2.5,
    },
    "카푸치노": {
        "재료": {
            "물": 250,
            "우유": 100,
            "커피": 24,
        },
        "가격": 3.0,
    }
}

profit = 0
resources = {
    "물": 300,
    "우유": 200,
    "커피": 100,
}
logo = '''
       _..._                                           
    .-'_..._''.                                        
  .' .'      '.\                        __.....__      
 / .'                         _.._  .-''         '.    
. '                         .' .._|/     .-''"'-.  `.  
| |                 __      | '   /     /________\   \ 
| |              .:--.'.  __| |__ |                  | 
. '             / |   \ ||__   __|\    .-------------' 
 \ '.          .`" __ | |   | |    \    '-.____...---. 
  '. `._____.-'/ .'.''| |   | |     `.             .'  
    `-.______ / / /   | |_  | |       `''-...... -'    
             `  \ \._,\ '/  | |                        
                 `--'  `"   |_|                        '''

def is_resources_enough(order_ingredients):
    for item in order_ingredients:
       if order_ingredients[item] > resources[item]:
           print(f"죄송합니다. {item}이(가) 부족합니다.")
           return False
       return True

def process_coins():
    total = 0.0
    total += int(input("쿼터 동전을 몇 개 넣으시겠습니까? >>> "))* 0.25
    total += int(input("다임 동전을 몇 개 넣으시겠습니까? >>> "))* 0.1
    total += int(input("니켈 동전을 몇 개 넣으시겠습니까? >>> "))* 0.05
    total += int(input("패니 동전을 몇 개 넣으시겠습니까? >>> "))* 0.01

    return total

#들어온 동전 금액과 가격을 비교하는 함수를 정의
def is_transaction_successful(money_received, drink_cost):
    charge = money_received - drink_cost
    if charge >= 0:
        global profit
        profit += drink_cost
        print(f"잔돈 ${charge}을 반환합니다.")
        return True

    else:
        print(f"동전이 충분하지 않습니다. 금액 ${money_received}을 반환합니다")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"{choice}☕가 나왔습니다. 맛있게 드세요.")

is_on = True
print(logo)
while is_on:
    choice = input("어떤 음료를 드시겠습니까? 에스프레소/라떼/카푸치노 >>>")
    if choice == "off":
        is_on = False
        print("자판기가 종료되었습니다.")
    elif choice == "report":
        print(f"물: {resources['물' ]}ml")
        print(f"우유: {resources[' 우유 ']}ml")
        print(f"커피: {resources[' 커피']}ml")
        print(f"물: ${profit}")
    elif choice in ["에스프레소", "라떼", "카푸치노"] :
        print("정상작동합니다.")
        drink = MENU[choice]
        if is_resources_enough(drink["재료"]) and is_transaction_successful(process_coins(),drink["가격"] ):
            make_coffee(choice, drink["재료"])
    else :
        print(f"잘못 입력하셨습니다. 다시 입력하세요.")


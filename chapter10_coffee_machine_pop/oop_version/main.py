from chapter10_coffee_machine_pop.pop_version2.main import choice
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#외부 파일에서 import해온 class의 생성 방법
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

#반복
is_on = True
while is_on:
  choice = input(f"어떤 음료를 드시겠습니까?  {menu.get_items()} >>>").lower()
  # todo -1 : choice가 -> off / report / 오타났을 때 작성하는 부분을 생성하시오
  if choice == "off":
      is_on = False
      print("자판기가 종료되었습니다.")
  elif choice == "report":
      coffee_maker.report()
      money_machine.report()
  #그 다음부터는 종료 이름을 정직하게 적었을 때, 혹은 오타났을 때에 해당합니다,
  else:
      drink = menu.find_drink(choice) #음료 객체를 변수명 drink에 저장
      if drink == None : # choice에 오타가 있을 경우 None이 반환되기 때문에 저장
          continue       # continue가 실행되면 이 밑의 코드라인은 실행되지 않고
                         # while반복문의 맨 앞으로 들어감
      # 여기서 부터 오타가 없이 메뉴이름을 정확하게 작성했을 때의 로직
      # 재료가 충분한지 확인 -> 돈 받는다 -> 받은 돈이 음료 가격보다 높으면 -> 커피 만든다.
      # import 받은 애들은 하나도 수정 안하고 여기 부분만 작성해서 동일한 자판기 프로그램을
      # 완성하십시오.
      if coffee_maker.is_resource_sufficient(drink):
  # coffee_maker.is_resources_sufficient()메서드를 확인해보면
  #drink.ingredient를 반복문 돌린다는 것을 확인할 수 있습니다.
  # 이제 여러분들이 주의해서 봐야할 점은 미리 작성된 메서드가 어껀 자료형의 argument를
  #요구하고 있는지입니다.
  # 즉, pop version 에서처럼 동일하게 생각해서 drink.ingredients를 argument로 넣었다면
  # 오류가 발생했을 겁니다. -> 미리 저장된 코드 부분을 확인해야겠죠. 그리고 return 타입도.
        if money_machine.make_payment(drink.cost):
          # 이상의 조건식을 통과했다면 돈을 더 많이 낸 것이므로 커피 만들면 되겠네요.
          coffee_maker.make_coffee(drink)








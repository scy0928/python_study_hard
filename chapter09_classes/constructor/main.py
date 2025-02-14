'''
생성자(constructor)
'''
from chapter09_classes.main import name2

#클래스 정의
# class Candy:
#     def set_info(self, shape, color):
#         self.shape = shape
#         self.color = color
#
#     def display_info(self):
#         print(f"사탕의 모양은{self.shape}이고, 색깔은 {self.color}입니다")
#
# #객체 생성
# satang = Candy()
# satang.set_info("구형", "갈색")
# satang.display_info()
'''

   satang이라는 인스턴스는 생성된 '이후'에 set_info()매서드를 호출하여 "구형" 모양의
   "갈색" 이라는 속성으로 갖게 됩니다.
   
   사탕 인스턴스의 생성 과정
        1. 값이 없는(속성에 값이 대입되어 있지 않은) 인스턴스를 생성
        2. 값을 저장할 수 있는 메서드 호출
        
   그렇다면 처음부터 값이 있는 인스턴스를 생성하면 코드라인이 줄어들지 않을까.
   이에 대한 해답니 생ㅅ ㅓㅇ자리는 개념이고,
   C/ JAVa 의 경우의 생성자는 클래스명과 동일한데 파이썬만 이상한 방식으로 만듦
   -> __init__()라는 매서드
   
   __init__() 메서드(생성자)는 인스턴스가 생성될 때 '자동으로 호출'되기 때문에 인스턴스 변수의
   '초기화' 용도로 사용, 즉 값이 있는 인스턴스를 생성할 수 있다는 의미 입니다.
   '객체 생성과 동시에' 새성자가 호출됨. -> 초기값은 저장할 떄 사용한다는 의미
   
   형식:
   
class 클래스명
     def __init__(self, shape, color):
           self.shape = shape
           self.color = color
'''
# class Candy2():
#
#     #생성자 정의
#     def __init__(self, shape, color):
#         self.shape = shape
#         self.color = color
#
#     def display_info(self):
#         print(f"사탕의 모양은 {self.shape}이고, 색깔은 {self.color}입니다")
#
# satang2 = Candy2("직육면체", "흰색")  #이부분이 달라짐
# satang2.display_info()

'''
이상에서 주목해야 할 점은 satang 인스턴스와 satang2인스턴스의 생성방식의 차이입니다.

2.소멸자(Destructor)
    인스턴스가 생성될 떄 자동으로 생성되는 생성자와 마찬가지로 인스턴스가 소멸될 때 호출되는 매서드
    이를 소멸자라 하며 소멸자를 정의하는 메서드는 __del__()
'''
# class Sample:
#
#     #생산자 정의
#     def __init__(self):
#         print(f"인스턴스가 생성되었습니다")
#
#     def __del__(self):
#         print(f"인스턴스가 소멸되었습니다")
#
# #객체 생성
# sample = Sample()
#
# del sample   #del 객체만으로 소멸자를 "원하는 시기"에 호출될 수 있음 -> 예를 들어 객체 소멸 시점
#
# #여기 부분에 추가적인 로직을 작성하여 더 프로그램이 진행된 후에 프로그램 전체 종류가 이루어질 수 있음
#
# print("프로그램이 종료되었습니다")
'''
기본 예제

생성자를 이용해서 용량을 가진 usb 인스턴스를 만드는 프로그램을 작성하시오

지시사항
1. 클래스 USB를 정의할 것
2. 생성자를 정의하여 매개변수로 capacity를 받은 것
3. get_info() 메서드로 정의할 것

math 단계 코드
usb = USB(64)
usb.get_info()

실행 예
64GB USB
'''
# #1번 지시사항
# class USB:
#     #2번 지시사항
#     def __init__(self, capacity):
#         self.capacity = capacity
#
#     #3번 지시사항
#     def get_info(self):
#         print(f"{self.capacity}GB USB")
#
# #객체 생성 및 get_info()메서드 호출
# usb = USB(64)
# usb.get_info()

'''
생성자와 소멸자를 이용하여 서비스 안내 메시지를 출력하는 프로그램을 작성하시오

class Service를 정의하고 생산자를 통해 매개변수를 service로 받고 print() 메서드를 생산자와 소멸자 내에 작성하시오

main단계에서의 작성
s = Service("길 안내")
del s

실행 예
길 안내 Service가 시작되었습니다
길 안내 Service가 종료되었습니다
'''

# class Service:
#     def __init__(self, service):
#          self.service = service
#          print(f"{self.service}Service가 시작되었습니다")
#
#     def __del__(self, service):
#         print(f"{self.service}Service가 종료되었습니다")
#
# s = Service("길 안내")
# # del s
# print("프로그램이 종료되는 시점")
# del s

'''
응용 예제

1. 다음 지시 사항을 읽고 이름을 저장하는 Person 클래스를 생성하시오

지시 사항

1. 다음과 같은 방법으로 man과 woman 인스턴스를 생성하시오
man = Person("James")
woman = Person("emily")
2. man과 woman 인스턴스가 생성되면 다음과 같은 메시지를 출력 할수 있도록 생성하십시오
james is born.
emily is born.

3.다음과 같은 방법으로 man 인스턴스를 삭제하시오
del man

4.인스턴스가 삭제되면 다음과 같은 메사지를 출력할 수 있도록 작성하십시오
james is dead.
'''

# class Person:
#     def __init__(self, name):
#         self.name = name
#         print(f"{self.name} is born.")
#
#     def __del__(self):
#         print(f"{self.name is dead}")
#
#     man = Person("James")
#     woman = Person("emily")
#
#     del man
#
#     print("프로그램이 종료되었습니다.")

'''
예제1.
   학생들의 성적을 관리하는 Student 클래스를 작성하시오. 이클래스는
   학생의 이름, 학번, 성적을 인스턴스 변수로 갖습니다.
   
   지시사항
   1)클래스를 정의하고 생성자를 통해 name, student id, grade를 초기화 하십시오
   2)학생의 프로필을 풀력하는 인스턴스 메서드 print_profile()를 작성하십시오 (call1()타입으로 : 매개변수 X, 리턴X)
   3)학생의 성적을 변경할 수 있는 인스턴스 메서드 set_grade()를 작성하십시오
       ->'이부분이 고민할 법한 요소입니다 // set_info()메서드를 검색해보세요 ctrl +shift + f눌러서
   4)세 명의 학생 인스턴스를 작성하고 각 학생의 정보를 출력한 대로
    성적을 변경하고 다시 출력하십시오
    
student1 = student("김형수", 20250001, "A")
student2 = student("이영희", 20250002, "B")
student3 = student("박민지", 20250003, "C")

실행 예

힉생 이름 : 김형수
학번 : 20250001
성적 : A

student2 / student 3도 출력하시오.

이후 student1 성적을 A+ / student2는 A / student2은 B+로 성적을 변경하고

다시 print_profile릉 적용하여 출력하시오.
'''
class Student:

    def __init__(self, name, student_id, grade):
        self.name = name

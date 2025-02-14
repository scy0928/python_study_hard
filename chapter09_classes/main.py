'''
1. 클래스 도입의 필요성
'''
#매개 변수가 6개만 함수를 하나 정의합니다
def student_info(name, depertment, professor, phone, address, grade):
    print(name)
    print(depertment)
    print(professor)
    print(phone)
    print(address)
    print(grade)

name1 = "안근수"
department1 = "영어교육과"
professor1  = "david"
phone1 = "010-2344-5678"
address1 = "부산광역시 연제구"
grade1 = "A"

#함수 호출
student_info(name1, department1, professor1, phone1, address1, grade1)
'''
지금까지 배운 함수와 매개변수, 그리고 argument를 통해 6개의 변수를 처리했습니다. 하지만
만들어야 할 변수의 개수가 많고, 학생 한 명 당 매개변수가 6개라면 학생이 100명일 경ㅇ우 600개의
변수를 처리할 수 있습니다.
'''
student_info(grade="B",
             address= "서울특병시 강남구",
             phone= "010-6576-3093",
             professor= "john",
             depertment= "computer science",
             name="김일"
             )          #keyword argument

#name2, ... grade2라는 변수를 선언하고, 거기에 여러분들의 정보를 입력한 뒤
# keyword argument를 통해서 student_info()함수를 호출하시오.

name2 = "송채영"
department2 = "수리과학과"
professor2  = "sam"
phone2 = "010-6676-0581"
address2 = "부산광역시 동구"
grade2 = "A"

 #keyword argument 를 적용한 함수 호출
student_info(name=name2, depertment=department2, professor=professor2, phone=phone2, address=address2, grade=grade2)

'''
이상의 상황들(변수에 각각 데이터를 대입한 후에 함수의 argument도 사용하거나, 혹은 데이터를 직접 argument에 등록)을
벗어나기 위해 클래스와 객체 개념을 도입합니다.

class란 : 객체를 만드는 도구 - 설계도 / 틀 / 청사진

     자동차 설계도 -> 클래스
     설계도를 통해 생성된 자동차들 -> 객체
     
     같은 설계도로 만든 자동차라 하더라도 서로 다른 옵션을 가질 수 있습니다.
     마찬가지로 같은 클래스로 만든 객체라 하더라도 서로 다른 값을 가질 수 있습니다.
     
     인스턴스(instance) 역시 클래스를 이용해서 생성한 객체를 가리키는 용어입니다.
     객체와 인스턴스는 그 둘을 바라보는 관점의 차이로 볼 수 있습니다.
     
     1. '자동차 설계도'로 만든 자동차는 객체(object) 입니다.
     2. 자동차는 자동차 설계도의 인스턴스(instance)입니다.
     
1. 클래스 정의
    틀래스를 작성하는 것을 클래스 정의라고 합니다. -> 함수 정의를 생각하시면 됩니다.
    
형식:

class클래스명(대문자로 시작)
   본문
   ----------------------
객체 생성 형식:                           -> 함수 호출을 생각하시면 일부 비슷합니다.
객체 이름 = 클래스명()
'''

#  클래스 정의 형식 예시
class WaffleMachine:     #클래스명은 대문자로 시작하고 Pascal Case로 표기함 python에서 변수는 snake_case
    pass                 #나중에 코드를 작성하겠다는 의미로 이 경우 실행시켜도 오류가 나지 않음

#객체 생성 예시
waffle = WaffleMachine()  #소괄호()가 중요합니다. 추후 사용 예정
print(waffle)

'''
print(waffle)을 실행시켰을 때 <__main__.WaffleMachine object at 0x0000019FDB585410>에서 object라고
표기된 점을 미루어 waffle 은 WaffleMachine의 객체명을 확인할 수 있음.

클래스의 구성
 
 1. 클래스의 기본 구성
   객체를 만들어 내는 클래스는 객체가 가져야 할 구성 요소를 지닙니다.
   객체를 생성하기 위해서는 클래스는 객체가 가져야 할 '값' 과 '기능'을 지녀야 합니다.
   
   값= 속성(attribute)
   기능=메서드(method)
   
   클래스를 구성하는 변수는 두 가지로 구분됩니다.
     1)클래스 변수 : 클래스를 기반으로 생성된 모든 인스턴스들이 공유하는 변수
     2) 인스턴스 변수 : 인스턴스 등이 개별적으로 가지는 변수
     
    매서드는 특징에 따라서
        1)클래스 매서드
        2)정적 매서드
        3)인스턴스 매서드
        
    인스턴스 변수 : 클래스를 기반으로 만들어지는 모든 인스턴스들이 각각 따로 저장하는 변수를 의미
      모든 인스턴스 변수는 self라는 키워드를 앞에 붙여준다
    인스턴스 메서드 : 인스턴스 변수를 사용하는 메서드
       인스턴스 변숫값에 따라서 각 인스턴스마다 다르게 동작합니다.
       인스턴스 메서드는 첫 번째 매개 변수로 self를 추가해야 합니다.
   
'''
#클래스 정의
# class Person:
#     #chapter06_function부분 참조하는데 -> call2()
#     def set_info(self, name, age, tel, address):   #클래스 내부에 def를 사용하면 method로 정의함.
#         self.name = name
#         self.age = age
#         self.tel = tel
#         self.address = address   #self는 인스턴스 메서드에 항상 있어야 하는 것으로
#                                  #아직 인스턴스를 생성하지 않았기 때문에 인스턴스 이름이 없습니다.
#                                  #추후에 인스턴스를 생성하게 되면 인스턴스명.name 등으로 시작합니다.
#
#     #call()/매개변수 없음 return 없음
#     def display_info(self):
#         print(f"이름 : {self.name}")
#         print(f"나이 : {self.age}")
#         print(f"연락처 : {self.tel}")
#         print(f"주소 :{self.address}")
#
#     #call3() / 매개 변수 없음 return 있음
#     def display_info2(self):
#         return(f"제 이름은 {self.name}이고, {self.age}살입니다. 연락처는 {self.tel}인데 {self.address}에 살고 있습니다.")
# #객체 생성
# person01 = Person()
# print(person01)    #객체명으로 그대로 출력할 수 없음 ->주소값만 출력
# person01.set_info( "안근수", age 38,  "010-2345-5678" ,  " 서울 특별시 마포구" )
# print(person01.display_info()) #클래스에서  정의한 method 사용 -> 메소드 호출 방식 객체명.메서드명()
#
# #person02 객체를 생성하시고, person02.set_info()를 활용하여 여러분 이름 나이 연락처 주소 들을 입력하고
# #display_info()(call3()유형으로 작성)를 정의하여 다음 실행 예와 같이 출력하도록 작성하세요.
# #실행 예
# #제 이름은 ------이고 -------살입니다
# #연락처는 ------인데, -------에 살고 있습니다.
# #코드 실행
# #print(person02.display_info2())d
# person02 = Person()     #객체 생성 완료
# person02.set_info("송채영",  17, "010-6676-0581",  "부산광역시 동구" )
#
# #method의 정의는 class 내부에서 이루어져야 한다.
# person02.display_info()
# print(person02.display_info2())

'''
응용 예제

다음 지시사항을 알고 책 제목과 저자 정보를 저장할 수 있는 Bokk 클래스를 생성하세요, -> 객체도 생성하고 실행예를 구현하세요.
1. 다음과 같은 방법으로 book1, book2 인스턴스를 생성하세요.

book1 = Book()
book2 = Book()

2. set_info(self, title, author)를 통해 책 제목을 입력하세요.

3. display_info()를 통해 실행 예와 같이 출력되도록 작성하세요.

실행 에
책 제목: 파이썬
책 저자 : 반경대
책 제목: 어린 왕자
책 저자 : 생택쥐페리
'''
class Book:
    def set_info(self, title, author, stock):
        self.title = title
        self.author = author
        self.stock = stock

    def display_info(self):
        print(f"책 제목 : {self.title}")
        print(f"책 저자 : {self.author}")

#여러분은 클래스 내부에 method를 정의하시면 됩니다.

book1 = Book()
book2 = Book()
book1.set_info( "파이썬", "민경태",  3)
book2.set_info(title="생탯 쥐페리", author= "어린왕자", stock=10)
book1.display_info()
book2.display_info()

#특정 개체의 속성값을 확인하는 방법 -> 객체명, 속성명
print(book1.title)
#그러면 특정 속성값만 꺼내는 이유
print(book1.stock + 2)
#어떤 method를 사용해서 속성에 값을 대입하고 어떤 method를 시용하면 정보를 출력할지 코드를 작성하셔야 합니다
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
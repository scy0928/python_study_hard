'''
외부 패키지의 설치

좌측 상단 메뉴 버튼(햄버거) ->file -> settings (ctrl +alt +s)
좌측 리스트에서 project :프로젝트명으로 되어있는 부분 클릭
->python interpreter
->좌상단에 + 눌러서 필요한 패키지 검색 및 설치
'''

from prettytable import PrettyTable
from pokemon_data import pokemon_data

table = PrettyTable()

table.field_names = ["번호", "이름", "타입"]
example1 = (1, "이상해씨", "풀/독")
table.add_row(pokemon_data[0])

print(table)

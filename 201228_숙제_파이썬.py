a = '이유덕,이재영,권종표,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌'.split(
    ',')

print(list(a))

print(type(a))

# <이재영 이란 이름은 몇번 반복되나요?>

print(a.count("이재영"))

# 매개변수 안의 인수를 카운팅하는 카운트 함수 사용...

# <중복을 제거한 이름을 출력>

aa = list(set(a))

# set은 집합
# 순서가 없고, 집합안에서는 unique한 값을 가집니다. (위키피디아뒤짐)
#->중복을 허용하지 않는 set의 속성을 이용해서 중복을 제거한 뒤 리스트로 변경 해쥼

print(aa)

#그런 aa 를 출력

#<중복을 제거한 이름을 오름차순>

aa.sort()

print(aa)

#print(aa.sort())=> none값 출력되는데 와이...

#<김씨와 이씨는 각각 몇명인가유>

a_sum =[]
b_sum =[]

# 김씨와 이씨를 각각 담을 공리스트 만듦

for i in aa:
#리스트 요소들 확인하기 위해 반복문 시작

  if i[0] == "김":
    a_sum.append(i)

#만약 리스트 자료의 첫글자 (= 인덱스 0번) 가 김씨면 에이썸이라는 리스트에 추가

  elif i[0] == "이":
    b_sum.append(i)

#만약 리스트 자료의 첫글자 (= 인덱스 0번) 가 이씨면 비썸이라는 리스트에 추가

print("김씨 {}명".format(len(a_sum)))

#김씨가 든 리스트 에이썸의 개수를 렌함수로 구한뒤 출력

print("이씨 {}명".format(len(b_sum)))

#이씨가 든 리스트 에이썸의 개수를 렌함수로 구한뒤 출력

print(a_sum)
print(b_sum)


#<3개의 각으로 삼각형의 예각 직각 둔각을 구별하는 프로그램 만드세요>

x = int(input("첫 번째 각 입력>"))
y = int(input("두 번째 각 입력>"))
z = int(input("세 번째 각 입력>"))

#인수로 쓰일 요소들을 입력받을 수 있도록 변수선언

def tri_search(x,y,z):

  if x + y + z != 180:
    return print("삼각형이 아님")

# 세 각의 합이 180이 아니면 삼각형이 아님. 나머지들은 뒤에 엘스안에 다시 이프문 넣어서 처리

  else:
    if x == 60 and y == 60 and z == 60:
      return print("예각삼각형")
    elif x == 90 or y == 90 or z == 90:
      return print("직각삼각형")
    else:
      return print("둔각삼각형")


cons_a = tri_search(x,y,z)

print(cons_a)



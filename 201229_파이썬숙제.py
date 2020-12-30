
#문제 1 홀수와 짝수의 개수를 구하는 함수만들기



def func(numlist):
    result = 0
    result2 = 0
#짝 홀의 개수를 각각 개산할 함수 내부 변수 두개 선언
    for i in numlist:
#리스트 내부 요소 다 꺼내서 작업할 반복문 실행
        if i % 2 == 0:
            result = result + 1
#리스트에서 빠져나온 인수를 2로 나눈값이 0, 즉 짝수면 result에 1개 추가
        else:
            result2 = result2 +1
#아님 2에 추가            
    print(list(numlist),"=","홀수 {}개 짝수 {}개".format(result,result2))
#결과 출력    

ab = [1,2,4,5,6,23,4,1,2]

print(func(ab))


#문제 2 1차원의 점들중에서 가장 짧은 구간 구하시오

s = [1,3,4,13,17,20]

def search(aa):
  a = 0 
  b = 0
# 점 두개를 출력해야 하니까 내부 변수 2개 선언
  for i in range(1,len(aa)):
#리스트 인덱스 활용을 위해 렌지 렌 함수 이용    
    a = aa[i]
    b = aa[i+1]
# a는 현재 for 문으로 들어온 인덱스 자료, b는 다음 인덱스 자료
    if b - a >= 2:
        continue
#만약에 둘을 마이너스한 값이 2(처음 인덱스 2개의 차이) 보다 크면 아무것도 출력하지 말고 그냥 하던일 계속 함
    else:  
      return print("({},{})".format(a,b))
# 이프식에 만족하지 않는 값(기준이 되는 2보다 작은거) 나오면
# (a,b) 형태의 출력값을 가지고 돌아감. 더이상 반복문을 실행하지 않음.

print(search(s))
# 제대로 나오는지 체크
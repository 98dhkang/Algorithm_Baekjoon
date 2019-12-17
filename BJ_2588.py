#(세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.
#(1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.

a=int(input())
b=int(input())

result3=a*(b%10)
result4=a*(b%100-b%10)/10
result5=a*(b//100)
result6=result3+(result4*10)+(result5*100)

print(int(result3))
print(int(result4))
print(int(result5))
print(int(result6))
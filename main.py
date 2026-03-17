
# 1. 정수 자료형 예시
int_variable = 100
print(f"정수 변수: {int_variable}, 자료형: {type(int_variable)}")
# 참고로 파이썬의 int()는 임의 정밀도(Arbitrary Precision)를 사용해서 오버플로우가 일어나지 않는다 ㅇㅇ

# 2. 실수 자료형 예시
float_variable = 3.141592
print(f"실수 변수: {float_variable}, 자료형: {type(float_variable)}")
# float의 고질적인 문제점으로 소수점 연산 시 0.1 + 0.2가 0.30000000000000004라고 나오는 고질적인 문제점이 있다 근데 설명하기에는 너무 오래 걸려 링크를 하나 첨부하였다 https://dev-monkey-dugi.tistory.com/163

# 3. 문자열 자료형 예시
string_variable = "파이썬"
print(f"문자열 변수: {string_variable}, 자료형: {type(string_variable)}")
# 사실 저렇게 귀찮게 하지말고 string_variable = "파이썬"; print(string_variable) 이렇게 출력할수 있다

# 변수는 값을 다시 할당하여 변경할 수 있다
int_variable = 200
print(f"변경된 정수 변수: {int_variable}")

# 다른 자료형의 값도 할당 가능하다
int_variable = "문자열"
print(f"이제 정수 변수가 문자열을 저장: {int_variable}, 자료형: {type(int_variable)}")

# 4. 리스트 자료형 예시
list_variable = [10, 20, 30, "파이썬", "자바스크립트"]
print(f"리스트 변수: {list_variable}, 자료형: {type(list_variable)}")
print(f"리스트 첫 번째 요소: {list_variable[0]}")
list_variable.append("추가된 값") # 리스트는 변경 가능 (가변형)
print(f"리스트 변경 후: {list_variable}")

# 5. 튜플 자료형 예시
tuple_variable = (1, 2, 3, "튜플", "재밌다")
print(f"튜플 변수: {tuple_variable}, 자료형: {type(tuple_variable)}")
print(f"튜플 두 번째 요소: {tuple_variable[1]}")
# tuple_variable.append(4) # 튜플은 변경 불가능 (TypeError 발생)(불변형)

# 6. 딕셔너리 자료형 예시
dict_variable = {"name": "홍길동", "age": 30, "city": "Seoul"}
print(f"딕셔너리 변수: {dict_variable}, 자료형: {type(dict_variable)}")
print(f"딕셔너리 'name'의 값: {dict_variable['name']}")
dict_variable['age'] = 26 # 딕셔너리는 변경 가능 (가변형)
print(f"딕셔너리 변경 후: {dict_variable}")


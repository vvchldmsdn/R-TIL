# 01.26 OOP (객체지향 프로그래밍)

**객체**: 클래스에서 정의한 것을 토대로 메모리에 할당된 것

* 파이썬은 모두 객체로 이루어져 있다.

* 객체는 특정 타입의 인스턴스(예시)이다.
* Class = 붕어빵 틀, 인스턴스 = 붕어빵

* 객체의 특징
  * 타입 / 매서드 / ?

**OOP**: 프로그램을 여러 개의 독립된 객체들과 그 객체들 간의 상호작용으로 파악하는 프로그래밍 방법

절차지향 -> 데이터를 저장을 해놓고 계속 함수를 통해 결과값을 호출하는 방법으로 사용



* 객체지향 예시 ex 1

```python
class Person:
    
    def greting(self):
        print('안녕하세요' + self.name)
        
jimin = Person()
jimin.name = '지민'
jimin.phone = '01050385282'
jimin.greeting()
```

 => 안녕하세요 지민입니다.



* ex 2 - 사각형 넓이 구하기

```python
class Rectangle:
    
    def __init__(self, x, y):
        self.x = y
        self.y = x
        
    def area(self):
        return self.x * self.y
    
R2 = Rectangle()
R2.x = 10
R2.y = 20
R2.area()
```

=> 200

-> 사각형 - 클래스 / 각 사각형 - 인스턴스 / 사각형의 정보 - 속성 / 사각형의 행동 - 매소드 (넓이를 구한다. 높이를 구한다.)

 

## 기본 문법

* 클래스 정의 : class Myclass:
* 인스턴스 생성: my_instance = MyClass()
* 매소드 호출: my_instance.my_method()
* 속성: my_instance.my_attribute





---------------------------------------------

## 클래스

* **클래스 속성**:  한 클래스의 모든 인스턴스라도 똑같은 값을 가지고 잇는 속성
* 













* self = instance 자기 자신

  * => 무조건 self method가 class 안에 들어가야 호출이 됨

  
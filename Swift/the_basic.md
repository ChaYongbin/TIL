# The Basic

## 상수와 변수 

### 상수와 변수의 선언

상수는 let, 변수는 var 로 정의를 한다. 

```swift
let maximumNumberOfLoginAttempts = 10 // 변하지 않는 상수 
var currentLoginAttempt = 0 // 자유롭게 변경할 수 있는 변수
```

변경할 필요가 없는 값을 저장하는 경우는 반드시 `let` 상수로 선언.

### 타입 명시 (Type Annotations)

```swift
var welcomeMessage: String
```

콜론(`:`) 뒤에 타입을 지정할 수 있다. 

```swift
welcomeMessage = "Hello"
```

상수나 변수를 정의하는 지점에 초기값을 지정하는 경우에는 사용할 타입을 추측을 한다. 
`타입 세이프`와 `타입 추정` 이라고 부른다. 

### 상수와 변수 이름 짓기

상수와 변수의 이름에 유니코드를 포함한 모든 문자를 사용할 수 있음. 

다만, 

```swift
let languageName = "Swift"
languageName = "Swift++"
// this is a compile-time error - languageName cannot be changed 
```

변수와 다르게 상수는 한번 값이 정해지면 변경을 할 수 없다. 

### 상수와 변수의 출력

`print` 함수를 사용하면 상수와 변수의 현재 값을 출력 가능.

```swift
print(friendlyWelcome)
```

## 주석(comment)

```swift
//
/* */
```

## 세미콜론(Semicolons)

사용해도 사용하지 않아도 무방.

## 정수(Integers)

`Swift`는 8, 16, 32, 64 비트 형태로 부호있는 정수와 부호없는 정수를 지원

### Int

* 32bit 플랫폼 -> Int32
* 64bit 플랫폼 -> Int64

### UInt

부호가 없는 정수형 타입.
* 32bit 플랫폼 -> UInt32
* 64bit 플랫폼 -> UInt64

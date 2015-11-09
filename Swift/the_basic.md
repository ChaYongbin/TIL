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

### 부동 소수점

Swift는 두가지의 부동 소수점 타임을 제공.
* `Double` 은 64비트 부동 소수점.
* `Float` 은 32비트 부동 소수점.

### 타입 세이프와 타입 추정(Type Safty and Type Inference)

Swift는 타입 세이프 언어.
타입 세이프 언어란, 코드 내에서 다루는 값들의 타입이 명확하도록 만드는 것.

Swift는 또한 타입 추정 때문에 C나 Objective C애 비해 타입을 지정해줘야 하는 경우가 적다.
타입 추정은 상수나 변수를 초기값과 함께 선언할 때 유용하다. 종종 타입 추정은 상수나 변수가 선언되는 지점에서 문자 그대로의 값을 할당하는 것을 통해 이루어진다.

```Swift
let meaningOfLife = 42
// meaningOfLife is inferred to be of type Int
```

이와 비슷하게 부동 소수점을 위한 타입을 지정하지 않으면 Swift는 `Double`형의 타입으로 추정한다.
```Swift
let pi = 3.14159
// pi is inferred to be of type Double
```
Swift는 부동 소수점 수를 위한 타입을 지정시 `Float`가 아니라 항상 `Double`을 선택한다.

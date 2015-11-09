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

## 부동 소수점

Swift는 두가지의 부동 소수점 타임을 제공.
* `Double` 은 64비트 부동 소수점.
* `Float` 은 32비트 부동 소수점.

## 타입 세이프와 타입 추정(Type Safty and Type Inference)

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

## 숫자의 문자표현

정수 문자는 다음과 같이 표현이 된다.
* 10진수는 아무런 접두어 없음.
* 2진수는 접두어 `0b`를 붙혀서
* 8진수는 접두어 `0o`를 붙혀서
* 16진수는 접두어 `0x`를 붙혀서

다음은 십진수 `17`을 표현하는 방식들.
```Swift
let decimalInteger = 17
let binaryInteger = 0b10001       // 17 in binary notation
let octalInteger = 0o21           // 17 in octal notation
let hexadecimalInteger = 0x11     // 17 in hexadecimal notation
```

`exp`지수를 가지고 있는 10진수는 기수에 10의 exp승을 곱해 얻을 수 있다.
* `1.25e2`는 1.25 x 10^2, `125.0`을 의미.
* `1.25e-2`는 1.25 x 10^-2, `0.0125`을 의미.

다음은 부동 소수점 문자는 모두 10진수 `12.1875`를 표현
```Swift
let decimalDouble = 12.1875
let exponentDouble = 1.21875e1
let hexadecimalDouble = 0xC.3p0
```

숫자의 문자표현을 조금 더 쉽게 읽을 수 있도록 추가 형식을 지원
```Swift
let paddedDouble = 000123.456
let oneMillion = 1_000_000
let justOverOneMillion = 1_000_000.000_000_1
```

## 숫자의 타입 변환(Numeric Type Conversion)

### 정수형 변환(Integer Conversion)

정수형의 상수나 변수에 저장 가능한 숫자의 범위는 숫자의 타입에 따라 다름.
```Swift
let cannotBeNegative: UInt8 = -1
// UInt8 cannot store negative numbers, and so this will report an error
let tooBig: Int8 = Int8.max + 1
// Int8 cannot store a number larger than its maximum value,
// and so this will also report an error
```

특별한 숫자 타입에서 다은 타입으로 변환하기 위해서는 존재하는 값을 원하는 타입의 숫자로 초기화.
```Swift
let twoThousand: UInt16 = 2_000
let one: UInt8 = 1
let twoThousandAndOne = twoThousand + UInt16(one)
```

### 정수와 실수 변환(Integer and Floating-Point Conversion)

실수와 정수사이의 변환은 분명하게 만들어야한다.
```Swift
let three = 3
let pointOneFourOneFiveNine = 0.14159
let pi = Double(three) + pointOneFourOneFiveNine
// pi equals 3.14159, and is inferred to be of type Double
```

반대로 실수를 정수로 바꾸는 것도 가능하다. 다만 이 경우에는 `Double`이나 `Float`값을 정수로 초기화 하는 과정이 있어야함.
```Swift
let integerPi = Int(pi)
// integerPi equals 3, and is inferred to be of type Int
```

> NOTE
> 상수나 변수를 결합하기위한 규칙은 numeric literals의 규칙과는 다름.
> numeric literals는 그 스스로가 명시적인 타입을 가지고 있지 않기 때문에 literal value 3은 literal value 0.14159와 바로 더할 수 있음.
> 그들의 타입은 오직 컴파일로 체크한다는 것을 의미.

## 타입 알리아스(Type Aliases)

*타입알리아스* 는 이미 존재하는 타입을 또다른 이름으로 정의하는 것. `typealias`라는 키워드로 타입 알리아스를 정의.

타입 알리아스는 외부의 소스에서온 특정한 사이즈를 가진 데이터로 작업하는 경우 처럼 이미 존재하는 타입을 보다 문맥에 맞는 이름으로 알아보고 싶을때 유용.

```Swift
typealias AudioSample = UInt16
```

타입알리아스를 정의하는 즉시, 당신은 그 타입알리아스를 원래의 이름대신 사용할 수 있음.
```Swift
var maxAmplitudeFound = AudioSample.min
// maxAmplitudeFound is now 0
```

## Booleans

Swift는 `Bool`이라는 기본적인 불리언 타입을 가짐. (`true`와 `flase`)
```Swift
let orangesAreOrange = true
let turnipsAreDelicious = false
```

> `i == 1`의 비교 결과는 `Bool` 타입.

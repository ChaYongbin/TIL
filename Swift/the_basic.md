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


## 튜플(Tuples)

튜플은 여러 값들을 하나의 값으로 묶어준다. 튜플안의 여러 값들은 어느 타입도 가능하고, 각각 동일한 타입일 필요도 없다.

```Swift
let http404Error = (404, "Not Found")
// http404Error is of type (Int, String), and equals (404, "Not Found")
```
`Int`값 하나와 `String` 값 하나를 서로 묶은 것. 이를 `(Int, String)` 타입의 튜플.

튜플의 각 내용들을 분리된 상수나 변수로 분해할 수 있고, 이는 평상시처럼 접근이 가능.
```Swift
let (statusCode, statusMessage) = http404Error
println("The status code is \(statusCode)")
// prints "The status code is 404"
println("The status message is \(statusMessage)")
// prints "The status message is Not Found"
```

튜플을 분리할 때 튜플에서 무시할 부분을 언더바(`_`)로 처리를 하면된다.
```Swift
let (justTheStatusCode, _) = http404Error
println("The status code is \(justTheStatusCode)")
// prints "The status code is 404"
```

또다른 방식은 0부터 시작하는 index number를 통하여 각각의 element value에 접근.
```Swift
println("The status code is \(http404Error.0)")
// prints "The status code is 404"
println("The status message is \(http404Error.1)")
// prints "The status message is Not Found"
```

튜플을 정의할 때 튜플의 각 element들에 이름을 지어줄 수 있음.
```Swift
let http200Status = (statusCode: 200, description: "OK")
println("The status code is \(http200Status.statusCode)")
// prints "The status code is 200"
println("The status message is \(http200Status.description)")
// prints "The status message is OK"
```

> NOTE
> 튜플은 연관성있는 값들을 임시로 묶는데도 유용. 그들은 복잡한 자료구조를 생성하기에는 알맞지 않음. 만일 당신의 자료구조가 임시적이지 않고 계속해서 사용될 것으로 생각된다면, 튜플보다는 클래스나 자료구조로 만드는 것이 나을 것.

## 옵셔널(Optionals)

옵셔널은 어떠한 값이 부재인지를 체크할때 사용.

* 그곳에는 값이 "있다", 그리고 그것은 x와 동일하다.
or
* 그곳에는 값이 전혀 "없다"

> NOTE
> 옵셔널에 대한 개념은 C나 Objective-C에는 존재하지 않는다.

`String`을 `Int`로 변환하기 위해 `Int()` 메서드를 사용
```Swift
let possibleNumber = "123"
let convertedNumber = Int(possibleNumber)
// convertedNumber is inferred to be of type "Int?", or "optional Int"
```
`Int()` 메서드가 실패하는 것으로 보아 `Int`가 아닌 Optional Int값을 리턴한다. optional Int는 `Int`가 아닌 `Int?`로 사용한다. 물음표는 그 값이 optional하다는 것을 의미.
이는 그 값이 어떠한 `Int`값을 가지거나 아에 전혀 값을 가지지 않는다는 것을 의미.
(이는 `Bool`이나 `String`과 같은 다른 값은 가질 수 없다. 이는 오직 `Int`값을 가지거나 아무값도 없을 것.)

### nil (흔히 NULL)

옵셔널 변수에는 `nil`을 설정할 수 있다.
```Swift
var serverResponseCode: Int? = 404
// serverResponseCode contains an actual Int value of 404
serverResponseCode = nil
// serverResponseCode now contains no value
```
> NOTE
> `nil`은 옵겨널이 아닌 상수나 변수에는 사용할 수 없다.

초기값이 없는 옵셔널 변수를 정의한다면, 그 변수는 자동으로 `nil`로 설정이 될 것이다.
```Swift
var surveyAnswer: String?
// surveyAnswer is automatically set to nil
```

### If문과 강제 언랩핑(If Statements and Forced Unwrapping)

어떤 옵셔널이 값을 가지고 있는지 찾기 위해서 `if` 문을 사용할 수 있다. 이 경우 만일 옵셔널이 값을 가지고 있다면 그 결과는 `true`일 것이고 전혀 값을 가지지 않는다면 `false`일 것.

옵셔널이 값을 가진다는 것을 확실히 알 때에는 옵셔널 이름의 맨 마지막에 느낌표를 붙이는 것으로 그 근원값에 접근할 수 있다. 여기서 느낌표는 "내가 이 옵셔널은 확실히 값을 가지고 있고 이를 사용하라"라는 의미를 가지고 있는 것이다.

```Swift
if convertedNumber {
    println("\(possibleNumber) has an integer value of \(convertedNumber!)")
} else {
    println("\(possibleNumber) could not be converted to an integer")
}
// prints "123 has an integer value of 123"
```
> NOTE
> 느낌표를 사용하려면, 항상 옵셔널이 `nil`이 아니라는 것을 확실히 해야한다.

### 옵셔널 바인딩(Optional Binding)

> **NOTICE**
> 이 부분은 아직 무슨 말인지 이해가 잘 안된다. 예제를 만들어서 확인해보자.

 옵셔널이 값을 가지고 있는지를 찾고 만일 그렇다면 값을 임시로 상수나 변수로 사용하도록 만들기 위해 옵셔널 바인딩을 사용할 수 있음.

 옵셔널 바인딩은 `if`문이나 `while`문에서 옵셔널 안에 값이 있는지 체크하고 이를 상수나 변수로 추출하는 것을 한번에 하기 위해 사용할 수 있음.

 ```Swift
if let constantName = someOptional {
    statements
}
```

```Swift
if let actualNumber = Int(possibleNumber) {
    println("\(possibleNumber) has an integer value of \(actualNumber)")
} else {
    println("\(possibleNumber) could not be converted to an integer")
}
// prints "123 has an integer value of 123"
```

> 다음을 의미.
> 만일 `Int(possibleNumber)`가 리턴한 옵셔널 `int`값이 값을 가지고 있을 경우, 새로운 상수인 `actualNumber`를 그 옵셔널이 가지는 값으로 설정한다.

만일 `if`문의 첫번째 문장에서 `actualNumber`의 값을 조종하는 것을 원한다면, `actualNumber`를 변수로 사용할 수 있음.

```Swift
if let firstNumber = Int("4"), secondNumber = Int("42") where firstNumber < secondNumber {
    print("\(firstNumber) < \(secondNumber)")
}
// prints "4 < 42"
```

### 무조건적으로 언랩핑된 옵셔널(Implicitly Unwrapped Optionals)

Implicitly Unwrapped Optional은 옵셔널이 첫번째로 정의되고 옵셔널들이 각 포인트에서 확실하게 존재한다고 가정한 뒤에 옵셔널의 값이 존재하는지 즉시 확인할때 유용하다. Swift에서 Implicitly Unwrapped Optional의 최우선 용도는 클래스의 초기화 과정에서 소유자가 없는 참조나 무조건적인 언랩핑된 옵셔널 속성들을 설명하는 것이다.

```Swift
let possibleString: String? = "An optional string."
println(possibleString!) // requires an exclamation mark to access its value
// prints "An optional string."

let assumedString: String! = "An implicitly unwrapped optional string."
println(assumedString)  // no exclamation mark is needed to access its value
// prints "An implicitly unwrapped optional string."
```

Implicitly Unwrapped Optional을 그것이 사용될때마다 자동적으로 언랩핑을 하기 위한 권한이 주어진 옵셔널으로 생각 할 수 있다. 그것을 사용할때마다 느낌표를 옵셔널의 이름뒤에 붙이는 것 보다는 옵셔널을 선언할때 옵셔널의 타입 뒤에 느낌표를 붙이는 것이 낫다.

만일 Implicitly Unwrapped Optional이 값을 가졌는지를 체크하기 위해서는 여전히 일반적인 옵셔널 처럼 다룰 수 있다:

```Swift
if assumedString {
    println(assumedString)
}
// prints "An implicitly unwrapped optional string."
```
 문장으로 옵셔널의 값을 체크하고 언랩핑하기 위한 Implicitly Unwrapped Optionals의 옵셔널 바인딩도 사용가능하다:

```Swift
if let definiteString = assumedString {
    println(definiteString)
}
// prints "An implicitly unwrapped optional string."
```

## Assertions

코드상에서 값이 없거나 올바르지 않은 경우를 디버그하기 위한 기회를 제공하고 종료 코드를 실행하기 위해 Assertion을 발생시킬수 있다.

### Assertions을 통한 디버그(Debugging with Assertions)

assertion은 논리적 조건이 항상 `true`인지를 런타임에 체크한다. 만일 조건이 false라면 코드는 종료되고, 앱도 종료된다.

전역적인 assert함수로서 assertion을 작성할 수도 있고, assert함수에게 `true`와 `false`를 체크할 조건과 조건이 false일때 출력할 메시지를 넘겨줄 수 있다:

```Swift
let age = -3
assert(age >= 0, "A person's age cannot be less than zero")
// this causes the assertion to trigger, because age is not >= 0
```
오직 `age >= 0`이 `true`일 때 (`age`가 음수가 아닐때)만 실행됩니다. 만일 `age`의 값이 음수라면 위와 같이 `age >= 0`의 결과는 `false`가 되고 assertion이 발생하며 그 앱은 종료됩니다.

Assertion 메시지는 문자어구를 사용해야하는 것은 아니다. assertion 메시지는 다음과 같이 원하는 경우에는 생략도 가능:
```Swift
assert(age >= 0)
```

### Assertion을 사용할 때(When to Use Assertions)

어떠한 조건이 `false`가 될수 있지만 코드 실행을 계속하기 위해서는 반드시 `true`이여만 하는 곳에 assertion을 사용한다. asertion 체크를 포함하는 올바른 경우들은 다음과 같다:

* 어떠한 정수의 서브스크립트 인덱스가 커스텀 서브스크립트 구현을 위해 제공되었으나, 그 서브스크립트 인덱스의 값이 너무 크거나 작을 수 있을때.
* 함수로 넘긴 어떤 값이 함수에서 작업을 진행하는데 적합하지 않은 값일때.
* 옵셔널 값이 현재 nil인데 추후의 코드 실행을 위해서 nil이 아닌 값이 필요할때.

<!--# Programming a Guessing Game -->
# 프로그래밍 추측 게임
<!--Let’s jump into Rust by working through a hands-on project together!-->
이제 실습(hands-on) 프로젝트를 함께 진행하여 Rust(이하 러스트)로 들어가 봅시다!
<!--This chapter introduces you to a few common Rust concepts by showing you how to use them in a real program-->
이 장에서는 여러분에게 실제 프로그램에서 몇 개의 일반적인 러스트 개념들을 어떻게 사용되는지를 보여주면서 이 개념들을 소개하고자 합니다.
<!--You’ll learn about `let`, `match`, methods, associated functions, using external crates, and more! -->
여러분은 `let`, `match`, 메소드, 관련(associated) 함수, 외부 크레이터 사용 등을 배울 것입니다.
<!--The following chapters will explore these ideas in more detail-->
다음 장에서 이 아이디어들을 좀 더 상세히 탐험할 것입니다.
<!--In this chapter, you’ll practice the fundamentals.  -->
이 장에서, 여러분은 기본적인 것을 연습할 것입니다.
We’ll implement a classic beginner programming problem: a guessing game
우리는 고전적인 입문자 프로그래밍 문제인 추측 게임을 구현할 것입니다.
<!--Here’s how it works: the program will generate a random integer between 1 and 100-->
작동 방식은 다음과 같습니다: 프로그램은 1에서 100 사이의 무작위의 정수를 생성합니다.
<!--It will then prompt the player to enter a guess-->
이 때 플레이어에게 추측을 입력하라는 프롬프트(prompt)가 나타날 것입니다.
<!--After a guess is entered, the program will indicate whether the guess is too low or too high-->
이후에 추측이 입력하면, 프로그램은 추측이 너무 낮은지 또는 너무 높은지를 지시합니다.
<!--If the guess is correct, the game will print a congratulatory message and exit.  -->
만약 추측이 맞다면, 그 게임은 축하 메세지를 출력하고 종료됩니다.
<!--## Setting Up a New Project -->
## 새로운 프로젝트 세팅하기
<!--To set up a new project, go to the *projects* directory that you created in Chapter 1 and make a new project using Cargo, like so: -->
새로운 프로젝트를 세팅하기 위해, 1장에서 만들었던 *projects* 디렉토리로 이동하고, Cargo를 이용해 새로운 프로젝트를 만듭니다.

```console
$ cargo new guessing_game 
$ cd guessing_game 
```

<!--The first command, `cargo new`, takes the name of the project (`guessing_game`) as the first argument-->
첫 번째 명령어 `cargo new`는 프로젝트의 이름(`guessing_game`)을 첫번째 인수로 사용합니다.
<!--The second command changes to the new project’s directory. -->
두 번째 명령어는 새로운 프로젝트들의 디렉토리로 이동합니다.
<!--Look at the generated *Cargo.toml* file: -->
생성된 *Cargo.toml* 파일을 보세요.

<span class="filename">Filename: Cargo.toml</span>

```toml
{{#include ../listings/ch02-guessing-game-tutorial/no-listing-01-cargo-new/Cargo.toml}} 
```

<!--If the author information that Cargo obtained from your environment is not correct, fix that in the file and save it again. -->
만약 Cargo가 당신의 환경으로부터 얻은 사용자 정보가 불명확할 경우, 파일 안에서 고치고 그것을 다시 저장하세요.
<!--As you saw in Chapter 1, `cargo new` generates a “Hello, world!” program for you-->
1장에서 본 것과 같이 `cargo new`는 프로그램 “Hello, world!”를 생성합니다.
<!--Check out the *src/main.rs* file: -->
src/main.rs 파일을 살펴봅시다.
<span class="filename">Filename: src/main.rs</span>

```rust
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/no-listing-01-cargo-new/src/main.rs}} 
```

<!--Now let’s compile this “Hello, world!” program and run it in the same step using the `cargo run` command: -->
이제 `cargo run` 명령어를 사용하여 이 “Hello, world!” 프로그램을 컴파일한 후 실행해 봅시다.

```console
{{#include ../listings/ch02-guessing-game-tutorial/no-listing-01-cargo-new/output.txt}} 
```

The `run` command comes in handy when you need to rapidly iterate on a project, as we’ll do in this game, quickly testing each iteration before moving on to the next one.
`run` 명령어는 우리가 다음 단계로 넘어가기 전에 각 반복을 빠르게 테스팅 하는 것을 이 게임에서 하는 것처럼 프로젝트를 빠르게 반복해야 할 때 유용합니다.
<!--Reopen the *src/main.rs* file-->
*src/main.rs* 파일을 다시 열어봅니다.
<!--You’ll be writing all the code in this file.-->
당신은 모든 코드들을 이 파일에 작성할 것입니다.
<!--## Processing a Guess -->
## 추측 진행하기
<!--The first part of the guessing game program will ask for user input, process that input, and check that the input is in the expected form-->
추측하는 게임 프로그램의 첫 번째 파트는 유저의 입력 값을 요구하고, 입력을 처리하고, 입력 값이 기대된 형식에 맞는지 검토합니다.
To start, we’ll allow the player to input a guess
시작하려면 우리는 플레이어가 추측을 입력할 수 있게 해야합니다.
<!--Enter the code in Listing 2-1 into *src/main.rs*. -->
Listing 2-1의 코드를 *src/main.rs* 에 작성하십시오.

<span class="filename">Filename: src/main.rs</span>

```rust,ignore
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/listing-02-01/src/main.rs:all}} 
```

<span class="caption">Listing 2-1: Code that gets a guess from the user and prints it</span>

<!--This code contains a lot of information, so let’s go over it line by line-->
이 코드는 많은 정보를 포함하기에 한 줄 한 줄씩 살펴보겠습니다.
<!--To obtain user input and then print the result as output, we need to bring the `io` (input/output) library into scope-->
유저의 입력 값을 얻고, 그 결과를 아웃풋으로 출력하려면, 우리는 `io`(input/output) 라이브러리를 가져와야합니다.
<!--The `io` library comes from the standard library (which is known as `std`): -->
`io` 라이브러리는 `std` 라고 불리는 표준 라이브러리에 있습니다.

```rust,ignore
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/listing-02-01/src/main.rs:io}} 
```

By default, Rust brings only a few types into the scope of every program in [the *prelude*][prelude]<!-- ignore -->
기본적으로 Rust는 범위(scope)에 [예약어 (the *prelude*)][prelude] 안 모든 프로그램의 오직 몇 가지 타입만 가져옵니다.
<!--If a type you want to use isn’t in the prelude, you have to bring that type into scope explicitly with a `use` statement-->
만약 당신이 사용하기를 원하는 타입이 예약어(prelude) 안에 없다면, 당신은 `use` 문을 사용하여 해당하는 타입을 명시적으로 범위 안으로 가져와야 합니다.
<!--Using the `std::io` library provides you with a number of useful features, including the ability to accept user input. -->
`std::io` 라이브러리를 사용하면 유저 입력 값을 받는 기능(ability)을 포함하여 수 많은 유용한 기능을 제공합니다.
[prelude]: ../std/prelude/index.html

<!--As you saw in Chapter 1, the `main` function is the entry point into the program: -->
당신이 1장에서 봤던 것처럼 `main` 함수는 프로그램의 진입점입니다.

```rust,ignore
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/listing-02-01/src/main.rs:main}} 
```

<!--The `fn` syntax declares a new function, the parentheses, `()`, indicate there are no parameters, and the curly bracket, `{`, starts the body of the function.  -->
`fn` 문법은 새로운 함수를 선언하고 비어있는 소괄호 `()`는 어떠한 파라미터도 없다는 것을 보여주고, 중괄호 `{` 함수의 몸체를 시작합니다.
<!--As you also learned in Chapter 1, `println!` is a macro that prints a string to the screen: -->
당신이 1장 에서 배웠듯이, `println!`은 화면에 프린트를 시작하는 매크로입니다.

```rust,ignore
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/listing-02-01/src/main.rs:print}} 
```

<!--This code is printing a prompt stating what the game is and requesting input from the user. -->
이 코드는 게임이 무엇인지를 알려주고, 사용자로부터 입력값을 요청하는 프롬프트(prompt)를 출력합니다.
<!--### Storing Values with Variables -->
### 변수에 값 저장하기
<!--Next, we’ll create a place to store the user input, like this:  -->
다음으로 우리는 사용자 입력 값을 저장하기 위한 장소를 만들어 줄 것입니다.

```rust,ignore
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/listing-02-01/src/main.rs:string}} 
```

<!--Now the program is getting interesting! -->
이제 프로그램은 좀 더 흥미로워지고 있습니다 !
<!--There’s a lot going on in this little line-->
이 작은 줄에서 많은 일이 일어났습니다.
Notice that this is a `let` statement, which is used to create a *variable*
이것은 *변수(variable)*를 만들 때 사용하는 `let` 문 입니다.
<!--Here’s another example: -->
여기에 또 다른 예시가 있습니다.

```rust,ignore
let foo = bar; 
```

<!--This line creates a new variable named `foo` and binds it to the value of the `bar` variable-->
이 줄은 `foo`라는 이름의 새로운 변수를 만들고 `bar` 변수로 그 값을 묶어 줍니다.
<!--In Rust, variables are immutable by default-->
Rust에서는 변수들은 기본적으로 변경 불가능(immutable)입니다.
<!--We’ll be discussing this concept in detail in the [“Variables and Mutability”][variables-and-mutability] section in Chapter 3-->
우리는 3장의 [“Variables and Mutability”][variables-and-mutability] 섹션에서 좀 더 상세하게 이 개념을 토의할 것입니다.
The following example shows how to use `mut` before the variable name to make a variable mutable:
아래의 예시는 변수를 변경 가능하게 설정하는 `mut`의 사용법을 보여줍니다.

```rust,ignore
let foo = 5; // immutable 
let mut bar = 5; // mutable 
```

<!--> Note: The `//` syntax starts a comment that continues until the end of the line-->
참고: `//` 문법은 줄 끝까지 계속되는 주석을 시작합니다.
<!--Rust ignores everything in comments, which are discussed in more detail in Chapter 3. -->
Rust는 주석 안에 모든 것을 무시합니다. 이것은 3장에서 좀 더 자세히 논의합니다.
<!--Let’s return to the guessing game program-->
이제 다시 추측 게임 프로그램으로 돌아와 봅시다.
<!--You now know that `let mut guess` will introduce a mutable variable named `guess`-->
여러분은 이제 `let mut guess`가 `guess`로 이름을 붙인 변경가능하게 한 변수를 도입한다는 것을 알 것입니다.
<!--On the other side of the equal sign (`=`) is the value that `guess` is bound to, which is the result of calling `String::new`, a function that returns a new instance of a `String`. -->
등호(`=`)의 다른 쪽에는 `guess`가 묶어진 값이 있는데, 그것은 `String`의 새 인스턴스(instance)를 반환하는 함수인 `String :: new`를 호출한 결과 입니다.
<!--[`String`][string] is a string type provided by the standard library that is a growable, UTF-8 encoded bit of text. -->
[`String`][string]은 표준 라이브러리에 의해 제공된 것으로 확장 가능한(growable) UTF-8로 인코딩 된 문자열 타입입니다.
[string]: ../std/string/struct.String.html

<!--The `::` syntax in the `::new` line indicates that `new` is an *associated function* of the `String` type-->
`:: new` 줄의 `::`구문은 `new`가 `String` 유형의 관련 함수(*associated function*)임을 나타냅니다.
<!--An associated function is implemented on a type, in this case `String`, rather than on a particular instance of a `String`-->
관련 함수(*associated function*)는 `String`의 특정 인스턴스가 아닌 유형 (이 경우 `String`)에서 구현됩니다.
<!--Some languages call this a *static method*. -->
몇몇 언어들에서 이것을 정적 메소드(*static method*)라 부릅니다.
<!--This `new` function creates a new, empty string-->
이 `new` 함수는 새로운 빈 문자열을 만듭니다.
<!--You’ll find a `new` function on many types, because it’s a common name for a function that makes a new value of some kind. -->
당신은 `new` 함수를 많은 타입에서 찾아 볼 수 있을 것인데, 왜냐하면, 그것은 어떤 종류의 새로운 값을 만드는 함수의 일반적인 이름이기 때문입니다.
<!--To summarize, the `let mut guess = String::new();` line has created a mutable variable that is currently bound to a new, empty instance of a `String`-->
요약하면 `let mut guess = String :: new ();` 줄은 현재 `String`의 비어있는 새 인스턴스에 바인딩 된 변할 수 있는 변수를 생성했습니다.
<!--Whew!  -->
우!
<!--Recall that we included the input/output functionality from the standard library with `use std::io;` on the first line of the program-->
프로그램의 첫 번째 줄에 `use std :: io;`를 사용하여 표준 라이브러리의 입력 / 출력 기능성을 포함했음을 기억하십시오.
<!--Now we’ll call the `stdin` function from the `io` module: -->
이제 우리는 `io` 모듈의 `stdin` 기능을 호출할 것입니다.

```rust,ignore
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/listing-02-01/src/main.rs:read}} 
```

<!--If we hadn’t put the `use std::io` line at the beginning of the program, we could have written this function call as `std::io::stdin`-->
만약 우리가 프로그램 시작 부분에 `use std :: io` 줄을 넣지 않았다면, 우리는 이 함수 호출을 `std :: io :: stdin`으로 작성할 수 있습니다.
<!--The `stdin` function returns an instance of [`std::io::Stdin`][iostdin], which is a type that represents a handle to the standard input for your terminal.  -->
`stdin` 함수는 사용자의 터미널을 위해 표준 입력에 대한 조작을 나타내는 타입 인 [`std :: io :: Stdin`] [iostdin]의 인스턴스를 반환합니다.
[iostdin]: ../std/io/struct.Stdin.html

<!--The next part of the code, `.read_line(&mut guess)`, calls the [`read_line`][read_line] method on the standard input handle to get input from the user-->
코드의 다음 부분인 `.read_line(&mut guess)`는 사용자로부터 입력을 다루기 위한 표준 입력 메소드인 [`read_line`][read_line]을 호출합니다.
<!--We’re also passing one argument to `read_line`: `&mut guess`. -->
우리는 또한, `read_line`: `&mut guess`에 하나의 인수(argument)를 보낼 수 있습니다.
[read_line]: ../std/io/struct.Stdin.html#method.read_line  

<!--The job of `read_line` is to take whatever the user types into standard input and append that into a string (without overwriting its contents), so it takes that string as an argument-->
`read_line`의 역할은 사용자가 입력하는 모든 것을 표준 입력으로 가져와 문자열에 추가하여 (내용을 덮어 쓰지 않고) 해당 문자열을 인수로 가지는 것입니다.
<!--The string argument needs to be mutable so the method can change the string’s content by adding the user input.  -->
그 문자열 인수는 메소드가 사용자 입력 값을 받아야하기에 변경 가능한 타입이어야 합니다.
The `&` indicates that this argument is a *reference*, which gives you a way to let multiple parts of your code access one piece of data without needing to copy that data into memory multiple times
`&`는 이 인수가 참조(*reference*)임을 나타내는데, 그것은 당신에게 해당 데이터를 메모리를 여러 번 복사 할 필요없이 당신의 코드의 여러 부분이 하나의 데이터에 액세스 할 수 있습니다.
<!--References are a complex feature, and one of Rust’s major advantages is how safe and easy it is to use references-->
참조는 복잡한 기능을 가지는데, Rust의 주요 장점 중 하나는 참조를 사용하는 것이 얼마나 안전하고 쉬운지 입니다.
<!--You don’t need to know a lot of those details to finish this program-->
당신이 이 프로그램을 마치기 위해 이러한 세부 정보를 많이 알 필요는 없습니다.
<!--For now, all you need to know is that like variables, references are immutable by default-->
당신이 지금 당장 알아야 할 것은 변수와 마찬가지로 참조는 기본적으로 변경할 수 없다는 것입니다.
<!--Hence, you need to write `&mut guess` rather than `&guess` to make it mutable. (Chapter 4 will explain references more thoroughly.) -->
따라서 변경 가능하게하려면`& guess`가 아닌`& mut guess`를 작성해야합니다. (4 장에서는 참고에 대해 자세히 설명합니다.)
<!--### Handling Potential Failure with the `Result` Type -->
### `Result` 타입으로 잠재적인 실패 다루기
<!--We’re still working on this line of code-->
우리는 여전히 이 코드 줄에서 작업 중 입니다.
<!--Although we’re now discussing a third line of text, it’s still part of a single logical line of code-->
비록 우리는 이제 텍스트의 세 번째 줄에 대해 논의하고 있지만, 여전히 단일 논리적 코드 줄의 일부분 입니다.
<!--The next part is this method: -->
다음 파트는 이 메소드 입니다.

```rust,ignore
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/listing-02-01/src/main.rs:expect}} 
```

<!--When you call a method with the `.foo()` syntax, it’s often wise to introduce a newline and other whitespace to help break up long lines-->
당신이 `.foo ()`구문을 사용하여 메서드를 호출 할 때, 긴 줄을 나누는 데 도움이 되도록 줄 바꿈 및 기타 공백을 도입하는 것이 좋습니다.
<!--We could have written this code as: -->
우리는 이 코드를 다음과 같이 쓸 수 있습니다.

```rust,ignore
io::stdin().read_line(&mut guess).expect("Failed to read line");
```

<!--However, one long line is difficult to read, so it’s best to divide it-->
그러나, 하나의 긴 줄은 읽기가 어렵기 때문에, 그것을 나누는 것이 최선입니다.
<!--Now let’s discuss what this line does. -->
이제 이 줄이 무엇을 하는지 토의해 봅시다.
<!--As mentioned earlier, `read_line` puts what the user types into the string we’re passing it, but it also returns a value—in this case, an [`io::Result`][ioresult]-->
일찍이 언급했듯이, `read_line` 사용자가 넣은 문자열에 대해 입력하지만 이 경우에 [`io::Result`][ioresult] 의 값을 반환합니다.
<!--Rust has a number of types named `Result` in its standard library: a generic [`Result`][result]as well as specific versions for submodules, such as `io::Result`.  -->
Rust는 표준 라이브러리에 `Result`라는 이름의 여러 유형(types)이 있습니다. 일반적인 [`Result`] 뿐만 아니라 `io::Result`와 같은 하위 모듈에 대한 특정한 버전도 있습니다.

[ioresult]: ../std/io/type.Result.html
[result]: ../std/result/enum.Result.html
 
<!--The `Result` types are [*enumerations*][enums]<!-- ignore -->, often referred to as *enums*-->
`Result` 유형들은 [열거형](*enumerations*)[enums]이라하며 종종, *enums*라 부르기도 합니다.
<!--An enumeration is a type that can have a fixed set of values, and those values are called the enum’s *variants*-->
열거형은 고정된 값의 집합들을 가질 수 있는 유형이며, 그 값들은 열거형의 *변형* 이라고 부릅니다.
<!--Chapter 6 will cover enums in more detail. -->
장 6에서 좀 더 자세히 열거형(enums)에 대해 다룰 것입니다.
[enums]: ch06-00-enums.html 
 
<!--For `Result`, the variants are `Ok` or `Err`-->
`Result`의 경우 그 변형은 `Ok` or `Err` 입니다.
<!--The `Ok` variant indicates the operation was successful, and inside `Ok` is the successfully generated value-->
`Ok` 변형은 작업이 성공했음을 나타내고, `Ok` 안에는 성공적으로 생성 된 값이 있습니다.
<!--The `Err` variant means the operation failed, and `Err` contains information about how or why the operation failed. -->
`Err` 변형은 작업이 실패함을 의미하고 `Err`에는 어떻게 또는 왜 작업이 실패한지에 대한 정보가 포함됩니다.
<!--The purpose of these `Result` types is to encode error-handling information-->
이 `Result` 유형의 목적은 오류 처리(error-handling) 정보를 인코딩하는 것입니다.
<!--Values of the `Result` type, like values of any type, have methods defined on them-->
`Result` 유형의 값들은 모든 유형의 값들과 마찬가지로 메서드가 정의되어 있습니다.
<!--An instance of `io::Result` has an [`expect` method][expect] that you can call-->
`io :: Result`의 인스턴스에는 호출 할 수있는 [`expect` 메소드] [expect]가 있습니다.
<!--If this instance of `io::Result` is an `Err` value, `expect` will cause the program to crash and display the message that you passed as an argument to `expect`-->
만약 이 `io :: Result` 인스턴스가 `Err` 값인 경우 `expect`는 프로그램이 충돌하고 `expect`에 인수로 전달한 메시지를 표시합니다.
<!--If the `read_line` method returns an `Err`, it would likely be the result of an error coming from the underlying operating system-->
만약 `read_line` 메소드가 `Err`을 반환하는 경우에는, 기본적인 운영 체제에서부터 발생하는 오류의 결과 일 수 있습니다.
<!--If this instance of `io::Result` is an `Ok` value, `expect` will take the return value that `Ok` is holding and return just that value to you so you can use it-->
만약 이 `io :: Result` 인스턴스가 `Ok` 값이면 `expect`는 `Ok`가 보유하고 있는 반환 값을 가져 와서 당신이 그 값을 사용할 수 있도록 해당 값만 반환합니다.
<!--In this case, that value is the number of bytes in what the user entered into standard input. -->
이 경우에 그 값은 사용자가 표준 입력으로 입력한 바이트 개수입니다.
[expect]: ../std/result/enum.Result.html#method.expect 

<!--If you don’t call `expect`, the program will compile, but you’ll get a warning:  -->
만약 당신이 `expect`를 호출하지 않는다면, 프로그램은 컴파일되지만 경고가 표시될 것입니다.

```console 
{{#include ../listings/ch02-guessing-game-tutorial/no-listing-02-without-expect/output.txt}} 
```

<!--Rust warns that you haven’t used the `Result` value returned from `read_line`, indicating that the program hasn’t handled a possible error.  -->
Rust는`read_line`에서 반환 된 `Result` 값을 사용하지 않았다고 경고하여, 프로그램이 처리 가능한 오류를 처리하지 않았음을 알려줍니다.
<!--The right way to suppress the warning is to actually write error handling, but because you just want to crash this program when a problem occurs, you can use `expect`-->
경고를 억누르는 올바른 방법은 실제로 오류 처리를 작성하는 것이지만, 당신은 문제가 발생했을 때 프로그램을 중단하고 싶기 때문에 `expect`를 사용할 수 있습니다.
<!--You’ll learn about recovering from errors in Chapter 9.  -->
당신은 9 장에서 오류를 복구하는 것에 대해 배우게 됩니다.

<!--### Printing Values with `println!` Placeholders -->
### `println!` 자리표시자(Placeholders)를 이용한 값 출력
<!--Aside from the closing curly bracket, there’s only one more line to discuss in the code added so far, which is the following: -->
지금까지 추가 된 코드에서 닫는 중괄호를 제외하고 논의할 줄이 하나 더 있습니다. 그 내용은 다음과 같습니다.

```rust,ignore 
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/listing-02-01/src/main.rs:print_guess}} 
```

<!--This line prints the string we saved the user’s input in-->
이 줄은 사용자의 입력을 저장 한 문자열을 출력합니다.
<!--The set of curly brackets, `{}`, is a placeholder: think of `{}` as little crab pincers that hold a value in place-->
중괄호 세트 `{}`는 자리 표시자입니다. `{}`를 값을 제자리에 고정하는 작은 게 집게라고 생각하십시오.
<!--You can print more than one value using curly brackets: the first set of curly brackets holds the first value listed after the format string, the second set holds the second value, and so on-->
당신은 중괄호를 사용하여 둘 이상의 값을 출력할 수 있습니다. 첫 번째 중괄호 세트는 형식 문자열(format string) 다음에 나열된 첫 번째 값을 유지하고 두 번째 세트는 두 번째 값과 기타 값들을 유지합니다.
<!--Printing multiple values in one call to `println!` would look like this: -->
`println!`에 대한 한 번의 호출로 여러 값을 출력하는 것은 다음과 같습니다.

```rust
let x = 5; 
let y = 10; 
 
println!("x = {} and y = {}", x, y); 
```

<!--This code would print `x = 5 and y = 10`. -->
이 코드는 `x = 5 and y = 10`을 출력합니다.
<!--### Testing the First Part -->
### 첫 번째 부분 테스트하기
<!--Let’s test the first part of the guessing game-->
이제 추측 게임의 첫 번째 부분을 테스트 해 보겠습니다.
<!--Run it using `cargo run`:  -->
다음의 코드를 `cargo run`을 이용해 실행하십시오.

<!--manual-regeneration 
cd listings/ch02-guessing-game-tutorial/listing-02-01/ 
cargo clean 
cargo run 
input 6-->

```console 
$ cargo run 
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)     Finished dev [unoptimized + debuginfo] target(s) in 6.44s      Running `target/debug/guessing_game` 
Guess the number!
Please input your guess.
6 
You guessed: 6
``` 
 
<!--At this point, the first part of the game is done: we’re getting input from the keyboard and then printing it. -->
이 시점에서 게임의 첫 번째 부분이 완료되었습니다. 우리는 키보드에서 입력을 받고 그것을 출력합니다.
<!--## Generating a Secret Number -->
## 비밀번호 생성하기
<!--Next, we need to generate a secret number that the user will try to guess-->
다음으로 우리는 사용자가 추측을 시도하기 위한 비밀번호를 생성할 필요가 있습니다.
<!--The secret number should be different every time so the game is fun to play more than once-->
비밀 번호는 매번 달라야 게임을 두 번 이상 플레이해도 즐겁습니다.
<!--Let’s use a random number between 1 and 100 so the game isn’t too difficult-->
게임이 너무 어렵지 않도록 1에서 100 사이의 임의의 숫자를 사용합니다.
<!--Rust doesn’t yet include random number functionality in its standard library-->
Rust는 아직 표준 라이브러리 안에 난수 기능을 포함하지 않습니다.
<!--However, the Rust team does provide a [`rand` crate][randcrate].  -->
그러나, Rust팀은 [`rand` 크레이트][randcrate]를 제공합니다.
[randcrate]: https://crates.io/crates/rand 

<!--### Using a Crate to Get More Functionality -->
### 크레이트를 사용해 더 많은 기능성 확보하기
<!--Remember that a crate is a collection of Rust source code files-->
기억해라 크레이트는 Rust 소스 코드 파일의 모음이다.
<!--The project we’ve been building is a *binary crate*, which is an executable-->
우리가 만들고있는 프로젝트는 실행가능한 *이진 상자*(binary crate) 입니다.
<!--The `rand` crate is a *library crate*, which contains code intended to be used in other programs. -->
`rand` 크레이트는 *라이브러리 크레이트* 로, 다른 프로그램에서 사용하기위한 코드를 포함합니다.
<!--Cargo’s use of external crates is where it really shines-->
Cargo의 외부 크레이트 사용은 정말로 빛납니다.
<!--Before we can write code that uses `rand`, we need to modify the *Cargo.toml* file to include the `rand` crate as a dependency-->
`rand`를 사용하는 코드를 작성하기 전에 우리는 `rand` 크레이트를 의존성을 포함하도록 * Cargo.toml * 파일을 수정할 필요가 있습니다.
<!--Open that file now and add the following line to the bottom beneath the `[dependencies]` section header that Cargo created for you-->
지금 해당 파일을 열고 Cargo가 생성 한 의존성(`[dependencies]`)섹션 헤더 아래 하단에 다음 줄을 추가하세요.
<!--Be sure to specify `rand` exactly as we have here, or the code examples in this tutorial may not work. -->
`rand`를 여기에있는 그대로 지정해야합니다. 그렇지 않으면이 이 튜토리얼의 코드 예제가 작동하지 않을 수 있습니다.
<!-- When updating the version of `rand` used, also update the version of `rand` used in these files so they all match:-->
사용 된`rand`의 버전을 업데이트 할 때, 이 파일에 사용 된`rand`의 버전도 모두 일치하도록 업데이트 하십시오.
<!--* ch07-04-bringing-paths-into-scope-with-the-use-keyword.md * ch14-03-cargo-workspaces.md -->
 
<span class="filename">Filename: Cargo.toml</span> 
 
```toml 
{{#include ../listings/ch02-guessing-game-tutorial/listing-02-02/Cargo.toml:9:}}
``` 
 
<!--In the *Cargo.toml* file, everything that follows a header is part of a section that continues until another section starts-->
*Cargo.toml* 파일에서 헤더 뒤에 오는 모든 것은 다른 섹션이 시작될 때까지 계속되는 섹션의 일부분 입니다.
<!--The `[dependencies]` section is where you tell Cargo which external crates your project depends on and which versions of those crates you require-->
의존성(`[dependencies]`)섹션은 Cargo에 당신의 프로젝트가 의존하는 외부 크레이트와 당신이 필요한 버전의 크레이트를 알려주는 곳입니다.
<!--In this case, we’ll specify the `rand` crate with the semantic version specifier `0.8.3`-->
이 경우에, 우리는 시맨틱(semantic) 버전 지정자 '0.8.3'을 사용하여 `rand` 크레이트를 지정합니다.
<!--Cargo understands [Semantic Versioning][semver](sometimes called *SemVer*), which is a standard for writing version numbers-->
Cargo는 버전 번호 작성을 위한 표준인 시멘틱 버저닝[Semantic Versioning] [semver] (*SemVer*라고도 함)을 이해합니다.
<!--The number `0.8.3` is actually shorthand for `^0.8.3`, which means any version that is at least `0.8.3` but below `0.9.0`-->
숫자 `0.8.3`은 실제로 `^ 0.8.3`의 약자로 이는 `0.8.3` 버전 이상이지만 `0.9.0` 미만인 모든 버전을 의미합니다.
<!--Cargo considers these versions to have public APIs compatible with version `0.8.3`, and this specification ensures you'll get the latest patch release that will still compile with the code in this chapter-->
Cargo는 이러한 버전이 `0.8.3` 버전과 호환되는 공용 API를 가지고 있다고 간주하며, 이 사양은이 장의 코드로 계속 컴파일되는 최신 패치 릴리스를 얻을 수 있도록 보장합니다.
<!--Any version `0.9.0` or greater is not guaranteed to have the same API as what the following examples use. -->
`0.9.0` 이상의 버전은 다음 예제에서 사용하는 것과 동일한 API를 보장하지 않습니다.
[semver]: http://semver.org 
 
<!--Now, without changing any of the code, let’s build the project, as shown in Listing 2-2. -->
이제 어떠한 코드의 변경 없이 Listing 2-2에 표시된대로 프로젝트를 빌드해 보겠습니다.
<!-- manual-regeneration 
cd listings/ch02-guessing-game-tutorial/listing-02-02/ 
cargo clean 
cargo build --> 
 
```console 
$ cargo build 
    Updating crates.io index 
  Downloaded rand v0.8.3 
  Downloaded libc v0.2.86 
  Downloaded getrandom v0.2.2 
  Downloaded cfg-if v1.0.0 
  Downloaded ppv-lite86 v0.2.10 
  Downloaded rand_chacha v0.3.0 
  Downloaded rand_core v0.6.2 
   Compiling rand_core v0.6.2 
   Compiling libc v0.2.86 
   Compiling getrandom v0.2.2 
   Compiling cfg-if v1.0.0 
   Compiling ppv-lite86 v0.2.10 
   Compiling rand_chacha v0.3.0 
   Compiling rand v0.8.3 
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)     Finished dev [unoptimized + debuginfo] target(s) in 2.53s
 ``` 
 
<span class="caption">Listing 2-2: The output from running `cargo build` after adding the rand crate as a dependency</span> 
 
<!--You may see different version numbers (but they will all be compatible with the code, thanks to SemVer!), different lines (depending on the operating system), and the lines may be in a different order. -->
당신은 아마 다른 버전 번호, (SemVer! 덕분에 모두 코드와 호환 가능), 다른 라인 (운영 체제에 따라 다름), 라인 순서가 다를 수 있습니다.  
<!--Now that we have an external dependency, Cargo fetches the latest versions of everything from the *registry*, which is a copy of data from [Crates.io][cratesio]-->
이제 외부 종속성이 있으므로 Cargo는 [Crates.io] [cratesio]의 데이터 사본 인 *레지스트리* 에서 모든 최신 버전을 가져옵니다.
<!--Crates.io is where people in the Rust ecosystem post their open source Rust projects for others to use. -->
Crates.io는 Rust 생태계의 사람들이 다른 사람들이 사용할 수 있도록 그들의 오픈 소스 Rust 프로젝트를 게시하는 곳입니다.
[cratesio]: https://crates.io/ 
 
<!--After updating the registry, Cargo checks the `[dependencies]` section and downloads any crates you don’t have yet-->
레지스트리를 업데이트 한 후 Cargo는 의존성(`[dependencies]`)섹션을 확인하고 아직 가지고 있지 않은 크레이트를 다운로드합니다.
<!--In this case, although we only listed `rand` as a dependency, Cargo also grabbed other crates that `rand` depends on to work-->
이 경우에는 `rand`만 의존성으로 나열했지만 Cargo는 `rand`가 작업에 의존하는 다른 크레이트도 가져 왔습니다.
<!--After downloading the crates, Rust compiles them and then compiles the project with the dependencies available. -->
크레이트를 다운로드 한 후 Rust는 크레이트를 컴파일 한 다음 사용 가능한 의존성으로 프로젝트를 컴파일합니다.
<!--If you immediately run `cargo build` again without making any changes, you won’t get any output aside from the `Finished` line-->
만약 당신이 변경하지 않고 즉시 'cargo build'를 다시 실행하면 당신은 'Finished'줄 외에는 어떤 결과도 출력되지 않습니다.
<!--Cargo knows it has already downloaded and compiled the dependencies, and you haven’t changed anything about them in your *Cargo.toml* file-->
Cargo는 이미 의존성을 다운로드하고 컴파일했으며 *Cargo.toml* 파일에서 의존성에 대해 아무것도 변경하지 않았음을 알고 있습니다.
<!--Cargo also knows that you haven’t changed anything about your code, so it doesn’t recompile that either-->
Cargo는 사용자가 코드에 대해 아무것도 변경하지 않았음을 알고 있으므로 이를 다시 컴파일하지도 않습니다.
<!--With nothing to do, it simply exits. -->
아무것도 하지 않는다면 그것은 단순하게 종료됩니다. 
<!--If you open up the *src/main.rs* file, make a trivial change, and then save it and build again, you’ll only see two lines of output: -->
만약 당신이 *src / main.rs* 파일을 열고 사소한 변경을 만든 다음 저장하고 다시 빌드하면 당신은 오직 두 줄의 출력만 볼 수 있을겁니다.
<!-- manual-regeneration 
cd listings/ch02-guessing-game-tutorial/listing-02-02/ 
touch src/main.rs 
cargo build --> 
 
```console 
$ cargo build 
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 2.53 secs
``` 
 
<!--These lines show Cargo only updates the build with your tiny change to the *src/main.rs* file-->
이 줄은 Cargo가 *src / main.rs* 파일을 약간 변경하여 빌드를 업데이트 한다는 것을 보여줍니다.
<!--Your dependencies haven’t changed, so Cargo knows it can reuse what it has already downloaded and compiled for those-->
의존성이 변경되지 않았으므로 Cargo는 이미 다운로드하고 컴파일한 항목을 재사용 할 수 있음을 알고 있습니다.
<!--It just rebuilds your part of the code. -->
그 코드의 당신의 부분들만 단순하게 재빌드 합니다.
<!--#### Ensuring Reproducible Builds with the *Cargo.lock* File  -->
#### *Cargo.lock* 파일과 함께 재현 가능한 빌드 보장하기
<!--Cargo has a mechanism that ensures you can rebuild the same artifact every time you or anyone else builds your code: Cargo will use only the versions of the dependencies you specified until you indicate otherwise-->
Cargo에는 사용자 또는 다른 사람이 당신의 코드를 빌드 할 때마다 동일한 아티팩트(artifact)를 다시 빌드할 수 있도록 보장하는 메커니즘이 있습니다. Cargo는 사용자가 다르게 표시 할 때까지 사용자가 지정한 의존성 버전만 사용합니다.
<!--For example, what happens if next week version 0.8.4 of the `rand` crate comes out and contains an important bug fix but also contains a regression that will break your code? -->
예를 들면, 만약 다음주에 `rand` 크레이트의 0.8.4 버전이 나오고, 중요한 버그 수정이 포함되어 있지만 코드를 손상시킬 퇴행(regression)도 포함되어 있다면 무슨일이 일어날까요?
<!--The answer to this problem is the *Cargo.lock* file, which was created the first time you ran `cargo build` and is now in your *guessing_game* directory-->
이 문제에 대한 대답은 *Cargo.lock* 파일입니다. 그것은 당신이 처음으로 `cargo build`를 했을 때 만들어지고, 지금은 당신의 *guessing_game* 디렉토리에 있을겁니다.
<!--When you build a project for the first time, Cargo figures out all the versions of the dependencies that fit the criteria and then writes them to the *Cargo.lock* file-->
당신이 처음으로 프로젝트를 빌드 할 때 Cargo는 기준에 맞는 모든 버전의 의존성을 파악한 다음 이를 *Cargo.lock* 파일에 기록합니다.
<!--When you build your project in the future, Cargo will see that the *Cargo.lock* file exists and use the versions specified there rather than doing all the work of figuring out versions again-->
당신이 미래 프로젝트를 빌드 할 때, Cargo는 *Cargo.lock* 파일이 존재하는지 확인할 것이고, 버전을 다시 파악하는 모든 작업을 수행하기 보다는 거기에 지정된 특정한 버전을 사용한다.
<!--This lets you have a reproducible build automatically-->
이것이 당신을 자동으로 재현 가능한 빌드를 가지도록 만든다.
<!--In other words, your project will remain at `0.8.3` until you explicitly upgrade, thanks to the *Cargo.lock* file. -->
다른 말로, 당신의 프로젝트는 *Cargo.lock* 파일에 덕분에 당신이 명시적으로 업그레이드 하기 전까지 `0.8.3` 으로 유지될 것이다. 
<!--#### Updating a Crate to Get a New Version -->
#### 새로운 버전을 가져오기 위해 업데이트하기

<!--When you *do* want to update a crate, Cargo provides another command, `update`, which will ignore the *Cargo.lock* file and figure out all the latest versions that fit your specifications in *Cargo.toml*-->
크레이트를 업데이트하고 싶을 때, Cargo는 *Cargo.lock* 파일을 무시하고 *Cargo.toml*의 당신의 사양에 맞는 모든 최신 버전을 파악하는`update`라는 또 다른 명령을 제공합니다.
<!--If that works, Cargo will write those versions to the *Cargo.lock* file. -->
만약 그것이 작동한다면, Cargo는 *Cargo.lock* 파일에 그 버전들을 작성할 것입니다.
<!--But by default, Cargo will only look for versions greater than `0.8.3` and less than `0.9.0`-->
그러나 기본적으로, Cargo는 오직 `0.9.0` 보다 작고 `0.8.3` 보다 큰 버전만 찾을 것입니다.
<!--If the `rand` crate has released two new versions, `0.8.4` and `0.9.0`, you would see the following if you ran `cargo update`:  -->
만약 `rand` 크레이트가 `0.8.4` 와 `0.9.0` 두개의 새로운 버전을 출시했다면, 당신은 `cargo update`를 실행하면 다음이 표시되는 것을 볼겁니다.
<!-- manual-regeneration 
cd listings/ch02-guessing-game-tutorial/listing-02-02/ 
cargo update 
assuming there is a new 0.8.x version of rand; otherwise use another update as a guide to creating the hypothetical output shown here (not use)-->  

```console
$ cargo update 
    Updating crates.io index 
    Updating rand v0.8.3 -> v0.8.4 
```

<!--At this point, you would also notice a change in your *Cargo.lock* file noting that the version of the `rand` crate you are now using is `0.8.4`.  -->
이 시점에서, 당신은 또한 *Cargo.lock* 파일에서 현재 사용중인 `rand` 크레이트의 버전이 `0.8.4` 임을 알 수 있습니다.
<!--If you wanted to use `rand` version `0.9.0` or any version in the `0.9.x` series, you’d have to update the *Cargo.toml* file to look like this instead:  -->
만약 당신이 `rand` `0.9.0` 버전 또는 `0.9.x` 시리즈의 다른 버전의 사용을 원한다면 당신은 *Cargo.toml* 파일을 다음과 같이 업데이트 해야합니다.

```toml 
[dependencies] 
rand = "0.9.0" 
``` 
 
<!--The next time you run `cargo build`, Cargo will update the registry of crates available and reevaluate your `rand` requirements according to the new version you have specified. -->
다음으로 당신이 `cargo build`를 실행하면, Cargo는 사용 가능한 크레이트의 레지스트리를 업데이트하고 지정한 새 버전에 따라 `rand` 필요 사항을 재평가(reevaluate)합니다.
<!--There’s a lot more to say about [Cargo][doccargo] and [its ecosystem][doccratesio] which we’ll discuss in Chapter 14, but for now, that’s all you need to know-->
[Cargo][doccargo]와 [Cargo 생태계][doccratesio]에 대한 좀 더 자세한 이야기는 14 장에서 논의될 것이지만, 지금은 당신은 이정도 까지만 알아도 됩니다.
<!--Cargo makes it very easy to reuse libraries, so Rustaceans are able to write smaller projects that are assembled from a number of packages. -->
Cargo를 사용하면 라이브러리를 매우 쉽게 재사용 할 수 있으므로, Rust 사용자들(Rustaceans)은 여러 패키지들로 구성된 소규모 프로젝트를 작성할 수 있습니다.

[doccargo]: http://doc.crates.io 
[doccratesio]: http://doc.crates.io/crates-io.html 

<!--### Generating a Random Number -->
### 임의의 숫자 생성하기  
<!--Now that you’ve added the `rand` crate to *Cargo.toml*, let’s start using `rand`-->
지금 *Cargo.toml*에 `rand` 크레이트를 추가했으니, 이제 `rand`를 사용해 봅시다.
<!--The next step is to update *src/main.rs*, as shown in Listing 2-3.  -->
다음 단계는 목록 2-3에 표시된대로 * src / main.rs *를 업데이트하는 것입니다.

<span class="filename">Filename: src/main.rs</span>

```rust,ignore
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/listing-02-03/src/main.rs:all}} 
```

<span class="caption">Listing 2-3: Adding code to generate a random number</span>

<!--First, we add a `use` line: `use rand::Rng`-->
첫 째 우리는 `use` 줄을 추가합니다. 다음과 같이 `use rand::Rng`
<!--The `Rng` trait defines methods that random number generators implement, and this trait must be in scope for us to use those methods-->
`Rng` 속성(trait)은 임의의 숫자 생성기를 실행하는 메소드를 정의하고, 이 속성은 반드시 우리가 해당 메서드를 사용할 수있는 범위 내에 있어야합니다.
<!--Chapter 10 will cover traits in detail.  -->
장 10에서 속성(trait)들에 대해 자세히 소개할 것입니다.
<!--Next, we’re adding two lines in the middle-->
다음으로, 우리는 중앙에 두 개의 줄들을 추가합니다.
<!--The `rand::thread_rng` function will give us the particular random number generator that we’re going to use: one that is local to the current thread of execution and seeded by the operating system-->
`rand :: thread_rng` 함수는 우리가 사용할 특정한 임의의 숫자 생성기를 제공합니다. 하나는 현재 실행 스레드에 로컬이고 운영 체제에 의해 시드(seed)됩니다.
<!--Then we call the `gen_range` method on the random number generator-->
그런 다음 우리는 임의의 숫자 생성기에서 `gen_range` 메소드를 호출합니다.
<!--This method is defined by the `Rng` trait that we brought into scope with the `use rand::Rng` statement-->
이 메소드는 `use rand :: Rng` 문을 사용하여 범위로 가져온 `Rng` 속성에 의해 정의됩니다.
<!--The `gen_range` method takes a range expression as an argument and generates a random number in the range-->
`gen_range` 메소드는 범위 표현식을 인수로 취하고 범위에서 임의의 숫자를 생성합니다.
<!--The kind of range expression we’re using here takes the form `start..end`-->
여기서 우리가 사용하는 범위 표현식의 종류는 `start..end` 형식을 가집니다.
<!--It’s inclusive on the lower bound but exclusive on the upper bound, so we need to specify `1..101` to request a number between 1 and 100-->
하한은 포함하지만 상한은 제외하므로 1에서 100 사이의 숫자를 요청하려면 `1..101`을 지정해야합니다.
<!--Alternatively, we could pass the range `1..=100`, which is equivalent. -->
대안적으로 우리는 동등하다는 `1..=100` 범위를 보낼 수 있습니다.
<!-- > Note: You won’t just know which traits to use and which methods and functions to call from a crate-->
> 참고 : 당신은 어떤 속성을 사용할지, 어떤 메서드와 함수를 크레이트에서 호출해야하는지 알 수 없습니다.
<!-- > Instructions for using a crate are in each crate’s documentation-->
> 크레이트 사용을 위한 지침은 각 크레이트 문서 안에 있습니다.
<!-- > Another neat feature of Cargo is that you can run the `cargo doc --open` command, which will build documentation provided by all of your dependencies locally and open it in your browser-->
> Cargo의 또 다른 멋진 기능은`cargo doc --open` 명령을 실행하여 모든 의존성에서 제공하는 문서를 로컬로 빌드하고 브라우저에서 열 수 있다는 것입니다.
<!-- > If you’re interested in other functionality in the `rand` crate, for example, run `cargo doc --open` and click `rand` in the sidebar on the left. -->
> 만약 당신이 예를 들어`rand` 상자의 다른 기능에 관심이있는 경우`cargo doc --open`을 실행하고 왼쪽 사이드 바에서`rand`를 클릭합니다.
<!--The second line that we added to the middle of the code prints the secret number-->
코드 중간에 추가한 두 번째 줄은 비밀 번호를 출력합니다.
<!--This is useful while we’re developing the program to be able to test it, but we’ll delete it from the final version-->
이것은 프로그램을 개발하는 동안 테스트 할 수 있도록 하기에 유용하지만, 우리는 최종 버전에서는 삭제할 것입니다.
<!--It’s not much of a game if the program prints the answer as soon as it starts! -->
프로그램이 시작되자마자 답을 출력하는 것은 게임이 아닙니다!
<!--Try running the program a few times: -->
몇 회 동안 그 프로그램을 실행해보겠습니다.
<!-- manual-regeneration 
cd listings/ch02-guessing-game-tutorial/listing-02-03/ 
cargo run 
4 
cargo run 
5 (not use)
--> 
 
```console 
$ cargo run 
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 2.53s
     Running `target/debug/guessing_game` 
Guess the number!
The secret number is: 7
Please input your guess.
4 
<!--You guessed: 4 -->
 
$ cargo run 
    Finished dev [unoptimized + debuginfo] target(s) in 0.02s
     Running `target/debug/guessing_game` 
Guess the number!
The secret number is: 83 
Please input your guess. 
5 
<!--You guessed: 5 
``` 
 
<!--You should get different random numbers, and they should all be numbers between 1 and 100-->
당신은 다른 임의의 숫자들을 얻었을 것입니다. 그리고, 그들은 모두 1과 100 사이에 있는 숫자일 겁니다. 
<!--Great job! -->
잘했어요!
<!--## Comparing the Guess to the Secret Number -->
## 비밀번호와 추측 값 비교하기
<!--Now that we have user input and a random number, we can compare them-->
이제 우리는 사용자 입력값과 임의의 숫자를 가지고 있으니 우리는 그것들을 비교할 수 있습니다.
<!--That step is shown in Listing 2-4-->
이제 단계는 목록 2-4에 표시됩니다.
<!--Note that this code won’t compile quite yet, as we will explain. -->
이 코드는 우리가 설명하지만 아직 컴파일되지 않을 것임을 명심하십시오. 
<span class="filename">Filename: src/main.rs</span> 
 
```rust,ignore,does_not_compile 
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/listing-02-04/src/main.rs:here}} 
``` 
 
<span class="caption">Listing 2-4: Handling the possible return values of comparing two numbers</span> 
 
<!--The first new bit here is another `use` statement, bringing a type called `std::cmp::Ordering` into scope from the standard library-->
여기서 첫 번째 새로운 부분은 또 다른 `use` 문으로 `std :: cmp :: Ordering`이라는 타입을 표준 라이브러리에서 범위로 가져옵니다.
<!--Like `Result`, `Ordering` is another enum, but the variants for `Ordering` are `Less`, `Greater`, and `Equal`-->
`Result`와 마찬가지로 `Ordering`은 또 다른 enum이지만, `Ordering`의 변형은 `Less`,`Greater` 및 `Equal`입니다.
<!--These are the three outcomes that are possible when you compare two values. -->
이것들은 세 가지의 결과로 그것은 당신으 두 값을 비교할 때 가능한 것입니다.
<!--Then we add five new lines at the bottom that use the `Ordering` type-->
그런 다음 `Ordering` 타입을 사용하는 5 개의 새 줄을 맨 아래에 추가합니다.
<!--The `cmp` method compares two values and can be called on anything that can be compared-->
`cmp` 메소드는 두 값을 비교하고, 비교할 수있는 모든 것에 호출 될 수 있습니다
<!--It takes a reference to whatever you want to compare with: here it’s comparing the `guess` to the `secret_number`-->
이것은 비교하려는 항목에 대한 참조가 필요합니다. 여기서 추측을 비밀번호와 비교합니다.
<!--Then it returns a variant of the `Ordering` enum we brought into scope with the `use` statement-->
그런 다음 그것은 우리가 `use` 문을 사용하여 범위로 가져온 `Ordering` 열거형(enum)의 변형을 반환합니다.
<!--We use a [`match`][match]expression to decide what to do next based on which variant of `Ordering` was returned from the call to `cmp` with the values in `guess` and `secret_number`. -->
우리는 [`match`] [match] 표현식을 사용하여 추측 및 비밀번호의 값과 함께 `cmp` 호출에서 반환 된 `Ordering`의 변형에 기반하여 다음에 수행 할 작업을 결정합니다.
[match]: ch06-02-match.html 
 
<!--A `match` expression is made up of *arms*-->
`match` 표현식은 *arms* 로 구성됩니다
<!--An arm consists of a *pattern* and the code that should be run if the value given to the beginning of the `match` expression fits that arm’s pattern-->
arm은 *pattern*과 `match` 표현식의 시작 부분에 주어진 값이 해당 arm의 패턴에 맞는 경우 실행 되어야하는 코드로 구성됩니다.
<!--Rust takes the value given to `match` and looks through each arm’s pattern in turn-->
Rust는 `match`에 주어진 값을 받아 차례로 각 arm의 패턴을 살펴 봅니다.
<!--The `match` construct and patterns are powerful features in Rust that let you express a variety of situations your code might encounter and make sure that you handle them all-->
`match` 구조와 패턴은 코드에서 발생할 수있는 다양한 상황을 표현하고 모든 상황을 처리 할 수 ​​있도록하는 Rust의 강력한 기능입니다.
<!--These features will be covered in detail in Chapter 6 and Chapter 18, respectively.  -->
이 기능들은 각각 6장과 18장에서 자세하게 소개될 것입니다.
<!--Let’s walk through an example of what would happen with the `match` expression used here-->
여기에 사용 된 `match` 표현식으로 어떤 일이 발생하는지에 대한 예를 살펴 보겠습니다.
<!--Say that the user has guessed 50 and the randomly generated secret number this time is 38-->
사용자가 50을 추측했다고 해보자, 그리고, 그 임의로 생성된 비밀번호는 이번에 38이라고 하자.
<!--When the code compares 50 to 38, the `cmp` method will return `Ordering::Greater`, because 50 is greater than 38-->
코드가 50과 38을 비교할 때 그 `cmp` 메소드는 `Ordering::Greater`를 반환할 것입니다. 왜냐하면, 50은 38보다 크기 때문입니다.
<!--The `match` expression gets the `Ordering::Greater` value and starts checking each arm’s pattern-->
`match` 표현식은 `Ordering::Greater` 값을 가지고 각 arm의 패턴을 검토하기 시작합니다.
<!--It looks at the first arm’s pattern, `Ordering::Less`, and sees that the value `Ordering::Greater` does not match `Ordering::Less`, so it ignores the code in that arm and moves to the next arm-->
첫 번째 arm의 패턴 인 `Ordering :: Less` 를보고 `Ordering :: Greater` 값이 `Ordering :: Less` 와 일치하지 않음을 확인하여 해당 arm의 코드를 무시하고 다음 arm으로 이동합니다.
<!--The next arm’s pattern, `Ordering::Greater`, *does* match `Ordering::Greater`! -->
다음 arm 패턴 `Ordering::Greater`는 `Ordering::Greater`와 일치 합니다 !
<!--The associated code in that arm will execute and print `Too big!` to the screen-->
그 arm과 연관된 코드는 실행되고 `너무크다 !`를 화면에 출력합니다.
<!--The `match` expression ends because it has no need to look at the last arm in this scenario.  -->
`match` 표현식이 끝납니다. 왜냐하면, 이 시나리오에서 마지막 arm을 확인할 필요가 없기 때문입니다.
<!--However, the code in Listing 2-4 won’t compile yet-->
그러나 목록 2-4의 코드는 아직 컴파일 되지 않았습니다.
<!--Let’s try it:  -->
그것을 해보죠
```console 
{{#include ../listings/ch02-guessing-game-tutorial/listing-02-04/output.txt}}
``` 

<!--The core of the error states that there are *mismatched types*-->
오류의 핵심은 *mismatched types* 이 있다는 것입니다.
<!--Rust has a strong, static type system-->
Rust는 강력하고 정적인 유형 시스템을 가지고 있습니다.
<!--However, it also has type inference-->
그러나, 그것은 또한, 타입 추론도 가지고 있습니다.
<!--When we wrote `let mut guess = String::new()`, Rust was able to infer that `guess` should be a `String` and didn’t make us write the type-->
우리가 `let mut guess = String::new()` 작성했을때 Rust는 추측이 문자열이어야 한다고 추론 할 수 있었고, 타입을 작성하지 않았습니다.
<!--The `secret_number`, on the other hand, is a number type-->
반면에 그 비밀번호는 숫자 타입입니다.
<!--A few number types can have a value between 1 and 100: `i32`, a 32-bit number; `u32`, an unsigned 32-bit number; `i64`, a 64-bit number; as well as others-->
값 1과 100 사이에 몇개의 숫자 타입이 존재할 수 있다. i32, 32 비트 숫자; u32, 부호없는 32 비트 숫자 i64, 64 비트 숫자 기타 등
<!--Rust defaults to an `i32`, which is the type of `secret_number` unless you add type information elsewhere that would cause Rust to infer a different numerical type-->
Rust는 기본적으로`i32`를 사용하는데, 이것은 Rust가 다른 곳에 타입 ​​정보를 추가하지 않는 한 다른 숫자 타입을 추론하게하는 비밀번호의 타입입니다.
<!--The reason for the error is that Rust cannot compare a string and a number type. -->
이 오류의 이유는 Rust는 문자열과 숫자 타입을 비교할 수 없기 때문입니다.
<!--Ultimately, we want to convert the `String` the program reads as input into a real number type so we can compare it numerically to the secret number-->
궁극적으로, 우리는 프로그램이 입력으로 읽은 문자열을 실수 타입으로 변환해야 우리는 숫자로서 그것을 비밀 번호와 비교할 수 있습니다.
<!--We can do that by adding another line to the `main` function body:-->
우리는 `main` 함수 몸통에 또 다른 줄을 추가하여 그것을 할 것입니다.
<span class="filename">Filename: src/main.rs</span>

```rust,ignore 
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/no-listing-03-convert-string-to-number/src/main.rs:here}} 
```

<!--The line is: -->
그 줄은 다음과 같다.

```rust,ignore
let guess: u32 = guess.trim().parse().expect("Please type a number!");
```

<!--We create a variable named `guess`-->
우리는 추측이라 이름지어진 변수를 만들었다.
<!--But wait, doesn’t the program already have a variable named `guess`? -->
그러나 기다려라, 프로그램이 이미 변수 이름 추측을 가지고 있지는 않은가 ?
<!-- It does, but Rust allows us to *shadow* the previous value of `guess` with a new one-->
그렇다. 그러나, Rust는 추측의 이전 값을 새 값으로 *shadow* 하도록 허용한다.
<!--This feature is often used in situations in which you want to convert a value from one type to another type-->
이 기능은 당신이 값을 하나의 타입에서 다른 타입으로 변환하기를 원할 때 종종 사용된다.
<!--Shadowing lets us reuse the `guess` variable name rather than forcing us to create two unique variables, such as `guess_str` and `guess` for example. (Chapter 3 covers shadowing in more detail.) -->
Shadowing을 사용하면 예를 들어 추측 문자열 변수 및 추측 숫자 변수와 같은 두 개의 고유한 변수를 만들지 않고 추측 변수 이름을 재사용 할 수 있습니다. (3 장에서는 Shadowing에 대해 자세히 다룹니다.)
<!--We bind `guess` to the expression `guess.trim().parse()`-->
우리는 추측 변수를 `guess.trim (). parse ()`표현식에 묶(bind)습니다.
<!--The `guess` in the expression refers to the original `guess` that was a `String` with the input in it-->
표현식의 `guess`는 입력이있는 문자열이던 원래 `guess`를 나타냅니다.
<!--The `trim` method on a `String` instance will eliminate any whitespace at the beginning and end-->
문자열 인스턴스에 `trim` 메소드는 처음과 끝에 어떤 공백을 제거합니다.
<!--Although `u32` can contain only numerical characters, the user must press <span class="keystroke">enter</span> to satisfy `read_line`-->
비록 u32는 숫자만 포함 할 수 있지만 `read_line`을 충족하려면 사용자가 <span class = "keystroke"> enter 키를</ span>를 눌러야합니다.
<!--When the user presses <span class="keystroke">enter</span>, a newline character is added to the string-->
사용자가 <span class = "keystroke">enter</span> 키를 눌렀을때 개행 문자가 문자열에 추가됩니다.
<!--For example, if the user types <span class="keystroke">5</span> and presses <span class="keystroke">enter</span>, `guess` looks like this: `5\n`-->
예를 들면, 만약 그 사용자가 <span class="keystroke">5</span>를 치고 <span class="keystroke">enter</span> 키를 누른다면, 추측 변수는 `5\n` 와 같이 보일 것입니다.
<!--The `\n` represents “newline,” the result of pressing <span class="keystroke">enter</span>-->
`\n`은 <span class = "keystroke"> enter</span>를 누른 결과 인 줄 바꿈(newline)을 나타냅니다.
<!--The `trim` method eliminates `\n`, resulting in just `5`. -->
`trim` 메소드는 `\n`를 제거하여 단지 숫자 5를 결과로 만듭니다.
<!--The [`parse` method on strings][parse]<!-- ignore --> parses a string into some kind of number-->
[문자열의 `parse` 메소드][parse]는 문자열을 일종의 숫자로 구문 분석합니다.
<!--Because this method can parse a variety of number types, we need to tell Rust the exact number type we want by using `let guess: u32`-->
왜냐하면, 이 메소드는 다양한 숫자 유형을 분석할 수 있기 때문에 `let guess: u32`를 사용하여 원하는 정확한 숫자 유형을 Rust에 알려 줄 필요가 있습니다.
<!--The colon (`:`) after `guess` tells Rust we’ll annotate the variable’s type-->
`guess` 뒤에 콜론(`:`)은 Rust에 변수 타입에 주석(annotate)을 달 것임을 알려줍니다.
<!--Rust has a few built-in number types; the `u32` seen here is an unsigned, 32-bit integer-->
Rust에는 몇 가지 기본 제공 숫자 유형이 있습니다. 여기에 표시된`u32`는 부호없는 32 비트 정수입니다.
<!--It’s a good default choice for a small positive number-->
그것은 작은 양수에 대한 좋은 기본 선택입니다.
<!--You’ll learn about other number types in Chapter 3-->
당신은 장 3에서 다른 숫자 타입들에 대해서 배울 것입니다.
<!--Additionally, the `u32` annotation in this example program and the comparison with `secret_number` means that Rust will infer that `secret_number` should be a `u32` as well-->
추가적으로 이 예제 프로그램에서 `u32` 주석과 비밀번호와 비교는 Rust가 비밀번호 역시 `u32` 임을 추론해야함을 의미합니다. 
<!--So now the comparison will be between two values of the same type!-->
그래서 지금 그 비교는 같은 타입의 두 값들 사이에서 이루어 질 것입니다.  
[parse]: ../std/primitive.str.html#method.parse
 
<!--The call to `parse` could easily cause an error-->
`parse`를 호출하는 것은 쉽게 오류를 일으킬 수 있습니다.
<!--If, for example, the string contained `A👍%`, there would be no way to convert that to a number-->
만약에 예를 들면, 그 문자열이 `A👍%`를 포함한다면, 거기에는 숫자로 변환하는 어떤 방법도 없습니다.
<!--Because it might fail, the `parse` method returns a `Result` type, much as the `read_line` method does (discussed earlier in [“Handling Potential Failure with the `Result` Type”](#handling-potential-failure-with-the-result-type))-->
왜냐하면, 그것은 실패할 수 있기 때문인데, `parse` 메서드는`read_line` 메서드와 마찬가지로 `Result` 타입을 반환합니다. (앞서 [ "`Result` 타입으로 잠재적 실패 처리"에서 논의 됨] (# handling-potential-failure- 결과 타입))
<!--We’ll treat this `Result` the same way by using the `expect` method again-->
우리는 다시 `expect` 메소드를 사용하여 이 결과를 동일한 방식으로 처리합니다.
<!--If `parse` returns an `Err` `Result` variant because it couldn’t create a number from the string, the `expect` call will crash the game and print the message we give it-->
만약 `parse`가 문자열로부터 숫자를 생성할 수 없기에 `Err` `Result` 변형을 반환한다면, `expect` 호출은 게임을 중단하고 우리가 제공 한 메시지를 출력합니다.
<!--If `parse` can successfully convert the string to a number, it will return the `Ok` variant of `Result`, and `expect` will return the number that we want from the `Ok` value. -->
만약 `parse`가 문자열로부터 숫자를 성공적으로 변환했다면, 그것은 `Ok` `Result` 변형을 반환할 것이고, `expect` 호출은 `Ok` 값에서 원하는 숫자를 반환합니다.
<!--Let’s run the program now! -->
이제 프로그램을 실행해 봅시다.
<!-- manual-regeneration 
cd listings/ch02-guessing-game-tutorial/no-listing-03-convert-string-to-number/ cargo run 
  76 (not use)
--> 
 
```console 
$ cargo run 
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 0.43s
     Running `target/debug/guessing_game` 
Guess the number!
The secret number is: 58 
Please input your guess.
 76 
You guessed: 76
Too big!
``` 
 
<!--Nice! -->
좋아요!
<!--Even though spaces were added before the guess, the program still figured out that the user guessed 76-->
추측하기 전에 공백이 추가되었지만, 프로그램은 여전히 ​​사용자가 76을 추측한 것으로 파악했습니다.
<!--Run the program a few times to verify the different behavior with different kinds of input: guess the number correctly, guess a number that is too high, and guess a number that is too low.  -->
프로그램을 몇 번 실행하여 다른 종류의 입력으로부터 나오는 다른 동작을 확인하십시오. 숫자를 올바르게 추측하고, 너무 높은 숫자를 추측하고, 너무 낮은 숫자를 추측하는 것.
<!--We have most of the game working now, but the user can make only one guess-->
우리는 이제 대부분의 게임이 작동하는 것을 가지지만, 사용자는 오직 하나의 추측만 가능합니다.
<!--Let’s change that by adding a loop! -->
반복문(loop)을 추가하여 변경해 보겠습니다!
<!--## Allowing Multiple Guesses with Looping -->
## 반복문(loop)을 통하여 여러번의 추측 허용하기
<!--The `loop` keyword creates an infinite loop-->
`loop` 키워드는 무한한 반복을 만듭니다.
<!--We’ll add that now to give users more chances at guessing the number: -->
우리는 사용자들이 숫자를 추측하는데 좀 더 기회를 제공하도록 추가할 것입니다.
<span class="filename">Filename: src/main.rs</span> 
 
```rust,ignore 
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/no-listing-04-looping/src/main.rs:here}} 
``` 
 
<!--As you can see, we’ve moved everything into a loop from the guess input prompt onward-->
당신이 볼 수 있듯이, 우리는 추측 입력 프롬프트에서 모든 것을 반복문으로 옮겼습니다.
<!--Be sure to indent the lines inside the loop another four spaces each and run the program again-->
반복문 안의 줄을 각각 4 칸씩 들여 쓰기하고 프로그램을 다시 실행하십시오.
<!--Notice that there is a new problem because the program is doing exactly what we told it to do: ask for another guess forever! It doesn’t seem like the user can quit! -->
프로그램이 우리가 지시 한대로 정확히 수행하기 때문에 새로운 문제가 있음을 주목하십시오. 영원히 다른 추측을 요구한다! 사용자가 종료 할 수없는 것같습니다!
<!--The user could always interrupt the program by using the keyboard shortcut <span class="keystroke">ctrl-c</span>-->
사용자는 언제든지 키보드 단축키 <span class="keystroke">ctrl-c</span> 를 이용해 프로그램을 중단할 수 있습니다.
<!--But there’s another way to escape this insatiable monster, as mentioned in the `parse` discussion in [“Comparing the Guess to the Secret Number”](#comparing-the-guess-to-the-secret-number): if the user enters a non-number answer, the program will crash-->
그러나 ["Comparing the Guess to the Secret Number"](# comparing-the-guess-to-the-secret-number)의 `parse` 토론에서 언급했듯이 이 만족할 줄 모르는 괴물을 피할 수 있는 또 다른 방법이 있습니다. 만약 답변으로 숫자가 아닌 답변을 입력하면, 프로그램이 중단될 것입니다.
<!--The user can take advantage of that in order to quit, as shown here:  -->
사용자는 여기에 표시된 것처럼 종료하기 위해 사용할 수 있습니다.
<!-- manual-regeneration 
cd listings/ch02-guessing-game-tutorial/no-listing-04-looping/ cargo run 
(too small guess) 
(too big guess) 
(correct guess) 
quit (not use)
--> 
 
```console 
$ cargo run 
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 1.50s
     Running `target/debug/guessing_game` 
Guess the number!
The secret number is: 59 
Please input your guess.
45 
You guessed: 45
Too small!
Please input your guess.
60 
You guessed: 60 
Too big!
Please input your guess. 
59 
You guessed: 59 
You win!
Please input your guess.
quit 
thread 'main' panicked at 'Please type a number!: ParseIntError { kind: InvalidDigit }', src/main.rs:28:47 
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
```

<!--Typing `quit` actually quits the game, but so will any other non-number input-->
`quit`을 치는 것은 실제로 게임을 종료합니다만, 다른 어떤 숫자가 아닌 입력도 가능합니다.
<!--However, this is suboptimal to say the least-->
그러나, 이것은 최적이라고 말하기에는 못 미치는 차선책 입니다.
<!--We want the game to automatically stop when the correct number is guessed. -->
우리는 정확한 숫자를 추측했을 때 게임이 자동적으로 멈추기를 원합니다.
<!--### Quitting After a Correct Guess -->
### 정확한 추측 이후에 종료하기
<!--Let’s program the game to quit when the user wins by adding a `break` statement:  -->
`break`문을 추가하여 사용자가 이기면 게임이 종료되도록 프로그래밍 해 보겠습니다.

<span class="filename">Filename: src/main.rs</span> 
 
```rust,ignore 
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/no-listing-05-quitting/src/main.rs:here}} 
``` 
 
<!--Adding the `break` line after `You win!` makes the program exit the loop when the user guesses the secret number correctly-->
`You win!` 이후에 `break` 줄을 추가하여, 사용자가 비밀번호를 정확하게 추측했을 때 반복이 종료되도록 프로그램을 만들어 봅시다.
<!--Exiting the loop also means exiting the program, because the loop is the last part of `main`.  -->
반복문이 종료된다는 것은 프로그램의 종료를 의미합니다. 왜냐하면, 반복문은 `main`의 마지막 부분이기 때문입니다.
<!--### Handling Invalid Input -->
### 잘못된 입력값 다루기
<!--To further refine the game’s behavior, rather than crashing the program when the user inputs a non-number, let’s make the game ignore a non-number so the user can continue guessing-->
게임의 동작을 더 세분화하기 위해사용자가 숫자가 아닌 값을 입력 할 때 프로그램이 충돌하는 대신 게임에서 숫자가 아닌 항목을 무시하도록하여 사용자가 계속 추측할 수 있도록 합니다.
<!--We can do that by altering the line where `guess` is converted from a `String` to a `u32`, as shown in Listing 2-5.  -->
우리는 목록 2-5와 같이 `guess`가 문자열에서 u32로 변환되는 행을 변경하여 이를 수행 할 수 있습니다.

<span class="filename">Filename: src/main.rs</span> 

```rust,ignore
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/listing-02-05/src/main.rs:here}} 
```

<span class="caption">Listing 2-5: Ignoring a non-number guess and asking for another guess instead of crashing the program</span>

<!--Switching from an `expect` call to a `match` expression is how you generally move from crashing on an error to handling the error-->
`expect` 호출에서 `match` 표현식으로 전환하는 것은 일반적으로 오류 발생시 충돌하는 것에서 오류 처리로 이동하는 방법입니다.
<!--Remember that `parse` returns a `Result` type and `Result` is an enum that has the variants `Ok` or `Err`-->
`parse`가 `Result` 타입을 반환하는 것과 `Result`는`Ok` 또는`Err` 변형이 있는 열거 형임을 기억하십시오.
<!--We’re using a `match` expression here, as we did with the `Ordering` result of the `cmp` method. -->
우리는 여기서 `cmp` 메소드의 `Ordering` 결과와 마찬가지로 `match` 표현식을 사용했습니다.
<!--If `parse` is able to successfully turn the string into a number, it will return an `Ok` value that contains the resulting number-->
만약 `parse`가 문자열을 숫자로 성공적으로 전환할 수 있다면, 그것은 결과 숫자를 포함하는 `Ok` 값을 반환할 것입니다.
<!--That `Ok` value will match the first arm’s pattern, and the `match` expression will just return the `num` value that `parse` produced and put inside the `Ok` value-->
이 `Ok` 값은 첫 번째 arm 패턴과 일치할 것이고, 그 `match` 표현식은 `parse`가 생성 한 숫자 값을 반환하고 `Ok` 값 안에 넣습니다.
<!--That number will end up right where we want it in the new `guess` variable we’re creating.  -->
그 숫자는 우리가 만들고있는 새로운 `guess` 변수에서 우리가 원하는 위치에 올 것입니다.
<!--If `parse` is *not* able to turn the string into a number, it will return an `Err` value that contains more information about the error-->
만약 `parse`가 문자열을 숫자로 전환하지 못했다면, 그것은 오류에 대한 정보를 포함하는 `Err` 값을 반환할 것입니다.
<!--The `Err` value does not match the `Ok(num)` pattern in the first `match` arm, but it does match the `Err(_)` pattern in the second arm-->
`Err` 값은 arm의 첫 번째 매치 값 안의 패턴인 `Ok(num)`과 일치하지 않을 것이지만, 그것은 두 번째 arm의 패턴인 `Err(_)`와 일치한다.
<!--The underscore, `_`, is a catchall value; in this example, we’re saying we want to match all `Err` values, no matter what information they have inside them-->
밑줄인 `_`는 포괄적인 값이다. 이 예제에서 우리는 `Err` 값이 어떤 정보를 가지고 있든 상관없이 모든 `Err`값을 일치 시키려고합니다.
<!--So the program will execute the second arm’s code, `continue`, which tells the program to go to the next iteration of the `loop` and ask for another guess-->
그래서 그 프로그램은 두 번째 arm 코드 `continue`가 실행될 것입니다. 이 코드는 프로그램이 `loop`의 다음 반복(iteration)으로 이동하여 다른 추측을 요청하도록 지시합니다.
<!--So, effectively, the program ignores all errors that `parse` might encounter!-->
그래서  프로그램은 효과적으로 `parse`가 마주하는 모든 에러들을 무시합니다.
<!--Now everything in the program should work as expected-->
이제 프로그램 안의 모든 것이 기대한대로 작동합니다.
<!--Let’s try it:  -->
실행해 봅시다.
<!-- manual-regeneration 
cd listings/ch02-guessing-game-tutorial/listing-02-05/ 
cargo run 
(too small guess) 
(too big guess) 
foo 
(correct guess) (not use)
--> 
 
```console 
$ cargo run 
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)     Finished dev [unoptimized + debuginfo] target(s) in 4.45s      Running `target/debug/guessing_game` 
Guess the number!
The secret number is: 61
Please input your guess.
10 
You guessed: 10
Too small!
Please input your guess.
99 
You guessed: 99
Too big!
Please input your guess.
foo 
Please input your guess.
61 
You guessed: 61
You win!
``` 
 
<!--Awesome!-->
멋져요!
<!--With one tiny final tweak, we will finish the guessing game-->
마지막으로 조금만 조정하면 추측 게임이 끝납니다.
<!--Recall that the program is still printing the secret number-->
프로그램은 여전히 비밀번호를 출력한다는 것을 떠올리십시오.
<!--That worked well for testing, but it ruins the game-->
그것은 테스트에는 잘 작동했지만, 게임을 망쳤습니다.
<!--Let’s delete the `println!` that outputs the secret number-->
비밀번호를 산출하는 `println!` 문을 지워 봅시다.
<!--Listing 2-6 shows the final code. -->
목록 2-6은 마지막 코드를 보여줍니다.
<span class="filename">Filename: src/main.rs</span> 
 
```rust,ignore 
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/listing-02-06/src/main.rs}} 
``` 
 
<span class="caption">Listing 2-6: Complete guessing game code</span>  

<!--## Summary -->
## 요약
 
<!--At this point, you’ve successfully built the guessing game-->
이 시점에서 당신은 성공적으로 추측 게임을 빌드 했을겁니다.
<!--Congratulations!  -->
축하해요!
<!--This project was a hands-on way to introduce you to many new Rust concepts: `let`, `match`, methods, associated functions, the use of external crates, and more-->
이 프로젝트는 'let', 'match', 메서드, 관련 함수, 외부 크레이트 사용 등 많은 새로운 Rust 개념을 소개하는 실습 방법이었습니다.
<!--In the next few chapters, you’ll learn about these concepts in more detail-->
다음으로 오는 몇개의 장에서는 당신은 이 개념들을 좀 더 자세히 배우게 될 것입니다.
<!--Chapter 3 covers concepts that most programming languages have, such as variables, data types, and functions, and shows how to use them in Rust-->
장 3장은 대부분의 프로그래밍 언어들이 가지고 있는 변수, 데이터 타입, 함수 등 개념을 소개하고 Rust에서의 사용법을 다룹니다.
<!--Chapter 4 explores ownership, a feature that makes Rust different from other languages-->
장 4장은 Rust가 다른 언어와 다르게 만드는 기능인 소유권(ownership)에 대해 탐험합니다.
<!--Chapter 5 discusses structs and method syntax, and Chapter 6 explains how enums work. -->
장 5 장에서는 구조체와 메서드 구문에 대해 설명하고 장 6 장에서는 열거 형의 작동 방식을 설명합니다.
[variables-and-mutability]: 

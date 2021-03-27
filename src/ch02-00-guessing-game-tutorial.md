<!--# Programming a Guessing Game -->
# 프로그래밍 추측 게임
<!--Let’s jump into Rust by working through a hands-on project together!-->
이제 실습 프로젝트를 함께 진행하여 러스트로 들어가 봅시다 !
<!--This chapter introduces you to a few common Rust concepts by showing you how to use them in a real program-->
이 챕터는 당신에게 몇개의 일반적인 러스트 개념들을 실제 프로그램에서 그것들이 어떻게 사용되는지를 보여주는 것으로 소개합니다.
<!--You’ll learn about `let`, `match`, methods, associated functions, using external crates, and more! -->
당신은 `let`, `match`, 메소드, 연관 함수, 외부 크레이터 사용 등을 배울 것 입니다.
<!--The following chapters will explore these ideas in more detail-->
다음에 오는 챕터들에서 이 아이디어들을 좀 더 상세히 탐험할 것 입니다.
<!--In this chapter, you’ll practice the fundamentals.  -->
이 챕터에서는 당신은 기본적인 것을 연습할 것 입니다.
<!--We’ll implement a classic beginner programming problem: a guessing game-->
우리는 고전적인 입문자 프로그래밍 문제인 추측 게임을 구현할 것 입니다.
<!--Here’s how it works: the program will generate a random integer between 1 and 100-->
작동 방식은 다음과 같다: 프로그램은 1에서 100 사이의 무작위의 정수를 생성한다.
<!--It will then prompt the player to enter a guess-->
그 때에 플레이어에게 추측을 입력하라는 창(prompt)이 나타날 것 입니다.
<!--After a guess is entered, the program will indicate whether the guess is too low or too high-->
이후에 추측이 입력되었으면, 프로그램은 추측이 너무 낮은지 또는 너무 높은지를 지시합니다.
<!--If the guess is correct, the game will print a congratulatory message and exit.  -->
만약 추측이 맞다면, 그 게임은 축하 메세지를 출력하고 종료됩니다.
<!--## Setting Up a New Project -->
## 새로운 프로젝트 세팅하기
<!--To set up a new project, go to the *projects* directory that you created in Chapter 1 and make a new project using Cargo, like so: -->
새로운 프로젝트를 세팅하기 위해, 챕터1을 만들었던 *projects* 디렉토리로 이동하고, Cargo를 이용해 새로운 프로젝트를 만듭니다.

```console
$ cargo new guessing_game 
$ cd guessing_game 
```

<!--The first command, `cargo new`, takes the name of the project (`guessing_game`) as the first argument-->
첫 번째 명령어 `cargo new`는 프로젝트의 이름(`guessing_game`)을 첫번째 인수로 사용합니다.
<!--The second command changes to the new project’s directory. -->
두 번째 명령어는 새로운 프로젝트들의 디렉토리로 변경하는 것 입니다.
<!--Look at the generated *Cargo.toml* file: -->
생성 된 *Cargo.toml* 파일을보십시오.

<span class="filename">Filename: Cargo.toml</span>

```toml
{{#include ../listings/ch02-guessing-game-tutorial/no-listing-01-cargo-new/Cargo.toml}} 
```

<!--If the author information that Cargo obtained from your environment is not correct, fix that in the file and save it again. -->
만약 카고가 당신의 환경으로부터 얻은 사용자 정보가 불명확할 경우, 파일 안에서 고치고 그것을 다시 저장하십시오.
<!--As you saw in Chapter 1, `cargo new` generates a “Hello, world!” program for you-->
당신이 챕터 1에서 본 것과 같이 `cargo new`는 당신을 위해 프로그램 “Hello, world!”를 생성합니다.
<!--Check out the *src/main.rs* file: -->
src/main.rs 파일을 살펴봅시다. 
<span class="filename">Filename: src/main.rs</span> 

```rust
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/no-listing-01-cargo-new/src/main.rs}} 
```

<!--Now let’s compile this “Hello, world!” program and run it in the same step using the `cargo run` command: -->
이제 이 “Hello, world!” 프로그램을 컴파일하고, 같은 단계에서 `cargo run` 명령어를 통해 실행해 봅시다.

```console
{{#include ../listings/ch02-guessing-game-tutorial/no-listing-01-cargo-new/output.txt}} 
```

<!--The `run` command comes in handy when you need to rapidly iterate on a project, as we’ll do in this game, quickly testing each iteration before moving on to the next one. -->
`run` 명령어는 우리가 다음 단계로 넘어가기 전에 각 반복을 빠르게 테스팅 하는 것을 이 게임에서 하는 것처럼 프로젝트를 빠르게 반복해야 할 때 유용합니다.
<!--Reopen the *src/main.rs* file-->
*src/main.rs* 파일을 다시 열어봅니다.
<!--You’ll be writing all the code in this file.-->
당신은 모든 코드들을 이 파일에 작성할 것 입니다.
<!--## Processing a Guess -->
## 추리 처리하기
<!--The first part of the guessing game program will ask for user input, process that input, and check that the input is in the expected form-->
추측하는 게임 프로그램의 첫 번째 파트는 유저의 입력 값을 묻고, 입력을 처리하고, 입력 값이 기대된 형식이 맞는지 검토합니다.
<!--To start, we’ll allow the player to input a guess-->
시작하기 위해 우리는 플레이어가 추측을 입력하기위해 허용해야 합니다.
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
유저의 입력 값을 얻고, 그 결과를 아웃풋으로 출력하려면, 우리는 `io`(input/output) 라이브러리를 범위(scope)로 가져와야합니다.
<!--The `io` library comes from the standard library (which is known as `std`): -->
`io` 라이브러리는 `std` 라고 불리는 표준 라이브러리에 있습니다.

```rust,ignore 
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/listing-02-01/src/main.rs:io}} 
```

<!--By default, Rust brings only a few types into the scope of every program in [the *prelude*][prelude]<!-- ignore -->-->
기본적으로 러스트는 범위(scope)에 [the *prelude*][prelude] 안 모든 프로그램의 오직 몇 가지 타입만 가져옵니다.
<!--If a type you want to use isn’t in the prelude, you have to bring that type into scope explicitly with a `use` statement-->
만약 당신이 사용하기를 원하는 타입이 prelude 안에 없다면, 당신은 `use` 문을 사용하여 해당하는 타입을 명시적으로 범위 안으로 가져와야 합니다.
<!--Using the `std::io` library provides you with a number of useful features, including the ability to accept user input. -->
`std::io` 라이브러리를 사용하면 당신에게 유저 입력 값을 받는 능력을 포함하여 수 많은 유용한 기능을 제공합니다. 
[prelude]: ../std/prelude/index.html 

<!--As you saw in Chapter 1, the `main` function is the entry point into the program: -->
당신이 챕터 1에서 봤던 것처럼 `main` 함수는 프로그램의 진입점 입니다.

```rust,ignore 
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/listing-02-01/src/main.rs:main}} 
```

<!--The `fn` syntax declares a new function, the parentheses, `()`, indicate there are no parameters, and the curly bracket, `{`, starts the body of the function.  -->
`fn` 문법은 새로운 함수를 선언하고 소괄호 `()` 는 어떠한 파라미터도 없다는 것을 보여주고, 중괄호 `{` 함수의 몸체를 시작합니다.
<!--As you also learned in Chapter 1, `println!` is a macro that prints a string to the screen: -->
당신이 챕터 1에서 배웠듯이, `println!`은 화면에 프린트를 시작하는 매크로 입니다. 

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
이제 프로그램은  좀 더 흥미로워지고 있습니다.
<!--There’s a lot going on in this little line-->
이 작은 줄에서 많은 일이 일어났습니다.
<!--Notice that this is a `let` statement, which is used to create a *variable*-->
이것은 *variable* 변수를 만들 때 사용하는 `let` 문 입니다. 
<!--Here’s another example: -->
여기에 또 다른 예시가 있습니다.

```rust,ignore
let foo = bar; 
```

<!--This line creates a new variable named `foo` and binds it to the value of the `bar` variable-->
이 줄은 `foo`라는 이름의 새로운 변수를 만들고 `bar` 변수로 그 값을 묶어 줍니다.
<!--In Rust, variables are immutable by default-->
러스트에서는 변수들은 기본적으로 불변형(immutable)입니다. 
<!--We’ll be discussing this concept in detail in the [“Variables and Mutability”][variables-and-mutability]<!-- ignore --> section in Chapter 3-->
우리는 챕터 3의 [“Variables and Mutability”][variables-and-mutability] 섹션에서 좀 더 상세하게 이 개념을 토의할 것입니다.
<!--The following example shows how to use `mut` before the variable name to make a variable mutable: -->
아래의 예시는 변수를 변경 가능하게 만들기 위해 변수 이름 앞에 `mut`을 어떻게 사용하는지 보여줍니다.

```rust,ignore
let foo = 5; // immutable 
let mut bar = 5; // mutable 
```

<!--> Note: The `//` syntax starts a comment that continues until the end of the > line-->
Note: `//` 문법은 > 줄 끝까지 계속되는 주석을 시작합니다.
<!--Rust ignores everything in comments, which are discussed in more detail > in Chapter 3. -->
러스트는 주석 안에 모든 것을 무시합니다. 이것은 3장에 좀 더 자세히 설명합니다.
<!--Let’s return to the guessing game program-->
이제 다시 추측 게임 프로그램으로 돌아와 봅시다.
<!--You now know that `let mut guess` will introduce a mutable variable named `guess`-->
당신은 이제 `let mut guess`가 변수 이름 `guess`를 변경가능하게 도입한다는 것을 알 것입니다.
<!--On the other side of the equal sign (`=`) is the value that `guess` is bound to, which is the result of calling `String::new`, a function that returns a new instance of a `String`. -->
등호(`=`)의 다른 쪽에는 `guess`가 묶어진 값이 있는데, 그것은 `String`의 새 인스턴스(instance)를 반환하는 함수 인`String :: new`를 호출한 결과 입니다.
<!--[`String`][string] is a string type provided by the standard library that is a growable, UTF-8 encoded bit of text. -->
[`String`][string] 은 표준 라이브러리에의해 제공된 것으로 확장 가능한(growable) UTF-8 인코딩의 문자열 타입입니다.
[string]: ../std/string/struct.String.html

<!--The `::` syntax in the `::new` line indicates that `new` is an *associated function* of the `String` type-->
`:: new` 줄의 `::`구문은 `new`가 `String` 유형의 관련 함수(*associated function*)임을 나타냅니다.
<!--An associated function is implemented on a type, in this case `String`, rather than on a particular instance of a `String`-->
연결된 함수는 `String`의 특정 인스턴스가 아닌 유형 (이 경우 `String`)에서 구현됩니다.
<!--Some languages call this a *static method*. -->
몇몇 언어들에서 이것을 정적 메소드(*static method*)라 부릅니다.
<!--This `new` function creates a new, empty string-->
이 `new` 함수는 새로운 빈 스트링을 만듭니다.
<!--You’ll find a `new` function on many types, because it’s a common name for a function that makes a new value of some kind. -->
당신은 `new` 함수를 많은 유형에서 찾아 볼 수 있을 것인데, 왜냐하면, 그것은 어떤 종류의 새로운 값을 만드는 함수의 일반적인 이름이기 때문입니다.
<!--To summarize, the `let mut guess = String::new();` line has created a mutable variable that is currently bound to a new, empty instance of a `String`-->
요약하면 `let mut guess = String :: new ();` 줄은 현재 `String`의 비어있는 새 인스턴스에 바인딩 된 변할 수 있는 변수를 생성했습니다.
<!--Whew!  -->
우!
<!--Recall that we included the input/output functionality from the standard library with `use std::io;` on the first line of the program-->
프로그램의 첫 번째 줄에 `use std :: io;` 를 사용하여 표준 라이브러리의 입력 / 출력 기능성을 포함했음을 기억하십시오.
<!--Now we’ll call the `stdin` function from the `io` module: -->
이제 우리는 `io` 모듈의 `stdin` 기능을 호출할 것입니다.

```rust,ignore
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/listing-02-01/src/main.rs:read}} 
```

<!--If we hadn’t put the `use std::io` line at the beginning of the program, we could have written this function call as `std::io::stdin`-->
만약 우리가 프로그램 시작 부분에 `use std :: io` 줄을 넣지 않았다면, 우리는 이 함수 호출을 `std :: io :: stdin`으로 작성할 수 있습니다.
<!--The `stdin` function returns an instance of [`std::io::Stdin`][iostdin], which is a type that represents a handle to the standard input for your terminal.  -->
`stdin` 함수는 터미널의 표준 입력에 대한 조작을 나타내는 타입 인 [`std :: io :: Stdin`] [iostdin]의 인스턴스를 반환합니다.
[iostdin]: ../std/io/struct.Stdin.html

<!--The next part of the code, `.read_line(&mut guess)`, calls the [`read_line`][read_line] method on the standard input handle to get input from the user-->
코드의 다음 부분인 `.read_line(&mut guess)`는 사용자로 부터 입력을 다루기 위한 표준 입력 메소드인 [`read_line`][read_line]을 호출합니다.
<!--We’re also passing one argument to `read_line`: `&mut guess`. -->
우리는 또한, `read_line`: `&mut guess` 에 하나의 인자(argument)를 보낼 수 있습니다.
[read_line]: ../std/io/struct.Stdin.html#method.read_line  

<!--The job of `read_line` is to take whatever the user types into standard input and append that into a string (without overwriting its contents), so it takes that string as an argument-->
`read_line`의 역할은 사용자가 입력하는 모든 것을 표준 입력으로 가져와 문자열에 추가하여 (내용을 덮어 쓰지 않고) 해당 문자열을 인자로 가지는 것입니다.
<!--The string argument needs to be mutable so the method can change the string’s content by adding the user input.  -->
그 문자열 인자는 메소드가 사용자 입력을 추가하여 문자열의 내용을 변경할 수 있도록 변경 가능할 필요가 있습니다.
<!--The `&` indicates that this argument is a *reference*, which gives you a way to let multiple parts of your code access one piece of data without needing to copy that data into memory multiple times-->
`&`는 이 인수가 참조(*reference*)임을 나타내는데, 그것은 당신에게 해당 데이터를 메모리를 여러 번 복사 할 필요없이 당신의 코드의 여러 부분이 하나의 데이터에 액세스 할 수 있습니다.
<!--References are a complex feature, and one of Rust’s major advantages is how safe and easy it is to use references-->
참조는 복잡한 특징을 가지는데, Rust의 주요 장점 중 하나는 참조를 사용하는 것이 얼마나 안전하고 쉬운지 입니다.
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
<!--Now let’s discuss what this line does. -->
 
<!--As mentioned earlier, `read_line` puts what the user types into the string we’re passing it, but it also returns a value—in this case, an [`io::Result`][ioresult]-->
<!--Rust has a number of types named `Result` in its standard library: a generic [`Result`][result]as well as specific versions for submodules, such as `io::Result`.  -->
[ioresult]: ../std/io/type.Result.html 
[result]: ../std/result/enum.Result.html 
 
<!--The `Result` types are [*enumerations*][enums]<!-- ignore -->, often referred to as *enums*-->
<!--An enumeration is a type that can have a fixed set of values, and those values are called the enum’s *variants*-->
<!--Chapter 6 will cover enums in more detail. -->
 
[enums]: ch06-00-enums.html 
 
<!--For `Result`, the variants are `Ok` or `Err`-->
<!--The `Ok` variant indicates the operation was successful, and inside `Ok` is the successfully generated value-->
<!--The `Err` variant means the operation failed, and `Err` contains information about how or why the operation failed. -->
 
<!--The purpose of these `Result` types is to encode error-handling information-->
<!--Values of the `Result` type, like values of any type, have methods defined on them-->
<!--An instance of `io::Result` has an [`expect` method][expect] that you can call-->
<!--If this instance of `io::Result` is an `Err` value, `expect` will cause the program to crash and display the message that you passed as an argument to `expect`-->
<!--If the `read_line` method returns an `Err`, it would likely be the result of an error coming from the underlying operating system-->
<!--If this instance of `io::Result` is an `Ok` value, `expect` will take the return value that `Ok` is holding and return just that value to you so you can use it-->
<!--In this case, that value is the number of bytes in what the user entered into standard input. -->
 
[expect]: ../std/result/enum.Result.html#method.expect 
 
<!--If you don’t call `expect`, the program will compile, but you’ll get a warning:  -->

```console 
{{#include ../listings/ch02-guessing-game-tutorial/no-listing-02-without-expect/output.txt}} 
``` 
 
<!--Rust warns that you haven’t used the `Result` value returned from `read_line`, indicating that the program hasn’t handled a possible error.  -->
<!--The right way to suppress the warning is to actually write error handling, but because you just want to crash this program when a problem occurs, you can use `expect`-->
<!--You’ll learn about recovering from errors in Chapter 9.  -->
<!--### Printing Values with `println!` Placeholders -->
 
<!--Aside from the closing curly bracket, there’s only one more line to discuss in the code added so far, which is the following: -->
 
```rust,ignore 
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/listing-02-01/src/main.rs:print_guess}} 
``` 
 
<!--This line prints the string we saved the user’s input in-->
<!--The set of curly brackets, `{}`, is a placeholder: think of `{}` as little crab pincers that hold a value in place-->
<!--You can print more than one value using curly brackets: the first set of curly brackets holds the first value listed after the format string, the second set holds the second value, and so on-->
<!--Printing multiple values in one call to `println!` would look like this: -->
 
```rust 
let x = 5; 
let y = 10; 
 
println!("x = {} and y = {}", x, y); 
``` 
 
<!--This code would print `x = 5 and y = 10`. -->
 
<!--### Testing the First Part -->
 
<!--Let’s test the first part of the guessing game-->
<!--Run it using `cargo run`:  -->
<!-- manual-regeneration 
cd listings/ch02-guessing-game-tutorial/listing-02-01/ 
cargo clean 
cargo run 
input 6 --> 
 
```console 
$ cargo run 
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)     Finished dev [unoptimized + debuginfo] target(s) in 6.44s      Running `target/debug/guessing_game` 
Guess the number!
Please input your guess.
6 
You guessed: 6
``` 
 
<!--At this point, the first part of the game is done: we’re getting input from the keyboard and then printing it. -->
 
<!--## Generating a Secret Number -->
 
<!--Next, we need to generate a secret number that the user will try to guess-->
<!--The secret number should be different every time so the game is fun to play more than once-->
<!--Let’s use a random number between 1 and 100 so the game isn’t too difficult-->
<!--Rust doesn’t yet include random number functionality in its standard library-->
<!--However, the Rust team does provide a [`rand` crate][randcrate].  -->
[randcrate]: https://crates.io/crates/rand 
 
<!--### Using a Crate to Get More Functionality -->
 
<!--Remember that a crate is a collection of Rust source code files-->
<!--The project we’ve been building is a *binary crate*, which is an executable-->
<!--The `rand` crate is a *library crate*, which contains code intended to be used in other programs. -->
 
<!--Cargo’s use of external crates is where it really shines-->
<!--Before we can write code that uses `rand`, we need to modify the *Cargo.toml* file to include the `rand` crate as a dependency-->
<!--Open that file now and add the following line to the bottom beneath the `[dependencies]` section header that Cargo created for you-->
<!--Be sure to specify `rand` exactly as we have here, or the code examples in this tutorial may not work. -->
 
<!-- When updating the version of `rand` used, also update the version of `rand` used in these files so they all match: 
<!--* ch07-04-bringing-paths-into-scope-with-the-use-keyword.md * ch14-03-cargo-workspaces.md -->
 
<span class="filename">Filename: Cargo.toml</span> 
 
```toml 
{{#include ../listings/ch02-guessing-game-tutorial/listing-02-02/Cargo.toml:9:}}
``` 
 
<!--In the *Cargo.toml* file, everything that follows a header is part of a section that continues until another section starts-->
<!--The `[dependencies]` section is where you tell Cargo which external crates your project depends on and which versions of those crates you require-->
<!--In this case, we’ll specify the `rand` crate with the semantic version specifier `0.8.3`-->
<!--Cargo understands [Semantic Versioning][semver](sometimes called *SemVer*), which is a standard for writing version numbers-->
<!--The number `0.8.3` is actually shorthand for `^0.8.3`, which means any version that is at least `0.8.3` but below `0.9.0`-->
<!--Cargo considers these versions to have public APIs compatible with version `0.8.3`, and this specification ensures you'll get the latest patch release that will still compile with the code in this chapter-->
<!--Any version `0.9.0` or greater is not guaranteed to have the same API as what the following examples use. -->
 
[semver]: http://semver.org 
 
<!--Now, without changing any of the code, let’s build the project, as shown in Listing 2-2. -->
 
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
 
<!--Now that we have an external dependency, Cargo fetches the latest versions of everything from the *registry*, which is a copy of data from [Crates.io][cratesio]-->
<!--Crates.io is where people in the Rust ecosystem post their open source Rust projects for others to use. -->
 
[cratesio]: https://crates.io/ 
 
<!--After updating the registry, Cargo checks the `[dependencies]` section and downloads any crates you don’t have yet-->
<!--In this case, although we only listed `rand` as a dependency, Cargo also grabbed other crates that `rand` depends on to work-->
<!--After downloading the crates, Rust compiles them and then compiles the project with the dependencies available. -->
 
<!--If you immediately run `cargo build` again without making any changes, you won’t get any output aside from the `Finished` line-->
<!--Cargo knows it has already downloaded and compiled the dependencies, and you haven’t changed anything about them in your *Cargo.toml* file-->
<!--Cargo also knows that you haven’t changed anything about your code, so it doesn’t recompile that either-->
<!--With nothing to do, it simply exits. -->
 
<!--If you open up the *src/main.rs* file, make a trivial change, and then save it and build again, you’ll only see two lines of output: -->
 
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
<!--Your dependencies haven’t changed, so Cargo knows it can reuse what it has already downloaded and compiled for those-->
<!--It just rebuilds your part of the code. -->
 
<!--#### Ensuring Reproducible Builds with the *Cargo.lock* File  -->
<!--Cargo has a mechanism that ensures you can rebuild the same artifact every time you or anyone else builds your code: Cargo will use only the versions of the dependencies you specified until you indicate otherwise-->
<!--For example, what happens if next week version 0.8.4 of the `rand` crate comes out and contains an important bug fix but also contains a regression that will break your code? -->
 
<!--The answer to this problem is the *Cargo.lock* file, which was created the first time you ran `cargo build` and is now in your *guessing_game* directory-->
<!--When you build a project for the first time, Cargo figures out all the versions of the dependencies that fit the criteria and then writes them to the *Cargo.lock* file-->
<!--When you build your project in the future, Cargo will see that the *Cargo.lock* file exists and use the versions specified there rather than doing all the work of figuring out versions again-->
<!--This lets you have a reproducible build automatically-->
<!--In other words, your project will remain at `0.8.3` until you explicitly upgrade, thanks to the *Cargo.lock* file. -->
 
<!--#### Updating a Crate to Get a New Version -->
#### 새로운 버전을 가져오기 위해 업데이트하기
 
<!--When you *do* want to update a crate, Cargo provides another command, `update`, which will ignore the *Cargo.lock* file and figure out all the latest versions that fit your specifications in *Cargo.toml*-->

<!--If that works, Cargo will write those versions to the *Cargo.lock* file. -->
 
<!--But by default, Cargo will only look for versions greater than `0.8.3` and less than `0.9.0`-->


<!--If the `rand` crate has released two new versions, `0.8.4` and `0.9.0`, you would see the following if you ran `cargo update`:  -->

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

<!--If you wanted to use `rand` version `0.9.0` or any version in the `0.9.x` series, you’d have to update the *Cargo.toml* file to look like this instead:  -->


```toml 
[dependencies] 
rand = "0.9.0" 
``` 
 
<!--The next time you run `cargo build`, Cargo will update the registry of crates available and reevaluate your `rand` requirements according to the new version you have specified. -->
 
<!--There’s a lot more to say about [Cargo][doccargo] and [its ecosystem][doccratesio] which we’ll discuss in Chapter 14, but for now, that’s all you need to know-->

<!--Cargo makes it very easy to reuse libraries, so Rustaceans are able to write smaller projects that are assembled from a number of packages. -->
 
[doccargo]: http://doc.crates.io 
[doccratesio]: http://doc.crates.io/crates-io.html 
 
<!--### Generating a Random Number -->
 
<!--Now that you’ve added the `rand` crate to *Cargo.toml*, let’s start using `rand`-->

<!--The next step is to update *src/main.rs*, as shown in Listing 2-3.  -->

<span class="filename">Filename: src/main.rs</span> 
 
```rust,ignore 
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/listing-02-03/src/main.rs:all}} 
``` 
 
<span class="caption">Listing 2-3: Adding code to generate a random number</span> 
 
<!--First, we add a `use` line: `use rand::Rng`-->

<!--The `Rng` trait defines methods that random number generators implement, and this trait must be in scope for us to use those methods-->

<!--Chapter 10 will cover traits in detail.  -->

<!--Next, we’re adding two lines in the middle-->

<!--The `rand::thread_rng` function will give us the particular random number generator that we’re going to use: one that is local to the current thread of execution and seeded by the operating system-->

<!--Then we call the `gen_range` method on the random number generator-->

<!--This method is defined by the `Rng` trait that we brought into scope with the `use rand::Rng` statement-->

<!--The `gen_range` method takes a range expression as an argument and generates a random number in the range-->

<!--The kind of range expression we’re using here takes the form `start..end`-->

<!--It’s inclusive on the lower bound but exclusive on the upper bound, so we need to specify `1..101` to request a number between 1 and 100-->

<!--Alternatively, we could pass the range `1..=100`, which is equivalent. -->
 
<!--> Note: You won’t just know which traits to use and which methods and functions > to call from a crate-->

<!--Instructions for using a crate are in each crate’s > documentation-->

<!--Another neat feature of Cargo is that you can run the `cargo > doc --open` command, which will build documentation provided by all of your > dependencies locally and open it in your browser-->

<!--If you’re interested in > other functionality in the `rand` crate, for example, run `cargo doc --open` > and click `rand` in the sidebar on the left. -->
 
<!--The second line that we added to the middle of the code prints the secret number-->

<!--This is useful while we’re developing the program to be able to test it, but we’ll delete it from the final version-->

<!--It’s not much of a game if the program prints the answer as soon as it starts! -->
 
<!--Try running the program a few times: -->
 
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

<!--Great job! -->
 
<!--## Comparing the Guess to the Secret Number -->
 
<!--Now that we have user input and a random number, we can compare them-->

<!--That step is shown in Listing 2-4-->

<!--Note that this code won’t compile quite yet, as we will explain. -->
 
<span class="filename">Filename: src/main.rs</span> 
 
```rust,ignore,does_not_compile 
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/listing-02-04/src/main.rs:here}} 
``` 
 
<span class="caption">Listing 2-4: Handling the possible return values of comparing two numbers</span> 
 
<!--The first new bit here is another `use` statement, bringing a type called `std::cmp::Ordering` into scope from the standard library-->

<!--Like `Result`, `Ordering` is another enum, but the variants for `Ordering` are `Less`, `Greater`, and `Equal`-->

<!--These are the three outcomes that are possible when you compare two values. -->
 
<!--Then we add five new lines at the bottom that use the `Ordering` type-->

<!--The `cmp` method compares two values and can be called on anything that can be compared-->

<!--It takes a reference to whatever you want to compare with: here it’s comparing the `guess` to the `secret_number`-->

<!--Then it returns a variant of the `Ordering` enum we brought into scope with the `use` statement-->

<!--We use a [`match`][match]expression to decide what to do next based on which variant of `Ordering` was returned from the call to `cmp` with the values in `guess` and `secret_number`. -->
 
[match]: ch06-02-match.html 
 
<!--A `match` expression is made up of *arms*-->

<!--An arm consists of a *pattern* and the code that should be run if the value given to the beginning of the `match` expression fits that arm’s pattern-->

<!--Rust takes the value given to `match` and looks through each arm’s pattern in turn-->

<!--The `match` construct and patterns are powerful features in Rust that let you express a variety of situations your code might encounter and make sure that you handle them all-->

<!--These features will be covered in detail in Chapter 6 and Chapter 18, respectively.  -->

<!--Let’s walk through an example of what would happen with the `match` expression used here-->

<!--Say that the user has guessed 50 and the randomly generated secret number this time is 38-->

<!--When the code compares 50 to 38, the `cmp` method will return `Ordering::Greater`, because 50 is greater than 38-->

<!--The `match` expression gets the `Ordering::Greater` value and starts checking each arm’s pattern-->

<!--It looks at the first arm’s pattern, `Ordering::Less`, and sees that the value `Ordering::Greater` does not match `Ordering::Less`, so it ignores the code in that arm and moves to the next arm-->

<!--The next arm’s pattern, `Ordering::Greater`, *does* match `Ordering::Greater`! The associated code in that arm will execute and print `Too big!` to the screen-->

<!--The `match` expression ends because it has no need to look at the last arm in this scenario.  -->

<!--However, the code in Listing 2-4 won’t compile yet-->

<!--Let’s try it:  -->

```console 
{{#include ../listings/ch02-guessing-game-tutorial/listing-02-04/output.txt}}
``` 

<!--The core of the error states that there are *mismatched types*-->

<!--Rust has a strong, static type system-->

<!--However, it also has type inference-->

<!--When we wrote `let mut guess = String::new()`, Rust was able to infer that `guess` should be a `String` and didn’t make us write the type-->

<!--The `secret_number`, on the other hand, is a number type-->

<!--A few number types can have a value between 1 and 100: `i32`, a 32-bit number; `u32`, an unsigned 32-bit number; `i64`, a 64-bit number; as well as others-->

<!--Rust defaults to an `i32`, which is the type of `secret_number` unless you add type information elsewhere that would cause Rust to infer a different numerical type-->

<!--The reason for the error is that Rust cannot compare a string and a number type. -->
 
<!--Ultimately, we want to convert the `String` the program reads as input into a real number type so we can compare it numerically to the secret number-->

<!--We can do that by adding another line to the `main` function body:-->

<span class="filename">Filename: src/main.rs</span> 
 
```rust,ignore 
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/no-listing-03-convert-string-to-number/src/main.rs:here}} 
``` 
 
<!--The line is: -->
 
```rust,ignore 
let guess: u32 = guess.trim().parse().expect("Please type a number!");
``` 
 
<!--We create a variable named `guess`-->

<!--But wait, doesn’t the program already have a variable named `guess`? It does, but Rust allows us to *shadow* the previous value of `guess` with a new one-->

<!--This feature is often used in situations in which you want to convert a value from one type to another type-->

<!--Shadowing lets us reuse the `guess` variable name rather than forcing us to create two unique variables, such as `guess_str` and `guess` for example. (Chapter 3 covers shadowing in more detail.) -->
 
<!--We bind `guess` to the expression `guess.trim().parse()`-->

<!--The `guess` in the expression refers to the original `guess` that was a `String` with the input in it-->

<!--The `trim` method on a `String` instance will eliminate any whitespace at the beginning and end-->

<!--Although `u32` can contain only numerical characters, the user must press <span class="keystroke">enter</span> to satisfy `read_line`-->

<!--When the user presses <span class="keystroke">enter</span>, a newline character is added to the string-->

<!--For example, if the user types <span class="keystroke">5</span> and presses <span class="keystroke">enter</span>, `guess` looks like this: `5\n`-->

<!--The `\n` represents “newline,” the result of pressing <span class="keystroke">enter</span>-->

<!--The `trim` method eliminates `\n`, resulting in just `5`. -->
 
<!--The [`parse` method on strings][parse]<!-- ignore --> parses a string into some kind of number-->

<!--Because this method can parse a variety of number types, we need to tell Rust the exact number type we want by using `let guess: u32`-->

<!--The colon (`:`) after `guess` tells Rust we’ll annotate the variable’s type-->

<!--Rust has a few built-in number types; the `u32` seen here is an unsigned, 32-bit integer-->

<!--It’s a good default choice for a small positive number-->

<!--You’ll learn about other number types in Chapter 3-->

<!--Additionally, the `u32` annotation in this example program and the comparison with `secret_number` means that Rust will infer that `secret_number` should be a `u32` as well-->

<!--So now the comparison will be between two values of the same type!-->

[parse]: ../std/primitive.str.html#method.parse 
 
<!--The call to `parse` could easily cause an error-->

<!--If, for example, the string contained `A👍%`, there would be no way to convert that to a number-->

<!--Because it might fail, the `parse` method returns a `Result` type, much as the `read_line` method does (discussed earlier in [“Handling Potential Failure with the `Result` Type”](#handling-potential-failure-with-the-result-type))-->

<!--We’ll treat this `Result` the same way by using the `expect` method again-->

<!--If `parse` returns an `Err` `Result` variant because it couldn’t create a number from the string, the `expect` call will crash the game and print the message we give it-->

<!--If `parse` can successfully convert the string to a number, it will return the `Ok` variant of `Result`, and `expect` will return the number that we want from the `Ok` value. -->
 
<!--Let’s run the program now! -->
 
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
 
<!--Nice! Even though spaces were added before the guess, the program still figured out that the user guessed 76-->

<!--Run the program a few times to verify the different behavior with different kinds of input: guess the number correctly, guess a number that is too high, and guess a number that is too low.  -->

<!--We have most of the game working now, but the user can make only one guess-->
<!--Let’s change that by adding a loop! -->
 
<!--## Allowing Multiple Guesses with Looping -->
 
<!--The `loop` keyword creates an infinite loop-->

<!--We’ll add that now to give users more chances at guessing the number: -->
 
<span class="filename">Filename: src/main.rs</span> 
 
```rust,ignore 
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/no-listing-04-looping/src/main.rs:here}} 
``` 
 
<!--As you can see, we’ve moved everything into a loop from the guess input prompt onward-->

<!--Be sure to indent the lines inside the loop another four spaces each and run the program again-->

<!--Notice that there is a new problem because the program is doing exactly what we told it to do: ask for another guess forever! It doesn’t seem like the user can quit! -->
 
<!--The user could always interrupt the program by using the keyboard shortcut <span class="keystroke">ctrl-c</span>-->

<!--But there’s another way to escape this insatiable monster, as mentioned in the `parse` discussion in [“Comparing the Guess to the Secret Number”](#comparing-the-guess-to-the-secret-number): if the user enters a non-number answer, the program will crash-->

<!--The user can take advantage of that in order to quit, as shown here:  -->

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

<!--However, this is suboptimal to say the least-->

<!--We want the game to automatically stop when the correct number is guessed. -->
 
<!--### Quitting After a Correct Guess -->
 
<!--Let’s program the game to quit when the user wins by adding a `break` statement:  -->


<span class="filename">Filename: src/main.rs</span> 
 
```rust,ignore 
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/no-listing-05-quitting/src/main.rs:here}} 
``` 
 
<!--Adding the `break` line after `You win!` makes the program exit the loop when the user guesses the secret number correctly-->

<!--Exiting the loop also means exiting the program, because the loop is the last part of `main`.  -->

<!--### Handling Invalid Input -->
 
<!--To further refine the game’s behavior, rather than crashing the program when the user inputs a non-number, let’s make the game ignore a non-number so the user can continue guessing-->

<!--We can do that by altering the line where `guess` is converted from a `String` to a `u32`, as shown in Listing 2-5.  -->


<span class="filename">Filename: src/main.rs</span> 
 
```rust,ignore 
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/listing-02-05/src/main.rs:here}} 
``` 
 
<span class="caption">Listing 2-5: Ignoring a non-number guess and asking for another guess instead of crashing the program</span> 
 
<!--Switching from an `expect` call to a `match` expression is how you generally move from crashing on an error to handling the error-->

<!--Remember that `parse` returns a `Result` type and `Result` is an enum that has the variants `Ok` or `Err`-->

<!--We’re using a `match` expression here, as we did with the `Ordering` result of the `cmp` method. -->
 
<!--If `parse` is able to successfully turn the string into a number, it will return an `Ok` value that contains the resulting number-->

<!--That `Ok` value will match the first arm’s pattern, and the `match` expression will just return the `num` value that `parse` produced and put inside the `Ok` value-->

<!--That number will end up right where we want it in the new `guess` variable we’re creating.  -->

<!--If `parse` is *not* able to turn the string into a number, it will return an `Err` value that contains more information about the error-->

<!--The `Err` value does not match the `Ok(num)` pattern in the first `match` arm, but it does match the `Err(_)` pattern in the second arm-->

<!--The underscore, `_`, is a catchall value; in this example, we’re saying we want to match all `Err` values, no matter what information they have inside them-->

<!--So the program will execute the second arm’s code, `continue`, which tells the program to go to the next iteration of the `loop` and ask for another guess-->

<!--So, effectively, the program ignores all errors that `parse` might encounter!-->

<!--Now everything in the program should work as expected-->

<!--Let’s try it:  -->

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
 
<!--Awesome! With one tiny final tweak, we will finish the guessing game-->

<!--Recall that the program is still printing the secret number-->

<!--That worked well for testing, but it ruins the game-->

<!--Let’s delete the `println!` that outputs the secret number-->

<!--Listing 2-6 shows the final code. -->

<span class="filename">Filename: src/main.rs</span> 
 
```rust,ignore 
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/listing-02-06/src/main.rs}} 
``` 
 
<span class="caption">Listing 2-6: Complete guessing game code</span>  

<!--## Summary -->
## 요약
 
<!--At this point, you’ve successfully built the guessing game-->

<!--Congratulations!  -->

<!--This project was a hands-on way to introduce you to many new Rust concepts: `let`, `match`, methods, associated functions, the use of external crates, and more-->

<!--In the next few chapters, you’ll learn about these concepts in more detail-->

<!--Chapter 3 covers concepts that most programming languages have, such as variables, data types, and functions, and shows how to use them in Rust-->

<!--Chapter 4 explores ownership, a feature that makes Rust different from other languages-->

<!--Chapter 5 discusses structs and method syntax, and Chapter 6 explains how enums work. -->
 
[variables-and-mutability]: 

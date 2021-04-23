<!--## Appendix A: Keywords -->
## 부록 A: 키워드
 
<!--The following list contains keywords that are reserved for current or future use by the Rust language-->
아래의 목록은 러스트에서 사용할 키워드입니다.
<!--As such, they cannot be used as identifiers (except as raw identifiers as we’ll discuss in the “[Raw Identifiers][raw-identifiers]” section), including names of functions, variables, parameters, struct fields, modules, crates, constants, macros, static values, attributes, types, traits, or lifetimes.-->
따라서 아래의 키워드들은 함수, 변수, 파라미터, 구조체 필드, 모듈, 크레이트, 상수, 매크로, 정적 변수, 속성, 타입, 트레잇, 라이프타임의 이름으로 사용할 수 없습니다. (아래에서 논의할 로우(raw) 식별자가 붙은 경우는 제외됩니다.)

[raw-identifiers]: #raw-identifiers 
 
<!--### Keywords Currently in Use -->
 ### 현재 사용되고 있는 키워드
 
<!--The following keywords currently have the functionality described.  -->
아래의 키워드들은 다음과 같은 기능으로 사용되고 있습니다.

<!-- * `as` - perform primitive casting, disambiguate the specific trait containing an item, or rename items in `use` and `extern crate` statements-->
* `as` - 형변환을 수행하고, 항목을 포함하는 특정 트레잇을 명확하게 하거나,`use` 및`extern crate` 구문에서 항목 이름을 바꿉니다.
<!-- * `async` - return a `Future` instead of blocking the current thread -->
* `async` - 현재 스레드를 차단하는 대신 'Future'를 반환합니다.
<!--* `await` - suspend execution until the result of a `Future` is ready -->
* `await` - 'Future'이 준비될 때까지 실행을 중지합니다.
<!--* `break` - exit a loop immediately -->
* `break` - 루프를 바로 빠져나갑니다.
<!--* `const` - define constant items or constant raw pointers -->
* `const` - 상수 또는 상수 로우 포인터 정의합니다.
<!-- * `continue` - continue to the next loop iteration -->
* `continue` - 다음 반복 루프로 넘어갑니다.
<!--* `crate` - link an external crate or a macro variable representing the crate in which the macro is defined -->
* `crate` - 외부 크레이트나 크레이트를 대표하는 매크로 변수를 링크합니다.
<!--* `dyn` - dynamic dispatch to a trait object -->
* `dyn` - 
<!--* `else` - fallback for `if` and `if let` control flow constructs  -->
* `else` - `if`와 `if let` 에서 제외된 경우를 나타낼 때 사용합니다.
<!--* `enum` - define an enumeration -->
* `enum` - 
<!--* `extern` - link an external crate, function, or variable -->
* `extern` -
<!--* `false` - Boolean false literal -->
* `false` -
<!--* `fn` - define a function or the function pointer type -->
* `fn` - 함수나 함수 포인터 타입을 정의합니다.
<!--* `for` - loop over items from an iterator, implement a trait, or specify a   higher-ranked lifetime -->
* `for` - 반복자의 항목을 반복하거나, 트레잇을 구현하거나, 더 높은 수준의 라이프타임을 명시합니다.
<!--* `if` - branch based on the result of a conditional expression -->
* `if` -
<!--* `impl` - implement inherent or trait functionality -->
* `impl` -
<!--* `in` - part of `for` loop syntax -->
* `in` - `for`루프 문법의 일부로 사용합니다.
<!--* `let` - bind a variable -->
* `let` -
<!--* `loop` - loop unconditionally -->
* `loop` -
<!--* `match` - match a value to patterns -->
* `match` -
<!--* `mod` - define a module -->
* `mod` - 모듈을 정의합니다.
<!--* `move` - make a closure take ownership of all its captures -->
* `move` - 
<!--* `mut` - denote mutability in references, raw pointers, or pattern bindings -->
* `mut` -
<!--* `pub` - denote public visibility in struct fields, `impl` blocks, or modules -->
* `pub` -
<!--* `ref` - bind by reference -->
* `ref` - 레퍼런스로 바인딩합니다.
<!--* `return` - return from function -->
* `return` - 함수로부터 결과를 반환합니다.
<!--* `Self` - a type alias for the type we are defining or implementing -->
* `Self` -
<!--* `self` - method subject or current module -->
* `self` - 
<!--* `static` - global variable or lifetime lasting the entire program execution -->
* `static` -
<!--* `struct` - define a structure -->
* `struct` - 구조체를 정의합니다.
<!--* `super` - parent module of the current module -->
* `super` -
<!--* `trait` - define a trait -->
* `trait` - 트레잇을 정의합니다.
<!--* `true` - Boolean true literal -->
* `true` - 불리언 타입의 True를 선언합니다.
<!--* `type` - define a type alias or associated type -->
* `type` - 
<!--* `union` - define a [union] and is only a keyword when used in a union declaration -->
* `union` -
<!--* `unsafe` - denote unsafe code, functions, traits, or implementations -->
* `unsafe` -
<!--* `use` - bring symbols into scope -->
* `use` -
<!--* `where` - denote clauses that constrain a type -->
* `where` -
<!--* `while` - loop conditionally based on the result of an expression -->
* `while` -

[union]: ../reference/items/unions.html 
 
<!--### Keywords Reserved for Future Use -->
 ### 미래에 사용하기 위해 예약한 키워드
 
<!--The following keywords do not have any functionality but are reserved by Rust for potential future use. -->
아래의 키워드들은 아직 기능은 정해지지 않았지만 미래에 새로운 기능을 추가할 때 사용하기 위해 예약한 단어들입니다.

* `abstract`
* `become`
* `box`
* `do`
* `final`
* `macro`
* `override`
* `priv`
* `try`
* `typeof`
* `unsized`
* `virtual`
* `yield`
 
<!--### Raw Identifiers -->
### 로우(raw) 식별자
 
<!--*Raw identifiers* are the syntax that lets you use keywords where they wouldn’t normally be allowed-->
로우(raw) 식별자는 일반적으로 허락되지 않은 키워드들을 사용할 수 있도록 해주는 문법입니다.
<!--You use a raw identifier by prefixing a keyword with `r#`.  -->
`#r`는 로우(raw) 식별자의 앞 글자를 의미하며, 사용하려는 키워드 앞에 붙여 사용할 수 있습니다.
<!--For example, `match` is a keyword-->
예를 들어, `match`는 키워드입니다.
<!--If you try to compile the following function that uses `match` as its name: -->
 그렇기에 만약 아래의 예시처럼 `match`라는 이름을 사용하여 함수를 정의하려고 한다면
 
<span class="filename">Filename: src/main.rs</span> 
 
```rust,ignore,does_not_compile 
fn match(needle: &str, haystack: &str) -> bool { 
    haystack.contains(needle) 
} 
``` 
<!--you’ll get this error: -->
 아래와 같은 오류가 발생합니다.

```text 
error: expected identifier, found keyword `match` 
 --> src/main.rs:4:4 
  | 
4 | fn match(needle: &str, haystack: &str) -> bool { 
  |    ^^^^^ expected identifier, found keyword 
``` 
<!--The error shows that you can’t use the keyword `match` as the function identifier-->
위 에러는 `match`라는 키워드를 함수 이름으로 사용할 수 없다고 설명합니다.
<!--To use `match` as a function name, you need to use the raw identifier syntax, like this: -->
 `match`를 함수 이름을 사용하기 위해서는 아래와 같이 로우(raw) 식별자 문법을 사용해야 합니다.
 
<span class="filename">Filename: src/main.rs</span> 
 
```rust 
fn r#match(needle: &str, haystack: &str) -> bool { 
    haystack.contains(needle) 
} 
 
fn main() { 
    assert!(r#match("foo", "foobar")); 
} 
``` 
<!--This code will compile without any errors-->
위 코드는 오류 없이 컴파일 될 것입니다.
<!--Note the `r#` prefix on the function name in its definition as well as where the function is called in `main`.  -->
`main` 함수에서도 이름 앞에 `r#` 접두사가 붙는다는 것을 기억하세요.
<!--Raw identifiers allow you to use any word you choose as an identifier, even if that word happens to be a reserved keyword-->
로우(raw) 식별자를 사용하면 예비 키워드를 포함한 어떤 키워드도 이름으로 선택할 수 있습니다.
<!--In addition, raw identifiers allow you to use libraries written in a different Rust edition than your crate uses-->
게다가, 로우(raw) 식별자는 러스트의 다른 버전에서 생성된 라이브러리도 사용할 수 있게 도와줍니다.
<!--For example, `try` isn’t a keyword in the 2015 edition but is in the 2018 edition-->
예를 들어, `try`는 2015년 버전에서는 키워드가 아니었지만, 2018년도에서는 키워드가 되었다고 가정합시다.
<!--If you depend on a library that’s written using the 2015 edition and has a `try` function, you’ll need to use the raw identifier syntax, `r#try` in this case, to call that function from your 2018 edition code-->
만약 2015 버전에서 만들어진 라이브러리 내부 코드에 `try` 함수가 있다면, 2018년 버전에서는 `r#try`로 사용해야 합니다.
<!--See [Appendix E][appendix-e] for more information on editions.  -->
러스트 버전에 대해 자세히 알고 싶다면 [부록 E][appendix-e]를 참고하세요.

[appendix-e]: appendix-05-editions.html 

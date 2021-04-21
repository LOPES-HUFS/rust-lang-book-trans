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
* `async` - 
<!--* `await` - suspend execution until the result of a `Future` is ready -->
* `await` -
<!--* `break` - exit a loop immediately -->
* `break` - 
<!--* `const` - define constant items or constant raw pointers -->
* `const` - 상수 또는  상수 로우 포인터 정의합니다.
<!-- * `continue` - continue to the next loop iteration -->
* `continue` - 다음 반복 루프로 넘어갑니다.
<!--* `crate` - link an external crate or a macro variable representing the crate in which the macro is defined -->
* `crate`
<!--* `dyn` - dynamic dispatch to a trait object -->
<!--* `else` - fallback for `if` and `if let` control flow constructs  -->
<!--* `enum` - define an enumeration -->
<!--* `extern` - link an external crate, function, or variable -->
<!--* `false` - Boolean false literal -->
<!--* `fn` - define a function or the function pointer type -->
<!--* `for` - loop over items from an iterator, implement a trait, or specify a   higher-ranked lifetime -->
<!--* `if` - branch based on the result of a conditional expression -->
<!--* `impl` - implement inherent or trait functionality -->
<!--* `in` - part of `for` loop syntax -->
<!--* `let` - bind a variable -->
<!--* `loop` - loop unconditionally -->
<!--* `match` - match a value to patterns -->
<!--* `mod` - define a module -->
<!--* `move` - make a closure take ownership of all its captures -->
<!--* `mut` - denote mutability in references, raw pointers, or pattern bindings -->
<!--* `pub` - denote public visibility in struct fields, `impl` blocks, or modules -->
<!--* `ref` - bind by reference -->
<!--* `return` - return from function -->
<!--* `Self` - a type alias for the type we are defining or implementing -->
<!--* `self` - method subject or current module -->
<!--* `static` - global variable or lifetime lasting the entire program execution -->
<!--* `struct` - define a structure -->
<!--* `super` - parent module of the current module -->
<!--* `trait` - define a trait -->
<!--* `true` - Boolean true literal -->
<!--* `type` - define a type alias or associated type -->
<!--* `union` - define a [union] and is only a keyword when used in a union declaration -->
<!--* `unsafe` - denote unsafe code, functions, traits, or implementations * `use` - bring symbols into scope -->
<!--* `where` - denote clauses that constrain a type -->
<!--* `while` - loop conditionally based on the result of an expression  -->
[union]: ../reference/items/unions.html 
 
<!--### Keywords Reserved for Future Use -->
 ### 미래에 사용하기 위해 예약한 키워드
 
<!--The following keywords do not have any functionality but are reserved by Rust for potential future use. -->
아래의 키워드들은 아직 기능은 정해지지 않았지만 미래에 새로운 기능을 추가할 때 사용하기 위해 예약한 단어들입니다.

<!--* `abstract` -->
<!--* `become` -->
<!--* `box` -->
<!--* `do` -->
<!--* `final` -->
<!--* `macro` -->
<!--* `override` -->
<!--* `priv` -->
<!--* `try` -->
<!--* `typeof` -->
<!--* `unsized` -->
<!--* `virtual` -->
<!--* `yield` -->
 
<!--### Raw Identifiers -->
### 로우(raw) 식별자
 
<!--*Raw identifiers* are the syntax that lets you use keywords where they wouldn’t normally be allowed-->
<!--You use a raw identifier by prefixing a keyword with `r#`.  -->
<!--For example, `match` is a keyword-->
<!--If you try to compile the following function that uses `match` as its name: -->
 만약 아래의 예시처럼 `match`라는 이름을 사용하여 함수를 정의하려고 한다면
 
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
위 에러는 `match`라는 키워드를 함수 식별자로서 사용할 수 없다고 설명합니다.
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
<!--Raw identifiers allow you to use any word you choose as an identifier, even if that word happens to be a reserved keyword-->
<!--In addition, raw identifiers allow you to use libraries written in a different Rust edition than your crate uses-->
<!--For example, `try` isn’t a keyword in the 2015 edition but is in the 2018 edition-->
<!--If you depend on a library that’s written using the 2015 edition and has a `try` function, you’ll need to use the raw identifier syntax, `r#try` in this case, to call that function from your 2018 edition code-->
<!--See [Appendix E][appendix-e] for more information on editions.  -->
[appendix-e]: appendix-05-editions.html 

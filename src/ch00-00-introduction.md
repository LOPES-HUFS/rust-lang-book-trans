# Introduction

<!-- > Note: This edition of the book is the same as [The Rust Programming Language][nsprust] available in print and ebook format from [No Starch Press][nsp].-->

> 주: 이 책은 [No Starch Press][nsp]에서 ebook 형식으로 제공하는 [The Rust 
> Programming Language][nsprust]과 동일하며, 이를 한국어로 번역합니다.

[nsprust]: https://nostarch.com/rust
[nsp]: https://nostarch.com/

<!-- Welcome to *The Rust Programming Language*, an introductory book about Rust.-->
Rust(이하 러스트) 입문서인 *The Rust Programming Language*에 오신 것을 환영합니다.
<!-- The Rust programming language helps you write faster, more reliable software.-->
러스트 프로그래밍 언어는 여러분이 더 빠르고 안정적인 소프트웨어를 작성할 수 있도록 도와줍니다.
<!-- High-level ergonomics and low-level control are often at odds in programming language design; Rust challenges that conflict. -->
고수준의 사용편의성(ergonomics)과 저수준의 제어는 종종 프로그래밍 언어를 설계하는 데 있어 상충되지만; 러스트는 이런 불일치(conflict)에 도전합니다.
<!-- Through balancing powerful technical capacity and a great developer experience, Rust gives you the option to control low-level details (such as memory usage) without all the hassle traditionally associated with such control. -->
강력한 기술 능력(capacity)과 아주 멋진 개발자 경험 사이의 균형을 맞추면서도, 러스트는 여러분에게 (메모리 사용과 같은) 저수준의 제어를 이와 관련된 전통적인 모든 혼란(hassle)없이 디테일하게 제어할 수 있는 옵션을 제공합니다.

<!-- ## Who Rust Is For -->
## Rust는 누구를 위한 것인가요?

<!-- Rust is ideal for many people for a variety of reasons. -->
러스트는 다양한 이유로 많은 사람들에게 이상적입니다.
<!-- Let’s look at a few of the most important groups. -->
가장 중요한 몇몇 그룹을 살펴보겠습니다.

<!-- ### Teams of Developers -->
### 개발자 팀

<!-- Rust is proving to be a productive tool for collaborating among large teams of developers with varying levels of systems programming knowledge. -->
러스트는 다양한 수준의 시스템 프로그래밍 지식을 가지고 있는 대규모 개발자 팀들 사이에서 협업을 위한 생산적인 도구임을 입증하고 있습니다.
<!-- Low-level code is prone to a variety of subtle bugs, which in most other languages can be caught only through extensive testing and careful code review by experienced developers. -->
저수준 코드는 다양한 종류의 버그들에 취약하기 때문에, 대부분 다른 언어들은 광범위한 테스트와 숙련된 개발자의 신중한 코드 리뷰를 통해서 버그들을 잡으려고 합니다.
<!--In Rust, the compiler plays a gatekeeper role by refusing to compile code with these elusive bugs, including concurrency bugs.-->
러스트에서, 컴파일러가 동시성(concurrency) 버그와 같이 찾기 힘든 버그들을 포함하고 있는 코드들은 컴파일하는 것을 거부함으로써 문지기(gatekeeper)와 같은 역할을 수행합니다.
<!--By working alongside the compiler, the team can spend their time focusing on the program’s logic rather than chasing down bugs.-->
컴파일러를 옆에 두고 작업하기에, 팀은 버그를 쫒는 대신 프로그램의 로직에 집중하는 데 시간을 할애할 수 있습니다.

<!--Rust also brings contemporary developer tools to the systems programming world:-->
Rust는 또한 시스템 프로그래밍 세계에서 사용하는 현대적인 개발자 도구들을 제공합니다.

<!--* Cargo, the included dependency manager and build tool, makes adding,
  compiling, and managing dependencies painless and consistent across the Rust
  ecosystem.-->
* 의존성(dependency)관리 및 빌드 도구인 Cargo를 사용하여 의존성 추가, 컴파일, 관리 등을 고통없이 일관성 있게 처리할 수 있습니다.
<!--* Rustfmt ensures a consistent coding style across developers.-->
* Rustfmt는 개발자들 사이에 일관된 코딩 스타일을 보장합니다.
<!--* The Rust Language Server powers Integrated Development Environment (IDE)
  integration for code completion and inline error messages.-->
* 러스트 언어 서버(Rust Language Server)는 코드 자동완성과 인라인 에러 메시지를 통합한 개발환경(IDE)를 제공합니다.

<!--By using these and other tools in the Rust ecosystem, developers can be
productive while writing systems-level code.-->
위의 도구들과 러스트 생태계의 다른 도구들까지 사용함으로써, 개발자들은 저수준 코드를 더욱 생산적으로 작성할 수 있습니다.

<!--### Students-->
### 학생

<!--Rust is for students and those who are interested in learning about systems concepts.-->
러스트는 시스템 개념에 대해 관심있는 학생들에게도 적합합니다.
<!--Using Rust, many people have learned about topics like operating systems development.-->
많은 사람들이 러스트를 사용하여 운영체제 개발과 같은 주제들을 공부해왔습니다.
<!--The community is very welcoming and happy to answer student questions.-->
커뮤티니 또한 학생들을 환영하며, 그들의 질문에 대해 친절하게 답변합니다.
<!--Through efforts such as this book, the Rust teams want to make systems concepts more accessible to more people, especially those new to programming.-->
이 책과 같은 노력들을 통해, 러스트 팀은 더 많은 사람, 특히 프로그래밍 입문자들이 시스템 개념들에 더 쉽게 다가갈 수 있기를 바랍니다.

<!--### Companies-->
### 회사

<!--Hundreds of companies, large and small, use Rust in production for a variety of tasks.-->
회사의 규모와 상관없이 수많은 회사들이 제품 생산을 위한 다양한 작업에 러스트를 사용하고 있습니다.
<!--Those tasks include command line tools, web services, DevOps tooling, embedded devices, audio and video analysis and transcoding, cryptocurrencies, bioinformatics, search engines, Internet of Things applications, machine learning, and even major parts of the Firefox web browser.-->
그런 작업들은 커맨드 라인 도구나, 웹 서비스, 데브옵스 도구화, 임베디드 디바이스, 오디오 및 비디오 분석과 트랜스코딩, 암호화, 생물정보학, 검색 엔진, IoT 애플리케이션, 머신 러닝, 심지어 파이어폭스 웹 브라우져의 주요한 부분까지 포함합니다.

<!--### Open Source Developers-->
### 오픈 소스 개발자들

<!--Rust is for people who want to build the Rust programming language, community, developer tools, and libraries.-->
 러스트는 프로그래밍 언어, 커뮤니티, 개발자 툴, 라이브러리를 만들고자 하는 사람들에게도 적합한 언어입니다.
<!--We’d love to have you contribute to the Rust language.-->
우리는 러스트 언어 발전에 기여하는 모든 이들을 환영합니다.

<!--### People Who Value Speed and Stability-->
### 속도와 안전성을 중시하는 사람

<!--Rust is for people who crave speed and stability in a language.-->
러스트는 속도와 안전성을 중시하는 사람들에게 적합합니다.
<!--By speed, we mean the speed of the programs that you can create with Rust and the speed at which Rust lets you write them.-->
여기서 속도란, 프로그램을 러스트로 작성하는 속도와 러스트로 만들어진 프로그램의 속도 모두를 지칭합니다.
<!--The Rust compiler’s checks ensure stability through feature additions and refactoring.-->
러스트 컴파일러의 검증은 기능 추가와 리팩토링을 통해 안정성을 보장합니다.
<!--This is in contrast to the brittle legacy code in languages without these checks, which developers are often afraid to modify.-->
이것은 개발자들이 수정하길 꺼려하는 불안정한 레거시 코드를 검증하지 않는 언어들과 대조됩니다.
<!--By striving for zero-cost abstractions, higher-level features that compile to lower-level code as fast as code written manually, Rust endeavors to make safe code be fast code as well.-->
무료 추상화, 즉 직접 쓴 코드만큼 빠르게 저수준의 코드로 컴파일되는 기능을 구현하기 위해 노력함으로써, 러스트는 안전한 코드를 빠른 코드로도 만들기 위해 노력합니다.

<!--The Rust language hopes to support many other users as well; those mentioned
here are merely some of the biggest stakeholders. -->
러스트는 지금까지 언급된 분야들 이외에서도 많이 사용되기를 원합니다; 지금까지 언급된 분야들은 러스트를 사용할 수 있는 것들의 극히 일부일 뿐입니다.
<!--Overall, Rust’s greatest ambition is to eliminate the trade-offs that programmers have accepted for decades by providing safety *and* productivity, speed *and* ergonomics.--> 
전반적으로, 러스트의 가장 큰 목표는 생산성과 안전성, 속도와 사용편의성을 모두 제공함으로써 프로그래머들이 수십년동안 가져온 통념을 제거하는 것입니다.
<!--Give Rust a try and see if its choices work for you.-->
러스트를 사용해보고, 당신에게 맞는 언어인지 확인해보세요.

<!-- ## Who This Book Is For -->
## 이 책은 어떤 사람을 위한 책인가요?

<!-- This book assumes that you’ve written code in another programming language but doesn’t make any assumptions about which one. -->
이 책은 여러분이 이미 다른 프로그래밍 언어 코드를 작성해 봤다는 것을 가정하고 있지만, 그 언어가 어떤 것인지 상관하지 않습니다.
<!-- We’ve tried to make the material broadly accessible to those from a wide variety of programming backgrounds. -->
우리는 다양한 프로그래밍 배경을 가진 사람들이 광범위하게 이용할 수 있는 자료를 만들기 위해 노력했습니다.
<!-- We don’t spend a lot of time talking about what programming *is* or how to think about it. -->
우리는 프로그래밍이 무엇인지, 또는 어떻게 생각하는지에 대해 길게 설명하지 않습니다.
<!-- If you’re entirely new to programming, you would be better served by reading a book that specifically provides an introduction to programming. -->
만약 여러분이 프로그래밍을 처음으로 시작하는 거라면, 프로그래밍 입문서를 읽는 것이 더 좋은 선택일 것입니다.

<!-- ## How to Use This Book -->
## 이 책의 사용법

<!-- In general, this book assumes that you’re reading it in sequence from front to
back. -->
일반적으로, 이 책은 처음부터 끝까지 순차적으로 읽는 것을 가정합니다.

<!-- Later chapters build on concepts in earlier chapters, and earlier
chapters might not delve into details on a topic; we typically revisit the
topic in a later chapter. -->
그렇기에 이전 장에서 다뤘던 개념들이 다음 장에서도 나온다면, 우리는 세부적으로 설명하지 않습니다.
<!-- You’ll find two kinds of chapters in this book: concept chapters and project
chapters. -->
이 책은 크게 개념 챕터와 프로젝트 챕터로 나눠집니다.
<!-- In concept chapters, you’ll learn about an aspect of Rust. -->
개념 챕터에서는 기본적인 러스트 언어의 특징에 대해서 배울 것입니다.
<!-- In project chapters, we’ll build small programs together, applying what you’ve learned so far. -->
프로젝트 챕터에서는 함께 작은 프로그램들을 만들고, 배웠던 것들을 적용할 것입니다.
<!-- Chapters 2, 12, and 20 are project chapters; the rest are concept chapters. -->
2,12,20장은 프로젝트 챕터이고, 나머지는 개념 챕터입니다.
<!-- Chapter 1 explains how to install Rust, how to write a “Hello, world!” program, and how to use Cargo, Rust’s package manager and build tool.  -->
1장은 러스트를 설치하는 방법과 'Hello world' 프로그램, 러스트 패키지 매니저와 빌드 도구인 cargo에 대하여 설명합니다.
<!-- Chapter 2 is a hands-on introduction to the Rust language. Here we cover concepts at a high level, and later chapters will provide additional detail. -->
2장에서는 맛보기 정도로 러스트를 실습합니다. 여기서는 러스트의 개념들을 대략적으로 다루며, 이후 장에서 세부적인 부분들을 다룹니다.
<!-- If you want to get your hands dirty right away, Chapter 2 is the place for that. -->
만약 바로 실습을 통해서 러스트를 배우고 싶다면, 2장부터 시작하셔도 됩니다.
<!-- At first, you might even want to skip Chapter 3, which covers Rust features similar to those of other programming languages, and head straight to Chapter 4 to learn about Rust’s ownership system. -->

<!-- However, if you’re a particularly meticulous learner who prefers to learn every detail before moving on to the next, you might want to skip Chapter 2 and go straight to Chapter 3, returning to Chapter 2 when you’d like to work on a project applying the details you’ve learned. -->

<!-- Chapter 5 discusses structs and methods, and Chapter 6 covers enums, `match` expressions, and the `if let` control flow construct. You’ll use structs and enums to make custom types in Rust. -->

<!-- In Chapter 7, you’ll learn about Rust’s module system and about privacy rules for organizing your code and its public Application Programming Interface(API). -->

<!-- Chapter 8 discusses some common collection data structures that the standard library provides, such as vectors, strings, and hash maps. -->

<!-- Chapter 9 explores Rust’s error-handling philosophy and techniques. -->

<!-- Chapter 10 digs into generics, traits, and lifetimes, which give you the power to define code that applies to multiple types. -->

<!-- Chapter 11 is all about testing, which even with Rust’s safety guarantees is necessary to ensure your program’s logic is correct.  -->

<!-- In Chapter 12, we’ll build our own implementation of a subset of functionality from the `grep` command line tool that searches for text within files. -->

<!-- For this, we’ll use many of the concepts we discussed in the previous chapters. -->

<!-- Chapter 13 explores closures and iterators: features of Rust that come from functional programming languages.  -->

<!-- In Chapter 14, we’ll examine Cargo in more depth and talk about best practices for sharing your libraries with others. -->

<!-- Chapter 15 discusses smart pointers that the standard library provides and the traits that enable their functionality. -->

<!-- In Chapter 16, we’ll walk through different models of concurrent programming and talk about how Rust helps you to program in multiple threads fearlessly. -->

<!-- Chapter 17 looks at how Rust idioms compare to object-oriented programming principles you might be familiar with. -->

<!-- Chapter 18 is a reference on patterns and pattern matching, which are powerful ways of expressing ideas throughout Rust programs. -->

<!-- Chapter 19 contains a smorgasbord of advanced topics of interest, including unsafe Rust, macros, and more about lifetimes, traits, types, functions, and closures. -->

<!-- In Chapter 20, we’ll complete a project in which we’ll implement a low-level multithreaded web server! -->

<!-- Finally, some appendices contain useful information about the language in a more reference-like format.-->

<!-- Appendix A covers Rust’s keywords, Appendix B covers Rust’s operators and symbols, Appendix C covers derivable traits provided by the standard library, Appendix D covers some useful development tools, and Appendix E explains Rust editions.-->

<!-- There is no wrong way to read this book: if you want to skip ahead, go for it! You might have to jump back to earlier chapters if you experience any confusion.-->

<!-- But do whatever works for you. -->
하지만 본인에게 가장 적절한 방법대로 공부하셔도 좋습니다.
<span id="ferris"></span>

<!--An important part of the process of learning Rust is learning how to read the
error messages the compiler displays: these will guide you toward working code.-->
해당 과정 중에 가장 중요한 부분은 컴파일러의 에러 메시지 읽는 방법을 배우는 것입니다: 이것만 잘해도 코드 내부의 오류들을 수정할 수 있습니다.
<!--As such, we’ll provide many examples that don’t compile along with the error message the compiler will show you in each situation.-->
우리는 각각의 오류들을 보여주기 위해 컴파일러가 에러 메시지를 주는 예제들을 제공할 예정입니다.
<!--Know that if you enter and run a random example, it may not compile! Make sure you read the surrounding text to see whether the example you’re trying to run is meant to error. -->
아무 예제를 입력하고 실행하면 컴파일되지 않을 수 있습니다. 이것은 오류를 보여드리기 위함이니 주변 텍스트를 확인하여 어떤 오류인지를 확인해주세요.
<!--Ferris will also help you distinguish code that isn’t meant to work:-->
또한, Ferris는 오작동하는 코드를 구분하기 위해 등장합니다.

| Ferris                                                                 | Meaning                                          |
|------------------------------------------------------------------------|--------------------------------------------------|
| <img src="img/ferris/does_not_compile.svg" class="ferris-explain"/>    | <!--This code does not compile!--> 컴파일 되지 않는 코드                    |
| <img src="img/ferris/panics.svg" class="ferris-explain"/>              | <!--This code panics!--> panic이 발생하는 코드                                 |
| <img src="img/ferris/unsafe.svg" class="ferris-explain"/>              | <!--This code block contains unsafe code.--> 안전하지 않은 코드를 포함           |
| <img src="img/ferris/not_desired_behavior.svg" class="ferris-explain"/>| <!--This code does not produce the desired behavior.--> 의도된 결과가 나오지 않는 코드 |

<!--In most situations, we’ll lead you to the correct version of any code that
doesn’t compile.-->
책 내용 대부분은 컴파일되지 않은 코드를 올바르게 수정하는 과정들을 보여줍니다.

<!--## Source Code-->
## 소스코드

<!--The source files from which this book is generated can be found on
[GitHub][book].-->
이 책에서 사용되는 소스코드 파일은 [GitHub][book]에서 찾으실 수 있습니다.

[book]: https://github.com/rust-lang/book/tree/master/src

## HELLO WORLD

<!-- Now that you’ve installed Rust, let’s write your first Rust program. -->
이제 러스트 설치를 마쳤으니, 여러분의 첫 번째 러스트 프로그램을 작성해봅시다.

<!-- It’s traditional when learning a new language to write a little program that prints the text `Hello world!` to the screen, so we’ll do the same here! -->
전통적으로 새로운 (번역자 주: 프로그래밍) 언어를 배울때 스크린에 `Hello, world!`라는 텍스트를 출력하는 작은 프로그램을 작성하기에, 우리도 여기서 그와 같은 같은 것을 해 볼 것입니다!

<!-- > Note: This book assumes basic familiarity with the command line. -->
Note: 이 책은 커맨트 라인에 대한 기본적인 숙지를 가정합니다.
<!-- > Rust makes no specific demands about your editing or tooling or where your code lives, so if you prefer to use an integrated development environment (IDE) instead of the command line, feel free to use your favorite IDE. -->
러스트는 여러분의 편집기나 도구 또는 여러분의 코드가 어디에 있는지에 대한 구체적인 요구사항이 없기에, 만약 여러분이 커맨드 라인 대신 '통합 개발 환경(integrated development environment(IDE))'를 사용하는 것을 더 선호한다면, 자유롭게 여러분이 선호하는 IDE를 사용해도 좋습니다.
<!-- > Many IDEs now have some degree of Rust support; check the IDE’s documentation for details. -->
많은 IDE들이 이제 어느 정도 러스트 언어를 지원합니다; (번역자 주: 그렇다 하더라도) 세부적으로(for details) 해당 IDE들의 문서를 확인하기 바랍니다.
<!-- > Recently, the Rust team has been focusing on enabling great IDE support, and progress has been made rapidly on that front! -->
최근에 러스트 팀은 대부분의 IDE 지원을 가능하게 하는데 초점을 맞추고 있고, 최전선에서 빠르게 발전하고 있습니다.

### 프로젝트 디렉토리 만들기(Creating a Project Directory)

<!-- You’ll start by making a directory to store your Rust code. -->
여러분은 여러분의 러스트 코드을 저장하기 위한 디렉토리를 만드는 것부터 시작할 것입니다.
<!--It doesn’t matter to Rust where your code lives, but for the exercises and projects in this book, we suggest making a *projects* directory in your home directory and keeping all your projects there.-->
여러분의 코드가 어디에 있는지 러스트에게는 중요하진 않지만, 그러나 이 책에 있는 프로젝트들과 연습(exercise)들을 위해서, 우리는 여러분의 홈(home) 디렉토리에 *projects* 라는 디렉토리를 만들고, 여러분의 모든 프로젝트들을 거기에 유지하는 것을 제안합니다.

<!--Open a terminal and enter the following commands to make a *projects* directory and a directory for the “Hello, world!” project within the *projects* directory.-->
터미널을 열고 아래의 커맨드들을 입력해 *projects* 디렉토리를 만들고 “Hello, world!” 프로젝트를 위한 디렉토리를 *projects* 디렉토리 안에 만들어 줍니다.
<!--For Linux, macOS, and PowerShell on Windows, enter this:-->
Linux, macOS 그리고 윈도우 PowerShell 에서 다음 명령어를 입력해주세요:

```console
$ mkdir ~/projects
$ cd ~/projects
$ mkdir hello_world
$ cd hello_world
```

<!--For Windows CMD, enter this:-->
윈도우 CMD에선 이 명령어를 입력해주세요:

```cmd
> mkdir "%USERPROFILE%\projects"
> cd /d "%USERPROFILE%\projects"
> mkdir hello_world
> cd hello_world
```

### 러스트 프로그램의 작성과 실행

<!--Next, make a new source file and call it *main.rs*.-->
다음으로 새로운 소스 파일*main.rs*을 만들어 봅시다.
<!--Rust files always end with the *.rs* extension.-->
러스트 파일들은 언제나 끝에 *.rs* 확장자를 붙여줍니다.
<!--If you’re using more than one word in your filename, use an underscore to separate them.-->
만약 당신이 너의 파일 이름에 하나의 단어 이상을 사용한다면, 밑줄을 사용하여 그것들을 구분하면 됩니다.
<!--For example, use *hello_world.rs* rather than *helloworld.rs*.-->
예를 들면, *helloworld.rs* 보다는 *hello_world.rs*를 사용하는게 낫습니다.
<!--Now open the *main.rs* file you just created and enter the code in Listing 1-1.-->
이제 당신이 방금 막 만든 *main.rs* 파일을 열고 1-1dml 코드 리스트를 입력해봅시다.

<span class="filename">Filename: main.rs</span>

```rust
fn main() {
    println!("Hello, world!");
}
```

<span class="caption">Listing 1-1: A program that prints `Hello, world!`</span>

<!--Save the file and go back to your terminal window.-->
파일을 저장하고 당신의 터미널 윈도우로 돌아갑니다.
<!--On Linux or macOS, enter the following commands to compile and run the file:-->
리눅스나 맥 OS에선 파일을 컴파일하고 실행하기 위해서 아래의 명령어들을 따라쳐 줍니다.

```console
$ rustc main.rs
$ ./main
Hello, world!
```

<!--On Windows, enter the command `.\main.exe` instead of `./main`:-->
윈도우 에서는 `./main` 명령어 대신에 `.\main.exe` 명령어를 입력합니다.

```powershell
> rustc main.rs
> .\main.exe
Hello, world!
```

<!--Regardless of your operating system, the string `Hello, world!` should print to the terminal.-->
당신의 OS 시스템에 관계없이 문자 `Hello, world!` 는 터미널에 출력될 것입니다.
<!--If you don’t see this output, refer back to the[“Troubleshooting”][troubleshooting]<!-- ignore --> part of the Installation section for ways to get help.-->
만약 당신이 이 결과물이 보이지 않는다면 도움을 얻기위한 방법으로 설치 파트의 [“Troubleshooting”] 섹션을 참조하면 됩니다.
<!--If `Hello, world!` did print, congratulations!-->
만약 `Hello, world!` 가 출력되었다면 축하합니다!
<!--You’ve officially written a Rust program.-->
당신은 공식적으로 러스트 프로그램을 작성한 것입니다.
<!--That makes you a Rust programmer—welcome!-->
그것은 당신을 러스트 프로그래머로 만들어 줄겁니다.- 환영합니다!

### 러스트 프로그램의 구조

<!--Let’s review in detail what just happened in your “Hello, world!” program.-->
당신의 “Hello, world!” 프로그램에 무슨 일이 발생한 것인지 자세히 살펴봅시다.
<!--Here’s the first piece of the puzzle:-->
여기에 퍼즐의 첫 부분이 있습니다.

```rust
fn main() {

}
```

<!--These lines define a function in Rust.-->
이 줄들은 러스트에서 함수를 정의합니다.
<!--The `main` function is special: it is always the first code that runs in every executable Rust program.-->
메인 함수는 특별합니다: 그것은 언제나 모든 실행되는 러스트 프로그램에서 작동하는 첫번째 코드입니다.
<!--The first line declares a function named `main` that has no parameters and returns nothing.-->
첫 번째 줄에 함수의 이름인 `main`을 선언하는데 그것은 파라미터가 없고 아무것도 반환하지 않습니다.
<!--If there were parameters, they would go inside the parentheses, `()`.-->
만약 거기에 파라미터들이 있다면, 괄호 안으로 들어가 있어야 합니다.

<!--Also, note that the function body is wrapped in curly brackets, `{}`.-->
또한, 함수의 몸체는 중괄호로 둘러싸여 있어야 함을 명심합니다.
<!--Rust requires these around all function bodies.-->
러스트는 이 모든 것들을 함수 몸체 주위에 필요로 합니다.
<!--It’s good style to place the opening curly bracket on the same line as the function declaration, adding one space in between.-->
여는 중괄호를 함수 선언과 같은 줄에 두고 그 사이에 하나의 공백(space)을 추가하는 것이 좋은 코드 스타일입니다.

<!--If you want to stick to a standard style across Rust projects, you can use an automatic formatter tool called `rustfmt` to format your code in a particular style.-->
만약 당신이 러스트 프로젝트에서 표준적인 스타일을 고수하고 싶다면, 당신은 당신의 코드를 특정한 스타일로 포맷해주는 `rustfmt`라고 부르는 자동적인 포매터 도구를 사용할 수 있습니다.
<!--The Rust team has included this tool with the standard Rust distribution, like `rustc`, so it should already be installed on your computer!-->
러스트팀은 `rustc`와 같이 이 도구를 표준적인 러스트 배포판에 포함시켰기 때문에 그것은 미리 당신의 컴퓨터에 설치되어 있습니다.
<!--Check the online documentation for more details.-->
더 상세한 것은 온라인 문서를 검토해주세요.

<!--Inside the `main` function is the following code:-->
메인 함수 내부에는 아래의 코드가 있습니다.

```rust
    println!("Hello, world!");
```

<!--This line does all the work in this little program: it prints text to the screen.-->
이 줄은 이 작은 프로그램에서 모든 작업을 합니다: 그것은 스크린에 텍스트를 출력합니다.
<!--There are four important details to notice here.-->
여기에서 알아차려야할 4가지 중요한 사항들이 있습니다.

<!--First, Rust style is to indent with four spaces, not a tab.-->
첫 번째 러스트 스타일은 tab 이 아닌 4개의 공백을 들여쓰기 하는 것입니다.

<!--Second, `println!` calls a Rust macro.-->
두 번째 `println!`은 러스트 매크로를 호출합니다.
<!--If it called a function instead, it would be entered as `println` (without the `!`).-->
만약 그것이 대신에 함수를 호출한다면, 그것은 `println`와 같이 !없이 입력 되었을 것입니다.
<!--We’ll discuss Rust macros in more detail in Chapter 19.-->
우리는 러스트 매크로들에 대해 챕터19장에서 좀더 자세히 토의할 것입니다.
<!--For now, you just need to know that using a `!` means that you’re calling a macro instead of a normal function.-->
지금은 당신이 느낌표를 사용한다는 것의 의미가 일반 함수 대신에 매크로를 호출한다는 것임을 알 필요가 있습니다.

<!--Third, you see the `"Hello, world!"` string.-->
세 번째 당신은 `"Hello, world!"` 문자를 본다는 점입니다.
<!--We pass this string as an argument to `println!`, and the string is printed to the screen.-->
우리는 이 문자를 `println!` 에 인자로 넘겨주고, 그 문자는 화면에 출력되었습니다.

<!--Fourth, we end the line with a semicolon (`;`), which indicates that this expression is over and the next one is ready to begin.-->
네 번째 우리는 줄 끝에 세미콜론(`;`)을 표시하는데, 그것은 이 표현식이 끝나고 다음 것이 시작될 준비가 되었다는 지시를 합니다.
<!--Most lines of Rust code end with a semicolon.-->
대부분의 러스트 코드 줄 끝은 세미콜론으로 끝납니다.

<!-- ### Compiling and Running Are Separate Steps -->
### 컴파일(Compiling)과 실행(Running)은 별도의 단계(Steps)

<!--You’ve just run a newly created program, so let’s examine each step in the process.-->
여려분은 이제 새롭게 만들어진 프로그램을 실행했으므로, 과정에서 각 단계를 살펴보겠습니다.

<!--Before running a Rust program, you must compile it using the Rust compiler by entering the `rustc` command and passing it the name of your source file, like this:-->
러스트 프로그램을 실행하기 전에, 여러분은 아래와 같이 명령어 `rustc`를 입력하고 다음으로 여러분의 소스 파일의 이름을 쳐서, 러스트 프로그램을 컴파일해야 합니다.

```console
$ rustc main.rs
```

<!--If you have a C or C++ background, you’ll notice that this is similar to `gcc` or `clang`.-->
만약 여러분이 C 또는 C ++ 배경 지식이 있으면, 이것이 `gcc`나 `clang`과 비슷하다는 것을 알아차릴 것입니다.
<!--After compiling successfully, Rust outputs a binary executable.-->
성공적으로 컴파일한 후, 러스트는 바이너리 '실행파일(executable)'을 출력합니다.
<!--On Linux, macOS, and PowerShell on Windows, you can see the executable by entering the `ls` command in your shell.-->
리눅스와 맥 OS, 윈도우 파워쉘(PowerShell)에서, 여러분은 여러분의 셀(shell)에서 명령어 `ls`를 하면 그 실행파일을 볼 수 있습니다.
<!--On Linux and macOS, you’ll see two files.-->
리눅스와 맥 OS에서는, 두 개의 파일이 보일 것입니다.
With PowerShell on Windows, you’ll see the same three files that you would see using CMD.
윈도우 파워쉘에서는, CMD를 사용하여 볼 수 있는 것과 같은 3개의 동일한 파일들을 볼 수 있습니다.

```console
$ ls
main  main.rs
```

<!--With CMD on Windows, you would enter the following:-->
윈도우 CMD에서, 여러분은 아랭와 같이 입력할 것입니다.

```cmd
> dir /B %= the /B option says to only show the file names =%
main.exe
main.pdb
main.rs
```

<!--This shows the source code file with the *.rs* extension, the executable file (*main.exe* on Windows, but *main* on all other platforms), and, when using Windows, a file containing debugging information with the *.pdb* extension.-->
이것은 *.rs* 확장자를 갖고 있는 소스 코드 파일, 실행 파일(윈도우에서는 *main.exe* , 그러나 다른 모든 플랫폼에서는 *main*) 그리고, 윈도우를 사용할 때, *.pdb* 확장자를 가지고 있는 디버깅 정보를 포함하는 파일을 보여줍니다.

<!--From here, you run the *main* or *main.exe* file, like this:-->
여기에서 다음처럼 *main* 또는 *main.exe* 파일을 실행합니다.

```console
$ ./main # or .\main.exe on Windows
```

<!--If *main.rs* was your “Hello, world!” program, this line would print `Hello, world!` to your terminal.-->
만약 *main.rs*가 여러분은 “Hello, world!” 프로그램이라면, 이 줄은 당신의 터미널에 `Hello, world!`를 출력할 것입니다.

<!--If you’re more familiar with a dynamic language, such as Ruby, Python, or JavaScript, you might not be used to compiling and running a program as separate steps.-->
만약 여러분이 좀 더 동적(dynamic) 언어, 예를 들어 루비, 파이썬, 자바스크립트 와 같은 언어에 친밀하다면, 아마도 프로그램을 컴파일(compiling)과 실행(running)하는 별도의 단계로 구분하는데에 익숙하지 않을 수도 있습니다.
<!--Rust is an *ahead-of-time compiled* language, meaning you can compile a program and give the executable to someone else, and they can run it even without having Rust installed.-->
러스트는 '사전에 컴파일된(*ahead-of-time compiled*)' 언어인데, 이는 여러분이 프로그램을 컴파일하고 누군가에게 그 실행파일을 줄 수 있으면, 그들은 러스트를 설치하지 않고도 이를 실행할 수 있다는 것을 의미합니다.
<!--If you give someone a *.rb*, *.py*, or *.js* file, they need to have a Ruby, Python, or JavaScript implementation installed (respectively).-->
만약 여러분이 누군가에게 *.rb*, *.py*, or *.js* 파일을 준다면, 그들은 루비, 파이썬, 자바스크립트를 이행하기 위해 개별적으로 설치를 해야할 필요가 있습니다.
<!--But in those languages, you only need one command to compile and run your program.-->
그러나 이런 언어들에서는, 여러분은 당신의 프로그램을 컴파일하고 실행하는데 오직 하나의 명령어만 필요로할 것입니다.
<!--Everything is a trade-off in language design.-->
모든 것은 언어 디자인 안에서의 상쇄작용입니다.

<!--Just compiling with `rustc` is fine for simple programs, but as your project grows, you’ll want to manage all the options and make it easy to share your code.-->
`rustc`와 함께 컴파일링 하는 것은 단일 프로그램에서 적당합니다만, 당신의 프로젝트가 성장한다면, 당신은 모든 선택사항을 관리하고, 당신의 코드를 공유할 수 있어야만 합니다.
<!--Next, we’ll introduce you to the Cargo tool, which will help you write real-world Rust programs.-->
다음으로, 우리는 여러분이 현실-세계 러스트 프로그램들을 작성하는데 도움을 줄 수 있는 Cargo 라는 도구를 여러분에게 소개할 것입니다.

[troubleshooting]: ch01-01-installation.html#troubleshooting

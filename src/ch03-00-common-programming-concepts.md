<!--# Common Programming Concepts -->
# 일반적인 프로그래밍 개념들
 
<!--This chapter covers concepts that appear in almost every programming language and how they work in Rust-->
이 장에서는 대부분의 프로그래밍 언어에서 사용하는 공통 개념들이 무엇인지, 또 그 개념들이 러스트에서는 어떻게 사용되는지에 대해서 다룹니다.
<!--Many programming languages have much in common at their core-->
많은 프로그래밍 언어들의 핵심 개념은 비슷합니다.
<!--None of the concepts presented in this chapter are unique to Rust, but we’ll discuss them in the context of Rust and explain the conventions around using these concepts. -->
러스트만이 가진 고유 특성들은 제외하고 설명하지만, 공통 개념들이 러스트에서는 어떤 의미로 쓰이는지에 대해서는 살펴볼 것입니다.
<!--Specifically, you’ll learn about variables, basic types, functions, comments, and control flow-->
구체적으로 우리는 변수, 기본 타입, 함수, 주석, 제어문에 대해 배울 것입니다.
<!--These foundations will be in every Rust program, and learning them early will give you a strong core to start from. -->
이런 기초 개념들은 러스트 프로그램에서도 필히 사용되기 때문에 이들을 미리 배우는 것은 차후의 단단한 밑거름이 될 것입니다.

<!-- #### Keywords -->
> #### 키워드

<!-- The Rust language has a set of *keywords* that are reserved for use by > the language only, much as in other languages-->
> 러스트 언어는 다른 언어들과 마찬가지로 사용가능한 *키워드* 모음이 있습니다.
<!-- Keep in mind that you cannot > use these words as names of variables or functions-->
> 키워드는 함수나 변수의 이름으로 사용할 수 없다는 것을 명심하세요.
<!-- Most of the keywords have > special meanings, and you’ll be using them to do various tasks in your Rust > programs; a few have no current functionality associated with them but have > been reserved for functionality that might be added to Rust in the future-->
> 대부분의 키워드는 특정한 기능을 의미하며, 이후 러스트 프로그램에서 다양하게 사용해볼 예정입니다.
<!--You can find a list of the keywords in [Appendix A][appendix_a].-->
> 키워드 목록은 [부록 A][appendix_a]에서 찾을 수 있습니다.

[appendix_a]: appendix-01-keywords.md 

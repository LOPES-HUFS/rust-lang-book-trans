""" 목표: 기존의 md 파일을 html 주석 처리된 md 파일로 변환하는 함수
    
    TODO:
    - [x] 파일 가져온 후 읽기
    - [x] 엔터로 잘린 글들만 이어 붙이기 (코드블록이나 테이블 등은 이어 붙이면 x)
    - [x] 이어진 글들 온점(.)을 기준으로 문장 나누기 --완료
    - [x] 문장에만 html 주석 기호 (<!--, -->) 붙이기
    - [x] 하나의 md 파일로 저장하기

output
-------
> translator('ch00-00-introduction.md')
> test[0:10]

<!--# Introduction -->
 
<!--> Note: This edition of the book is the same as [The Rust Programming > Language][nsprust] available in print and ebook format from [No Starch > Press][nsp]. -->
 
[nsprust]: https://nostarch.com/rust 
[nsp]: https://nostarch.com/ 
 
<!--Welcome to *The Rust Programming Language*, an introductory book about Rust-->
<!--The Rust programming language helps you write faster, more reliable software-->
<!--High-level ergonomics and low-level control are often at odds in programming language design; Rust challenges that conflict-->
<!--Through balancing powerful technical capacity and a great developer experience, Rust gives you the option to control low-level details (such as memory usage) without all the hassle traditionally associated with such control. -->

HOW TO USE
-------
1. 영어버전 md 파일을 다운받는다.
2. 주피터노트북에서 md 파일이 있는 디렉토리를 오픈한다.
3. translator('ch00-00-introduction.md') 입력한다.
4. 다시 md파일을 확인하면 주석처리 된 모습을 확인할 수 있다.
"""
import re
from string import ascii_uppercase


def translator(file_name):
    
    my_file = open(file_name, mode='r')
    lines = my_file.readlines()
    fin = linemaker(lines)
    lines = [sen.replace('\n',' ') for sen in fin]
    fin = spliter(lines)
    link = symbolic_link(fin)
    with open(file_name, mode = 'w') as f:
        f.writelines(link)
    
def linemaker(lines):
    fin = []
    txt = ''
    for line in lines:
        if 65 < len(line) < 85:
            txt += line
        else:
            txt += line
            fin.append(txt)
            txt = ''
    return fin

def spliter(lines):
    lis = []
    for sen in lines:
        temp = re.split('\.[\s](?=[\w]+)',sen)
        lis += temp
    return lis


def symbolic_link(lines):
    
    lis = []
    for sen in lines:
        if sen[0] == '#' or sen[0] == '>' or sen[0] == '*' or sen[0] in list(ascii_uppercase):
            sen = '<!--' + sen + '-->\n'
            lis.append(sen)
        else:
            sen = sen + '\n'
            lis.append(sen)
    return lis

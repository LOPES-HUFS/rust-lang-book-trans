## 목표: 기존의 md 파일을 html 주석 처리된 md 파일로 변환하는 함수
### - 파일 가져온 후 읽기 --완료
### - 엔터로 잘린 글들만 이어 붙이기 (코드블록이나 테이블 등은 이어 붙이면 x) --완료
### - 이어진 글들 온점(.)을 기준으로 문장 나누기 --완료
### - 문장에만 html 주석 기호 (<!--, -->) 붙이기
### - 하나의 md 파일로 저장하기

def translator(file_name):
    
    my_file = open(file_name, mode='r')
    lines = my_file.readlines()
    fin = linemaker(lines)
    lines = [sen.replace('\n',' ') for sen in fin]
    fin = spliter(lines)
    return fin
    
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

# rust-lang-book-trans

러스트를 공부합니다.

## 번역 아이디어

우선 영어 문장을 한 줄씩 주석처리하면서 한 줄 한 줄 번역합니다. 이렇게 번역하면 모든 줄이 다 단락이 떨어지는 문제가 발생합니다. 그러나 개별 파일을 다 번역하게 되면 영어 문장을 제거할 예정입니다. 한 줄씩 띄어쓰기를 하기 때문에 한글이 한 줄씩 떨어지게 됩니다. 원래 마크다운 포멧에서는 만약 단락을 표현하기 위하여 두 줄씩 띄어쓰기를 하면 됩니다.

## tip

### 터미널을 이용한 방법

```bash
# bat: 화면에서 멋지게 여러가지 형식의 텍스트 파일 내용을 보여준다.
brew install bat
# ripgrep: 정규표현식을 사용할 수 있게 해준다.
brew install ripgrep
```

*executable* 이라는 글자가 들어간 파일을 다 찾아 주세요!

```bast
rg -i executable | bat
```

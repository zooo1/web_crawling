# 2019.09.27

이 강의는 인프런의 '파이썬을 활용한 웹 데이터 수집하기' 강좌를 들으며 정리한 내용입니다.

# 오리엔테이션

## python, anaconda 설치 및 개발 환경 설정

### python

> 프로그래밍 언어의 일종으로 객체 지향형이다. 

#### 설치 방법

나는 맥을 사용하고 있고 brew, zsh등을 미리 설치해놓은 상태에서 시작하였다. 아직 brew, zsh를 설치하지 않았다면..! [클릭](https://beomi.github.io/2017/07/07/Beautify-ZSH/) 하여 설치를 합시다. ~~zsh를 사용하면 왠지 간지나는 개발자가 된 것 같다.~~ 

터미널 창에서  ![brew install python3](../assets/brew_install_python)

을 실행하면 python 설치가 완료된다. 이미 맥에서는 python2가 내장되어 있기 때문에 설치 후에도 python2가 실행되는 경우가 있다. 이를 방지하기 위해서는 

```bash
vim ~/.zshrc
```

에서 수정모드 (i 버튼 클릭)로 전환 후 아래와 같이 설정해준다. 

![alias 설정](../assets/alias)

설정 후에는 esc + `:wq`버튼을 누르고 명령창에 source 해준다.

```bash
source ~/.zshrc
```

### anaconda

> python 기반의 data 분석에 필요한 오픈 소스를 모아놓은 **개발 플랫폼**
>
> 수준 높은 패키지 관리자를 통해 파이썬의 효율을 극대화할 수 있다.
>
> **가상환경** 관리자를 통해 프로젝트별 개발환경을 구성할 수 있다.
>
> (가상환경을 구성하면 패키지 충돌이 일어나지 않고 개별적으로 환경을 구성할 수 있다.)



아래의 이미지를 보면 조금 더 쉽게 이해할 수 있다.

![pythonVSanaconda](../assets/pipVSanaconda) 

일반적인 파이썬이 pip만 제공한다면 아나콘다는 다양한 패키지들을 이미 갖고 있다. 용량은 크지만 패키지 관리가 용이하고 가상환경에서 작업할 수 있다는 장점이 있다. 

#### 설치 방법

1. anaconda [사이트](https://www.anaconda.com/distribution/)에 접속하여 다운로드 받기

2. anaconda path 설정해주기 

   ```bash
   vim ~/.zshrc
   ```

   ![anaconda path](../assets/anaconda_path)

   ```bash
   source ~/.zshrc
   ```

#### 기본 명령어

```bash
conda create --name(-n) [가상환경 이름] [설치할 패키지 ex)python=3.6]
conda info -envs
activate [가상환경이름]
conda update conda
conda list
pip install -ignore-installed [패키지 이름]
pip uninstall [패키지이름]
conda remove -n [가상환경이름] --all
conda clean -all(-a)
```





### atom

> 문서 및 소스 코드 편집기

설치 방법:

[여기](https://atom.io/) 에서 각자의 환경에 맞는 것을 찾아 다운로드 하면 끝..!




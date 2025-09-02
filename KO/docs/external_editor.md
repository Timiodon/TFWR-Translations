# 외부 에디터
게임 내 텍스트 에디터는 보통 이 게임을 플레이하기에 충분하지만, 물론 Visual Studio Code와 같은 더 정교한 텍스트 에디터와는 경쟁할 수 없어요.

게임은 모든 코드 파일을 .py 파일로 저장하므로, Python 에디터로 편집할 수 있어요. 
이는 편의를 위한 것일 뿐, 게임 내 언어는 실제 Python이 아니지만, Python IntelliSense가 어느 정도 잘 작동할 만큼 비슷해요.
파일은 [세이브 폴더](persistent_data_path/Saves)에서 찾을 수 있어요.

각 세이브에는 `__builtins__.py` 파일도 포함되어 있는데, 여기에는 IntelliSense를 활성화하기 위해 게임 내 빌트인과 일치하는 내장 Python 정의가 들어있어요. 
VS Code는 `__builtins__.py`를 자동으로 감지할 수 있지만, 일부 에디터는 `from __builtins__ import *`를 해야만 작동할 수 있어요.

외부 변경 사항을 세이브를 다시 로드하지 않고 게임 내에서 보려면 "파일 감시" 옵션을 활성화해야 해요. 외부에서 파일을 생성하거나 삭제하면, 이를 보려면 여전히 세이브를 다시 로드해야 해요.

## VS Code 사용하기
Visual Studio Code는 The Farmer Was Replaced와 함께 사용하기에 권장되는 코드 에디터예요.

[여기](https://code.visualstudio.com/download)에서 설치할 수 있어요.

다운로드한 후, VS Code에 Python 확장 프로그램을 설치하세요.

그런 다음, VS Code에서 `.py` 파일이 있는 [폴더](persistent_data_path/Saves)를 여세요. 개별 파일만 열지 말고 전체 폴더를 열어야 `__builtins__.py` 파일이 작동해요.

게임에서 "파일 감시" 옵션이 켜져 있는지 확인하세요. 이제 VS Code에서 저장할 때마다 변경 사항이 게임에 자동으로 나타나요.

이게 다예요! 이제 전문 코드 에디터에서 코드를 작성할 수 있어요!
# 외부 에디터
게임 내 텍스트 에디터는 이 게임을 플레이하는 데 보통 충분하지만, 물론 Visual Studio Code와 같은 더 정교한 텍스트 에디터와는 경쟁할 수 없습니다.

게임은 모든 코드 파일을 .py 파일로 저장하므로, 파이썬 에디터로 편집할 수 있습니다. 
참고로 이것은 편의를 위한 것일 뿐입니다. 게임 내 언어는 실제로 파이썬이 아니지만, 파이썬 IntelliSense가 그럭저럭 작동할 만큼은 가깝습니다.
파일은 [저장 폴더](persistent_data_path/Saves)에서 찾을 수 있습니다.

각 저장 파일에는 IntelliSense를 활성화하기 위해 게임 내 빌트인과 일치하는 파이썬 내장 정의가 포함된 `__builtins__.py` 파일도 들어 있습니다. 
VS Code는 `__builtins__.py`를 자동으로 감지할 수 있지만, 일부 에디터는 `from __builtins__ import *`를 해야만 작동할 수 있습니다.

저장 파일을 다시 불러오지 않고도 외부 변경 사항을 게임 내에서 보려면, "File Watcher" 옵션을 활성화해야 합니다. 외부에서 파일을 생성하거나 삭제하는 경우, 변경 사항을 보려면 여전히 저장 파일을 다시 불러와야 합니다.

## VS Code 사용하기
Visual Studio Code는 The Farmer Was Replaced와 함께 사용하기에 권장되는 코드 에디터입니다.

[여기](https://code.visualstudio.com/download)서 설치할 수 있습니다.

다운로드 후, VS Code에서 파이썬 확장 프로그램을 설치하세요.

그 다음, VS Code에서 `.py` 파일이 있는 [폴더](persistent_data_path/Saves)를 여세요. 개별 파일이 아닌 전체 폴더를 열어야 `__builtins__.py` 파일이 작동합니다.

게임 내에서는 "File Watcher" 옵션이 켜져 있는지 확인하세요. 이제 VS Code에서 저장할 때마다 변경 사항이 게임에 자동으로 나타납니다.

이게 다입니다! 이제 전문 코드 에디터에서 코드를 작성할 수 있습니다!
# External Editor
게임 내 텍스트 에디터로도 이 게임을 플레이하는 데에는 보통 충분하지만, 당연히 Visual Studio Code 같은 더 고급의 텍스트 에디터와는 비교할 수 없어요.

게임은 모든 코드를 .py 파일로 저장하니까 Python 에디터로 편집할 수 있어요. 다만, 이건 단지 편의를 위한 거예요. 게임 내 언어는 실제로 Python은 아니지만, Python IntelliSense가 잘 작동할 정도로 비슷해요.
파일은 [저장 폴더](persistent_data_path/Saves)에서 찾을 수 있어요.

각 저장 파일에는 내장 Python 정의가 포함된 `__builtins__.py` 파일도 있어요. 이 파일 덕분에 게임 내 내장 기능과 호환되는 IntelliSense를 사용할 수 있죠. VS Code는 `__builtins__.py`를 자동으로 인식할 수 있지만, 몇몇 에디터는 `from __builtins__ import *`를 해야 제대로 작동할 수도 있어요.

저장 파일을 다시 로드하지 않고도 외부 변경 사항을 게임에서 보려면, "File Watcher" 옵션을 활성화해야 해요. 외부에서 파일을 생성하거나 삭제하면 저장 파일을 다시 로드해야만 변경 사항을 볼 수 있어요.

## VS Code 사용하기
Visual Studio Code는 The Farmer Was Replaced와 함께 사용하기에 추천하는 코드 에디터예요.

[여기](https://code.visualstudio.com/download)에서 설치할 수 있어요.

다운로드한 후, VS Code 내에서 Python 확장을 설치하세요.

그 다음, VS Code에서 `.py` 파일을 보유한 [폴더](persistent_data_path/Saves)를 열어요. 개별 파일만 열지 말고 폴더 전체를 여세요. 그렇지 않으면 `__builtins__.py` 파일이 작동하지 않을 수 있어요.

게임에서 "File Watcher" 옵션이 켜져 있는지 확인하세요. 이제 VS Code에서 저장할 때마다 변경 사항이 자동으로 게임에 반영돼요.

끝이에요! 이제 전문가 수준의 코드 에디터에서 코드를 작성할 수 있어요!
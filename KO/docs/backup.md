# 백업 로딩하기
안타깝게도 가끔씩 저장 파일이 손상되거나 코드 파일을 잃어버리게 될 수 있어. 만약 이런 일이 발생한다면 백업을 로딩해보는 게 좋아. 자주 발생하면, Steam Cloud를 끄는 걸 고려해봐.

게임이 저장될 때마다 백업이 생성되며, 필요한 경우 복구할 수 있도록 소수의 백업이 유지돼.
이 백업들은 [backup directory](persistent_data_path/Backup)에서 찾을 수 있어. 이들은 [save directory](persistent_data_path/Saves)에 있는 저장 파일들의 복사본이야.
백업을 로딩하는 가장 쉬운 방법은 로드하고 싶은 특정 백업의 폴더를 저장 디렉토리에 복사하는 거야.

저장은 `save.json` 파일과 여러 개의 `.py` 파일이 있는 폴더야.
코드 파일들을 조금만 잃었거나, 코드 파일들은 있는데 `save.json` 파일이 손상되었다면, 백업에서 해당 파일들만 가져와서 손상된 부분을 교체할 수도 있어.
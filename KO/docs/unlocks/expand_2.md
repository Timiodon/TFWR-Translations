# 확장 2
농장이 또 확장되었네요! 이제 타일이 한 줄로 가지런히 배열되어 있지 않아서, 정사각형 그리드를 탐색하는 방법을 찾아야 해요.

`while` 루프만으로는 센서와 연산자를 해제하기 전까지는 이것이 불가능해요.
이제 `for` 루프를 소개할 차례입니다.

`for` 루프에 대해 모든 정보를 알고 싶다면 [For Loop](docs/scripting/for.md) 페이지를 참조하세요. 하지만 지금은 코드를 일정 횟수 반복할 때만 필요해요.

`# n 번의 뒤집기
for i in range(5):
	do_a_flip()`

`range(n)`은 `0`부터 `n-1`까지의 숫자 범위를 만들고, `n`개의 요소가 있습니다. `for` 루프는 시퀀스의 각 요소에 대해 루프 본문을 한 번 실행합니다. 이 예에서 `do_a_flip()`은 `5`번 호출될 것입니다.

함수 `get_world_size()`도 이제 사용할 수 있어요. 이 함수는 농장의 한 변의 길이를 반환합니다. 이렇게 하면 다음 확장 업그레이드 때 코드가 깨지지 않게 작성할 수 있습니다.

`for i in range(get_world_size()):
	harvest()
	move(North)`

이 예제는 어떤 농장 크기에서도 농장의 한 열을 수확합니다.

농장을 돌아다니는 방법이 막히셨다면 아래의 힌트를 확인하세요.
<spoiler=show hint> 농장을 돌아다니는 방법은 여러 가지가 있습니다.
우리가 찾고 있는 것은 농장이 다시 확장되더라도 깨지지 않는 체계적인 방법으로 농장을 탐색하는 것입니다.
농장의 모든 곳에 가기 위한 체계적인 방법은 다음 두 단계를 계속 반복하는 것입니다:

1. `North` 쪽으로 돌아갈 때까지 이동합니다.
2. `East`로 이동합니다.

`for i in range(get_world_size()):` 이 아이디어를 코드로 바꾸는 데 유용할 수 있습니다.
</spoiler>
<spoiler=show possible solution> 기본적인 탐색은 다음과 같을 수 있습니다:

`for i in range(get_world_size()):
	for j in range(get_world_size()):
		# 모든 타일에서 한 번 뒤집기
		do_a_flip()
		move(North)
	move(East)`
</spoiler>
def solution(participant, completion):
    answer = ''

    runner = {}

    for player in participant:
        if not player in runner:
            runner[player] = 1
        else:
            runner[player] += 1

    for player in completion:
        runner[player] -= 1
        if runner[player] == 0:
            runner.pop(player)

    answer = list(runner.keys())[0]

    return answer
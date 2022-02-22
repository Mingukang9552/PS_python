def solution(lottos, win_nums):
    answer = []
    sameNum = 0
    val = lottos.count(0)
    for i in lottos:
        if i in win_nums:
            sameNum += 1
    high = 1 if val + sameNum < 2 else val + sameNum
    low = 1 if sameNum < 2 else sameNum


    answer.append(7-high)
    answer.append(7-low)
    return answer


def main():
    lottos = [44, 1, 0, 0, 31, 25]
    wind_nums = [31, 10, 45, 1, 6, 19]
    print(solution(lottos, wind_nums))


main()

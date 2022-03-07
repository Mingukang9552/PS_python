def solution(numbers):
    answer = set()
    for i in range(0,len(numbers)) :
        for j in range(i+1,len(numbers)) :
            answer.add(numbers[i] + numbers[j])


    answer = list(answer)
    answer.sort()
    return answer


def main() :
    numbers = [2,1,3,4,1]
    print(solution(numbers))

main()
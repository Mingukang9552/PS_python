def solution(s):
    answer = ""
    dic = {"zero" : 0, "one" : 1, "two" : 2, "three" : 3,
           "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9}
    tmp = ""
    for i in s :
        if i.isalpha() :
            tmp += i
            if tmp in dic:
                answer += str(dic[tmp])
                print(dic[tmp])
                tmp = ""
        elif i.isdigit() :
            answer += str(i)
    return answer


def main():
    s = "onezero"
    print(solution(s))


main()

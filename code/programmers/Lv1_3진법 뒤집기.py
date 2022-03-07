def solution(n):
    answer = makeDecimal(makeTriple(n))
    return answer

def makeTriple(n) :
    tmp = ""
    while True :
        tmp = str(n%3) + tmp
        if n < 3 :
            break
        else :
            n = n//3
    return tmp

def makeDecimal(n) :
    ans = 0
    for i in range(0,len(list(n))) :
        ans += pow(3,int(i)) * int(n[i])
    return ans

def main() :
    n = 125
    print(solution(n))

main()
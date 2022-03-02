def solution(numbers, hand) :
    answer = ''

    left = [1,4,7]
    right = [3,6,9]
    leftLoc = 10
    rightLoc = 11
    for i in numbers :
        if i in left :
            answer += 'L'
            leftLoc = i
        elif i in right :
            answer += 'R'
            rightLoc = i
        else :
            answer += getHand(leftLoc,rightLoc,i,hand)
            if answer[len(answer)-1] == 'L' :
                leftLoc = i
            else :
                rightLoc = i

    return answer
def getHand(leftNum, rightNum, targetNum,hand) :
    answer = ''
    keypad = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 0, 11],
    ]
    leftLoc = []
    rightLoc = []
    targetLoc = []
    for i in range(0,len(keypad)) :
        for j in range(0, len(keypad[i])) :
            if keypad[i][j] == leftNum :
                leftLoc.append(i)
                leftLoc.append(j)
            if keypad[i][j] == rightNum :
                rightLoc.append(i)
                rightLoc.append(j)
            if keypad[i][j] == targetNum :
                targetLoc.append(i)
                targetLoc.append(j)

    leftDis = abs(leftLoc[0] - targetLoc[0]) + abs(leftLoc[1] - targetLoc[1])
    rightDis = abs(rightLoc[0] - targetLoc[0]) + abs(rightLoc[1] - targetLoc[1])
    if leftDis > rightDis :
        answer = 'R'

    elif leftDis < rightDis :
        answer = 'L'
    else :
        answer  = 'L' if hand == 'left' else 'R'
    return answer
def main() :
    numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
    hand = "right"
    print(solution(numbers,hand))

main()
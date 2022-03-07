def solution(sizes):
    tmp = 0
    w,h = -1, -1
    for i in range(0,len(sizes)) :
        if sizes[i][0] < sizes[i][1] :
            tmp = sizes[i][1]
            sizes[i][1] = sizes[i][0]
            sizes[i][0] = tmp
        w = max(w, sizes[i][0])
        h = max(h, sizes[i][1])
    return w * h

def main() :
    sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
    print(solution(sizes))

main()
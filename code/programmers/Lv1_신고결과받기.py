def solution(id_list, report, k):
    answer = []
    dic1 = {}
    dic2 = {}
    reportLst = []
    for str in report:
        str = str.split(" ")
        if not str[1] in dic1:
            dic1[str[1]] = {str[0]}
        else :
            dic1[str[1]].add(str[0])
        if not str[0] in dic2 :
            dic2[str[0]] = {str[1]}
        else :
            dic2[str[0]].add(str[1])
    for str in dic1.keys() :
        if(len(dic1[str]) >= k ) :
            reportLst.append(str)
    print(reportLst)
    for i in id_list :
        cnt = 0
        if i in dic2 :
            for j in dic2[i] :
                if j in reportLst :
                    cnt += 1
        answer.append(cnt)
    print(answer)
    return answer

def main () :
    k = 2
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report =  ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
    print(solution(id_list,report,k));

main();
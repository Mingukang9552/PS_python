import re;

def solution(new_id) :
    new_id = new_id.lower()
    new_id = re.sub("[^a-z|0-9|_|.|-]*","",new_id)
    new_id = re.sub("[.]+",".",new_id)
    if new_id[0] == "." :
        new_id = new_id[1:len(new_id)]
    if len(new_id) >=1 and new_id[len(new_id)-1] == "." :
        new_id = new_id[0:len(new_id)-1]
    if new_id == "" :
        new_id += "a"
    if len(new_id) >= 16 :
        new_id = new_id[0:15]
        if new_id[len(new_id)-1] == "." :
            new_id = new_id[0:len(new_id)-1]
    if len(new_id) <= 2 :
        for i in range(0,3-len(new_id)) :
            new_id += new_id[len(new_id)-1]
    print(new_id)
    return new_id

def main() :
    new_id = "=.="
    print(solution(new_id))

main()
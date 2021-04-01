def solution(new_id):
    answer = ''
    # 1단계
    new_id = new_id.lower()
    # 2단계
    reco = ""
    for i in new_id:
        if i.isdigit() or i.isalpha() or i == "-" or i == '.' or i == '_':
            reco += i
    # 3단계
    chk = 0
    new_id = []
    for i in reco:
        if chk:
            if i == ".":
                continue
            else:
                new_id.append(i)
                chk = 0
        else:
            if i == ".":
                chk = 1
            new_id.append(i)
    if new_id[0] == ".":
        new_id[0] = ""
    if new_id[-1] == ".":
        new_id[-1] = ""

    reco = ""
    for i in new_id :
        reco += i
    if len(reco) == 0 :
        reco = "a"
    if len(reco) >= 16 :
        reco = reco[:15]
        if reco[-1] == '.' :
            reco = reco[:-1]

    while len(reco)< 3 :
        reco = reco+reco[-1]

    return reco
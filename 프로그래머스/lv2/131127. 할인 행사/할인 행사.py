def solution(want, number, discount):
    ans = 0
    wantList = dict(zip(want, number))
    wantSet = set(want)

    for j in range(len(discount)):
        if discount[j] in wantList:
            wantList[discount[j]] -= 1
            if wantList[discount[j]] == 0:
                wantSet.remove(discount[j])

        if j >= 10:
            if discount[j-10] in wantList:
                wantList[discount[j-10]] += 1
                if wantList[discount[j-10]] == 1:
                    wantSet.add(discount[j-10])

        if len(wantSet) == 0:
            ans+=1 

    return ans

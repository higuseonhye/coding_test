def solution(user_id, banned_id):
    def match(user, ban):
        if len(user) != len(ban):
            return False
        for u, b in zip(user, ban):
            if b == '*':
                continue
            if u != b:
                return False
        return True

    def dfs(user_id, banned_id, banned_idx, used, answer):
        if banned_idx == len(banned_id):
            answer.append(used[:])
            return
        for i, user in enumerate(user_id):
            if i in used:
                continue
            if match(user, banned_id[banned_idx]):
                used.append(i)
                dfs(user_id, banned_id, banned_idx+1, used, answer)
                used.pop()

    answer = []
    used = []
    dfs(user_id, banned_id, 0, used, answer)
    return len(set(tuple(sorted(a)) for a in answer))

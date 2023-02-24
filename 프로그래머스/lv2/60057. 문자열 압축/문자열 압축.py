def solution(s):
    n = len(s)
    min_len = n
    
    # try all possible lengths of substrings
    for length in range(1, n+1):
        start = 0
        count = 1
        compressed = ""
        
        # compress the string using the current length of substrings
        while start+length <= n:
            substr = s[start:start+length]
            next_substr = s[start+length:start+2*length]
            
            if substr == next_substr:
                count += 1
            else:
                if count > 1:
                    compressed += str(count)
                compressed += substr
                count = 1
            
            start += length
        
        if count > 1:
            compressed += str(count)
        compressed += s[start:]
        
        # update the minimum length of the compressed string found so far
        min_len = min(min_len, len(compressed))
    
    return min_len

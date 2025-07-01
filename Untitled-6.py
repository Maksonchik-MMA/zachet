def reverseStr(s, k):
    result = []
    for i in range(0, len(s), 2*k):
        
        result.append(s[i:i+k][::-1] + s[i+k:i+2*k])
    return ''.join(result)
# Примеры использования 
print(reverseStr("abcdefg", 2))
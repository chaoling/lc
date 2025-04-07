'''
### 🔹 Problem: **Custom String Compression**

**Difficulty**: Easy/Medium

---

#### **Description**

Given a string `s` consisting of uppercase letters and digits, compress it using the following custom rule:

For each **consecutive group of identical characters**, replace the group with the **number of occurrences followed by the character**.

For example:
- `"AAABBC111"` → `"3A2B1C31"`

The function should return the compressed string.

---

#### **Constraints**
- `1 <= s.length <= 10^4`
- `s` consists only of uppercase English letters and digits (`A-Z`, `0-9`)

---

#### **Example 1**

**Input**:  
`s = "AAABBC111"`

**Output**:  
`"3A2B1C31"`

---

#### **Example 2**

**Input**:  
`s = "A"`

**Output**:  
`"1A"`

---

#### **Function Signature**

```python
def compress_string(s: str) -> str:
    pass
```

---

#### **Follow-up**
How would you modify your function if the compression only applied when it reduces the string's length?
'''
def compress_string(s: str) -> str:
    '''
    using a pointer to scan the original str and make the compressed version along the way
    AAABBC11
    '''
    if not s:
        return ""
    res = [] # store the compressed one into a mutable list first
    n = len(s)
    pre = s[0]
    cnt = 1
    for i in range(1,n):
        if s[i] == pre:
            cnt += 1
        else:
            
            res.append(str(cnt))
            res.append(pre)
            pre = s[i]
            cnt = 1
    if cnt:
        res.append(str(cnt))
        res.append(pre)

    compressed =  ''.join(res)
    return compressed if len(compressed) < len(s) else s

def decompress(s: str) -> str:
    if not s:
        return ""
    res = [] # store the compressed one into a mutable list first
    n = len(s)
    assert n > 1
    i = 0
    while i < n:
        num_str = ''
        while i < n and s[i].isdigit():
            num_str += s[i]
            i += 1
        if i < n:
            res.append(s[i] * int(num_str))
            i += 1
    
    return ''.join(res)

if __name__ == "__main__":
    origin = "AAAAAAAAAAA222211100AAA"
    r = compress_string(origin)
    d =decompress(r)
    print (r,d)
    assert origin == d
    #TODO: how to handle numbers as char? like 12A 42 31 20 3A without deliminators? 


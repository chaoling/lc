'''
71. Simplify Path
Medium
You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. Your task is to transform this absolute path into its simplified canonical path.

The rules of a Unix-style file system are as follows:

A single period '.' represents the current directory.
A double period '..' represents the previous/parent directory.
Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
Any sequence of periods that does not match the rules above should be treated as a valid directory or file name. For example, '...' and '....' are valid directory or file names.
The simplified canonical path should follow these rules:

The path must start with a single slash '/'.
Directories within the path must be separated by exactly one slash '/'.
The path must not end with a slash '/', unless it is the root directory.
The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.
Return the simplified canonical path.

 

Example 1:

Input: path = "/home/"

Output: "/home"

Explanation:

The trailing slash should be removed.

Example 2:

Input: path = "/home//foo/"

Output: "/home/foo"

Explanation:

Multiple consecutive slashes are replaced by a single one.

Example 3:

Input: path = "/home/user/Documents/../Pictures"

Output: "/home/user/Pictures"

Explanation:

A double period ".." refers to the directory up a level (the parent directory).

Example 4:

Input: path = "/../"

Output: "/"

Explanation:

Going one level up from the root directory is not possible.

Example 5:

Input: path = "/.../a/../b/c/../d/./"

Output: "/.../b/d"

Explanation:

"..." is a valid name for a directory in this problem.

 

Constraints:

1 <= path.length <= 3000
path consists of English letters, digits, period '.', slash '/' or '_'.
path is a valid absolute Unix path.
'''
class Solution:
    def simplifyPath(self, path: str) -> str:
        stk =[]
        tokens = path.split('/')
        for token in tokens:
            if token == '' or token == '.':
                continue
            elif token == "..":
                if stk:
                    stk.pop()
            else:
                stk.append(token)
        return '/'+'/'.join(stk)
    
    def simplifyPath_complex(self, path: str) -> str:
        '''
        ds: stack
        algo: check the following rules:
        1) start with /: bail early if not
        2) when encounter /, check the stack, if the last item pushed is a 
           / already, skip it and continue
        3) when encounter ., check how many consequtive . follows it,
           if zero, skip it, if 1, pop all until previous
           /, contine, if more than 1, push all . as is onto
           the stack and contiue...
        4) if / is the last char, ignor it unless / is 
           the only char in the path
        '''
        n = len(path)
        if n == 1:
            return '/'
        stk = ['/'] #path always start with '/'
        tmp = [] # store the '.'
        for s in path[1:]:
            if s != '.' and tmp:
                if s != '/':
                    stk += tmp
                    tmp = []
                else:
                    n = len(tmp)
                    if n == 1:
                        tmp = [] #ignore
                    elif n == 2:
                        for _ in range(2):
                            while stk and stk.pop() != '/':
                                continue
                        stk.append('/')
                        tmp = []
                    else: # n >=3
                        stk += tmp
                        tmp = []

            if s == '/':
                if stk[-1] == '/':
                    continue
                else:
                    stk.append(s)
            elif s == '.' and stk[-1] == '/':
                tmp.append(s)
            else:
                stk.append(s)
        # if there are any . left in the stack
        if tmp:
            n = len(tmp)
            if n == 1:
                tmp = []
            elif n == 2:
                for _ in range(2):
                    while stk and stk.pop() != '/':
                        continue
                stk.append('/')
                tmp = []
            else: # n >=3
                stk += tmp
                tmp = []
        # if there are any / left in the stack
        if stk[-1] == '/' and len(stk) > 1:
            stk.pop()
        return ''.join(stk)
# test
if __name__ == "__main__":
    s = Solution()
    print(s.simplifyPath("/a//b////c/d//././/..")) # "/a/b/c/d"
    print(s.simplifyPath("/../")) # "/"
    print(s.simplifyPath("/home/")) # "/home"
    print(s.simplifyPath("/home//foo/")) # "/home/foo"
    print(s.simplifyPath("/home/user/Documents/../Pictures")) # "/home/user/Pictures"
    print(s.simplifyPath("/../")) # "/"
    print(s.simplifyPath("/.../a/../b/c/../d/./")) # "/.../b/d"
    print(s.simplifyPath("/a//b////c/d//././/..")) # "/a/b/c/d/"
    print(s.simplifyPath("/..hidden")) # "/..hidden"
    print(s.simplifyPath("/hello../world")) # "/hello../world"
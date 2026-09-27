# Last updated: 26/09/2026, 21:47:20
1class Solution:
2    def isValid(self, s: str) -> bool:
3        pilha = []
4
5        pares = {
6            ')': '(',
7            ']': '[',
8            '}': '{'
9        }
10
11        for caractere in s:
12            if caractere in "([{":
13                pilha.append(caractere)
14
15            else:
16                if not pilha:
17                    return False
18
19                if pilha[-1] != pares[caractere]:
20                    return False
21
22                pilha.pop()
23
24        return len(pilha) == 0
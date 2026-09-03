# Last updated: 03/09/2026, 14:54:57
1class Solution:
2    def romanToInt(self, s: str) -> int:
3        valores = {
4            "I": 1,
5            "V": 5,
6            "X": 10,
7            "L": 50,
8            "C": 100,
9            "D": 500,
10            "M": 1000
11        }
12
13        resultado = 0
14
15        for i in range(len(s)):
16            if i < len(s) - 1 and valores[s[i]] < valores[s[i + 1]]:
17                resultado -= valores[s[i]]
18            else:
19                resultado += valores[s[i]]
20
21        return resultado
22        resultado = 0
23
24        for i in range(len(s)):
25            if i < len(s) - 1 and valores[s[i]] < valores[s[i + 1]]:
26                resultado -= valores[s[i]]
27            else:
28                resultado += valores[s[i]]
29
30        return resultado
# Last updated: 22/10/2026, 23:47:54
1
2class Solution:
3    def generateMatrix(self, n: int) -> list[list[int]]:
4        matrix = [[0] * n for _ in range(n)]
5
6        top, bottom = 0, n - 1
7        left, right = 0, n - 1
8        num = 1
9
10        while top <= bottom and left <= right:
11            # Esquerda para direita
12            for col in range(left, right + 1):
13                matrix[top][col] = num
14                num += 1
15            top += 1
16
17            # Cima para baixo
18            for row in range(top, bottom + 1):
19                matrix[row][right] = num
20                num += 1
21            right -= 1
22
23            # Direita para esquerda
24            if top <= bottom:
25                for col in range(right, left - 1, -1):
26                    matrix[bottom][col] = num
27                    num += 1
28                bottom -= 1
29
30            # Baixo para cima
31            if left <= right:
32                for row in range(bottom, top - 1, -1):
33                    matrix[row][left] = num
34                    num += 1
35                left += 1
36
37        return matrix
38
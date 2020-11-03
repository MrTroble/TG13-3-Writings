using LinearAlgebra

H = [3, 3, 4]
E = [7, 3, 4]
G = [3, 7, 4]
F = [7, 7, 4]
A = [10, 0, 0]
B = [10, 10, 0]

HE = norm(H - E)
AB = norm(A - B)
EA = norm(E - A)

TFA = HE * EA
TFB = ((AB - HE) * EA) / 2

GSMT = (TFA + TFB) * 4
print(GSMT)
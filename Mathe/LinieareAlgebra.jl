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

trapez(a, b, h) = 0.5h * (a + b)

OM(a, b) = 0.5(a + b)

MU = OM(A, B)
MO = OM(E, F)

println(MU)
println(MO)

HO = norm(MU - MO)
println(HO)

Atrap = trapez(AB, EA, HO)
println(Atrap)

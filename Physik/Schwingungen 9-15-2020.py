import math
import plot


def v(t):
    return -0.025 * math.pi * math.sin(math.pi * t)


def s(t):
    return 0.025 * math.cos(math.pi * t)


def a(t):
    return -0.025 * math.pi**2 * math.cos(math.pi * t)


print(a(1))

plot.plotovertime([
    a,
    v,
    s,
], 1000, 0.01)
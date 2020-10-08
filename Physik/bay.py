import math
import plot


def function(x):
    return 8 * math.cos(4 * math.pi * x + math.pi) + 10


def function2(x):
    return -32 * math.pi * math.sin(4 * math.pi * x + math.pi)


def perhour(x):
    return x / 24


print(perhour(function2(-1 / 8)))
print(perhour(function2(18 / 24)))
print(perhour(function2(14 / 24)))

plot.plotovertime([function, function2], 1000, 0.001)
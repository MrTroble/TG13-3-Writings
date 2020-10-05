import math
import plot


def function(x):
    return 8 * math.cos(4 * math.pi * x + math.pi) + 10


plot.plotovertime([function], 1000, 0.001)
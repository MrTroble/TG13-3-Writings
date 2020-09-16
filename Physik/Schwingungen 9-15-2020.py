import math
import matplotlib.pyplot as plot


def v(t):
    return -0.025 * math.pi * math.sin(math.pi * t)


def s(t):
    return 0.025 * math.cos(math.pi * t)


def a(t):
    return -0.025 * math.pi**2 * math.cos(math.pi * t)


ts = []
vs = []
at = []
ss = []
samples = 10000
for x in range(samples):
    ct = x * 0.001
    ts.append(ct)
    vs.append(v(ct))
    ss.append(s(ct))
    at.append(a(ct))

plot.plot(ts, vs)
plot.plot(ts, ss)
plot.plot(ts, at)
plot.show()
# Induktion rotierende Spule ABI 1998

$A = 40cm^2$

$N = 500$

Messreihe:

| f in Hz          | 16   | 22   | 28   | 36   |
| ---------------- | ---- | ---- | ---- | ---- |
| $\hat{U}_i$ in V | 0.34 | 0.46 | 0.59 | 0.75 |

![test](Induktion%20rotierende%20Spule%20ABI%201998.png)

Propotionalitätsfaktor: $k = 0.02$

## B

$k = 2 \cdot \pi \cdot N \cdot A \cdot B$

$\Phi(t) = B \cdot A \cdot \cos(\omega t)$

$\Phi'(t) = -B \cdot A \cdot \omega \sin(\omega t)$

$U_i(t) = -N \Phi'(t)$

$U_i(t) = N \cdot B \cdot A \cdot \omega \sin(\omega t)$

Für $\hat{U_i}$ gilt $\sin(\omega t) = 1$

Somit $\hat{U_i} = N \cdot B \cdot A \cdot \omega$

wobei $\omega = 2\pi$ da $\omega = 2\pi \cdot f$

$\hat{U_i} = 2\pi \cdot N \cdot B \cdot A \cdot f$

$k = \dfrac{\hat{U_i}}{f}$

$B = \dfrac{k}{2 \cdot \pi \cdot N \cdot A}$

$B = \dfrac{0.02}{2 \cdot \pi \cdot 500 \cdot 0.04m^2}$

$B = 1.59 \cdot 10^{-3}$

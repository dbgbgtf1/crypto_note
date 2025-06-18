from typing import Optional, Tuple

# 椭圆曲线参数
p = 11
a = 4
b = 4

Point = Optional[Tuple[int, int]]  # 可以为 None（表示无穷远点）

def inverse_mod(k: int, p: int) -> int:
    return pow(k, -1, p)

def point_add(P: Point, Q: Point) -> Point:
    if P is None:
        return Q
    if Q is None:
        return P
    
    x1, y1 = P
    x2, y2 = Q
    
    if x1 == x2 and (y1 + y2) % p == 0:
        return None  # P + (-P) = O

    if P != Q:
        m = ((y2 - y1) * inverse_mod(x2 - x1, p)) % p
    else:
        if y1 == 0:
            return None
        m = ((3 * x1 * x1 + a) * inverse_mod(2 * y1, p)) % p
    
    x3 = (m * m - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p
    return (x3, y3)

def point_double(P: Point) -> Point:
    return point_add(P, P)

def scalar_mult(k: int, P: Point) -> Point:
    result = None
    addend = P

    while k:
        if k & 1:
            result = point_add(result, addend)
        addend = point_double(addend)
        k >>= 1
    return result

def point_neg(P: Point) -> Point:
    if P is None:
        return None
    x, y = P
    return (x, (-y) % p)

def point_sub(P: Point, Q: Point) -> Point:
    return point_add(P, point_neg(Q))

# 已知参数
G = (0, 2)
d = 4
C0 = (8, 8)
C2 = (6, 7)

# 解密过程：M = C2 - d*C0
# dC0 = scalar_mult(d, C0)
# M = point_sub(C2, dC0)
M = point_sub((6, 7), (1, 8))

# print(f"d * C0 = {dC0}")
print(f"M = C2 + dC0 = {M}")

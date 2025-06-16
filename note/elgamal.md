## 简介

标准的ElGamal是一对多的模型
Alice公开自己的公钥, 任何人可以给Alice加密发消息, 而Alice用自己的私钥解密

## 操作流程

### 密钥生成(Alice):

选择素数p以及p的原根g
随机选择私钥 x 属于[1, p-2]
公钥 y = g^{x} mod p

> 其中p需为安全素数, 即满足p = 2q + 1(q也为素数)
> 且g^{q} === 1 (mod p)

### 加密发送(Bob)

明文m, 随机选择临时密钥 k 属于[1, p-2]

c1 = g^{k} mod p
c2 = m * (y^{k}) mod p

发送密文对(c1, c2)

### 解密(Alice)

计算共享密钥 s = c1^{x}mod p
计算 s^(-1) mod p
> 即s的模逆元
计算明文 m = c2 * s^(-1) mod p

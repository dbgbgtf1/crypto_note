直接就能用的代码, 理论上背住就行了

```c
#include <stdint.h>
#include <stdio.h>
#include <string.h>

// 初始化 S-box 的长度
#define SBOX_LENGTH 256

// 初始化 S-box 和密钥调度算法 (KSA)
void
rc4_init (uint8_t *state, const uint8_t *key, int keylen)
{
  int i, j = 0;
  uint8_t temp;

  // 初始化 S-box 为 0-255
  for (i = 0; i < SBOX_LENGTH; i++)
    {
      state[i] = i;
    }

  // 密钥调度算法 (KSA)
  for (i = 0; i < SBOX_LENGTH; i++)
    {
      j = (j + state[i] + key[i % keylen]) % SBOX_LENGTH;
      // 交换 state[i] 和 state[j]
      temp = state[i];
      state[i] = state[j];
      state[j] = temp;
    }
}

// 生成密钥流并加密/解密数据 (PRGA)
void
rc4_crypt (uint8_t *state, const uint8_t *indata, uint8_t *outdata, int length)
{
  int i = 0, j = 0, k;
  uint8_t temp;

  for (k = 0; k < length; k++)
    {
      i = (i + 1) % SBOX_LENGTH;
      j = (j + state[i]) % SBOX_LENGTH;

      // 交换 state[i] 和 state[j]
      temp = state[i];
      state[i] = state[j];
      state[j] = temp;

      // 生成伪随机字节
      uint8_t rnd = state[(state[i] + state[j]) % SBOX_LENGTH];

      // 输出密文 = 明文 XOR 密钥流
      outdata[k] = indata[k] ^ rnd;
    }
}

// 打印十六进制数据
void
print_hex (const uint8_t *data, int length)
{
  for (int i = 0; i < length; i++)
    {
      printf ("%02X ", data[i]);
    }
  printf ("\n");
}

// 示例
int
main ()
{
  // 示例密钥
  const uint8_t key[] = "SecretKey";
  int keylen = strlen ((const char *)key);

  // 明文
  const uint8_t plaintext[] = "Hello, RC4 Encryption!";
  int datalen = strlen ((const char *)plaintext);

  uint8_t state[SBOX_LENGTH];
  uint8_t ciphertext[256];
  uint8_t decrypted[256];

  // 加密
  rc4_init (state, key, keylen);
  rc4_crypt (state, plaintext, ciphertext, datalen);

  printf ("Plaintext: %s\n", plaintext);
  printf ("Ciphertext (hex): ");
  print_hex (ciphertext, datalen);

  // 解密（重新初始化 state）
  rc4_init (state, key, keylen);
  rc4_crypt (state, ciphertext, decrypted, datalen);

  decrypted[datalen] = '\0'; // 添加字符串结尾
  printf ("Decrypted: %s\n", decrypted);

  return 0;
}
```

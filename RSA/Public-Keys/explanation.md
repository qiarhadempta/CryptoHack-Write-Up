# Public Keys
<img width="1608" height="489" alt="image" src="https://github.com/user-attachments/assets/04809f96-f9fb-4238-ad77-ca404d1eff0d" />

Public keys used in RSA are n (which is a product of two prime numbers p & q), and e (which is a public exponent).  
Here we are given some values:

``` bash
e = 65537
p = 17
q = 23
m = 12
```
and we are asked the ciphertext of the message (m).

Here are the following step:
1. First, we have to find n by this operation: n = p * q = 17 * 23 = 391
2. After n is found, then we can encrypt the message by c = m^e mod n.
   c = 12^65537 mod 391 = 301
3. Check the python script [here](https://github.com/qiarhadempta/CryptoHack-Write-Up/blob/main/RSA/Starter/Public-Keys/solver.py)

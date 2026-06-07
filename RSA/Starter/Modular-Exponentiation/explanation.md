# Modular Exponentiation
<img width="1467" height="630" alt="image" src="https://github.com/user-attachments/assets/19e90043-e66a-477a-b2af-ed827dc8dc77" />

## Self explanation of what I've learned from this module 
RSA relies heavily on modular exponentiation. Take an example for encrypting a message, the mathematical operation is 
``` bash
c = m^e mod n
```
and for decrypting a message, the mathematical behind it is  
``` bash
m = c^d mod n
```
Later, I'll explain what these numbers mean. It's good to know that this modular exponentiation helps us to build a `trapdoor function`,
which means it's easy to compute in one direction, but it's extremely hard to reverse it back. For this challenge, I made a [python script](https://github.com/qiarhadempta/CryptoHack-Write-Up/blob/main/RSA/Starter/Modular-Exponentiation/solver.py) using 
`pow(base, exponent, modulus)` to solve it

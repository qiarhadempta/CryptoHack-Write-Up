# RSA Signature

<img width="1590" height="736" alt="image" src="https://github.com/user-attachments/assets/5e4d0157-df7d-4489-8c1e-e243b5c7e4f7" />

## Self explanation of what I've learnt
Signature is a mathematical scheme used to verify the authenticity and integrity of a digital message or document. In RSA, these process break down into:
1. We encrypt the message (m) with our receiver's public key
   ``` bash
   c = m^e mod n
   ```
2. To sign the message, calculate the message's hash: `H(m) ` and encrypt it with our private key
   ``` bash
   S = H(m)^d mod n
   ```
3. Later on, the receiver calculate the hash from the message using our private key
   ``` bash
   H(m)' = S^e mod n
   ```
4. If H(m) = H(m)', the signature is VALID. The message is proven to be authentic and completely unchanged.

For the solution of the challenge above, check the python script [here](https://github.com/qiarhadempta/CryptoHack-Write-Up/blob/main/RSA/RSA-Signatures/solver.py) 

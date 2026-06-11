# Private Keys
<img width="1472" height="742" alt="image" src="https://github.com/user-attachments/assets/17e0dd03-8293-4394-9025-3f02ac81295d" />

## Self Explanation on What I've Learnt
Unlike the public key where we used n and e, here, we used n and d as the private key. 

d is modular inverse of e mod phi. So to find d with python, we can compute it by:
``` bash
d = pow(e, -1, phi)
```

Check the python script [here]()

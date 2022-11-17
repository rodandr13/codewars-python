"""
Hector the hacker has stolen some information, but it is encrypted.
In order to decrypt it, he needs to write a function that will generate
a decryption key from the encryption key which he stole (it is in hexadecimal).
To do this, he has to determine the two prime factors P and Q
of the encyption key, and return the product (P-1) * (Q-1).
"""


def find_key(encryption_key):
    n = int(encryption_key,16)
    for i in range(2,int(n**.5)+1):
        if not n%i:
            return (i-1)*(n//i-1)


def premier_entre_eux(a, b):
    if a > b:
        a, b = b, a
    for i in range(2, a + 1):
        if a % i == 0 and b % i == 0:
            return False
    return True

def element_e(phi_n):
    for e in range(2, phi_n):
        if premier_entre_eux(e, phi_n):
            return e

def cryptage(m, e, n):
    return pow(m, e, n)

m = int(input("donner le message a crypter : "))
p = int(input("donner p : "))
q = int(input("donner q : "))

n = p * q
phi_n = (p - 1) * (q - 1)

e = element_e(phi_n)

m_cry = cryptage(m, e, n)

print(n)
print(e)
print(m_cry)

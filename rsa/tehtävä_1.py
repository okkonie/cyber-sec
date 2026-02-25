p = 11
q = 13
n = p * q

# Eulerin φ-funktion tulos: φ(n) = (p − 1)(q − 1)
e_n = (p - 1) * (q - 1)

a = 0
b = 0

# Valitaan a:ksi ensimmäinen alkuluku, jolla ei voida jakaa φ(n) 
# tulosta tasan eli ratkaistaan a yhtälöstä syt(a, φ(n)) = 1
for num in range(2,e_n):
  is_prime = True
  for i in range(2,num):  
    if (num % i == 0):
      is_prime = False
  if is_prime and e_n % num != 0:
    a = num
    break

# Etsitään luku b, mikä toteuttaa yhtälön ab ≡ 1 (mod φ(n))
for i in range(e_n):
  if((a * i) % e_n == 1):
    b = i
    break

print("a =", a)
print("b =", b)
from fraction import simplification as simp, add, multi

print("Bonjours je suis Khayyam! \nEcrivez votre nom de famille avec les lettre du scrable et je ferrais de même :\n")

def ask_name():
  while True:
    familly_name = input().upper().strip()
    if familly_name.isascii() and not ' ' in familly_name:
      print(f'Maintenant les lettres sont KHAYYAM et {familly_name}')
      return familly_name
    else:
      print("Je ne comprend pas veuillez écrire votre nom avec les lettres du scrable")

letters = 'KHAYYAM' + ask_name()

def count(chars: str):
  count = 0
  for char in chars:
    count += letters.count(char)
  return count

number_voyelles = count('AEIOUY')
number_consonns = len(letters)-number_voyelles

num1, den1 = simp(count('Y'), number_voyelles)
print(f'1) Voyelle! P(n10|v)={num1}/{den1}')

num2, den2 = simp(count('AEIOU'), number_voyelles)
print(f'2) Voyelle! P(n1|v)={num2}/{den2}')

num3, den3 = simp(count('DGMBCPFHVJQ'), number_consonns)
print(f'3) Consonne! P(n2à8|!v)={num3}/{den3}')

num4, den4 = simp(number_voyelles, len(letters))
print(f'4) P(v)={num4}/{den4}')

num51, den51 = simp(*add((1, 1), (-num2, den2), (-num1, den1)))
num52, den52 = simp(*add((1, 1), (-num4, den4)))
num53, den53 = simp(count('LNRST'), number_consonns)
num54, den54 = simp(*add((1, 1), (-num53, den53), (-num3, den3)))
print(f'5) P(n2à8|v)={num51}/{den51}\n   P(!v)={num52}/{den52}\n   P(n1|!v)={num53}/{den53}\n   P(n10|!v)={num54}/{den54}')

num6, den6 = simp(*add(multi((num4, den4), (num2, den2)), multi((num52, den52), (num53, den53))))
print(f'6) P(n1)={num6}/{den6}')

num7, den7 = simp(*multi((num4, den4), (num2, den2), (den6, num6)))
print(f'7) P(v|n1)={num7}/{den7}')
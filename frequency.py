x = input("Anna sana: ")

# Käytetyimmät sanat järjesteksysessä
word_ranking = [
  'a', 'i', 't', 'n', 'e', 's', 'l', 'o', 'k',
  'u', 'ä', 'm', 'v', 'r', 'j', 'h', 'y', 'p',
  'd', 'ö', 'g', 'b', 'f', 'c', 'w', 'å', 'q'
]

char_frequency = {}

# Kirjainten käyttö
for i in range(0, len(x)):
  if(x[i] not in char_frequency.keys()):
    char_frequency[x[i]] = 1
  else:
    char_frequency[x[i]] += 1

sorted_chars = sorted(char_frequency.items())

for j in range(0, len(x)):
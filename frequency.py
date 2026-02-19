# Suomen kielen käytetyimmät kirjaimet järjestyksessä
char_ranking = "A I T N E S L O K U Ä M V R S J H Y P D Ö G B F C W Å Q"

text = "KPIKBKOAWEE BATEZPÄEEKPBPÄÄE WBPCEEZ KEAFEÄKIGGE BHMIGVPÄKBMIZ, GEPKKIPCIZ, CEKEZ, PHVPÄKIZ, KBPVPZKEKEUBMIZ ME KPIKBWIAFFBMIZ FEOKKE. KJQCIGGPÄKJ KPIKBKOAWEE IP WBPCE FOPKIZFEEZ ÄEEWOKKEE, WEEZ FQÄIIÄÄJ BZ UABÄIÄÄP IPFJ VEEGP. KPIKBKOAWE BZ ÄOBMEOFÄIZ ME ÄEEKEWOOCIZ KEÄEUEPZBZ IKÄPVPÄKJ KPICBZ UJJÄQBPFIOFÄPIZ., ME KBPÄEEGKE OHPGKE ÄOBMEOKOVPÄIZ WJGPGGJ. QGIIZÄJ KPIKBKOAWEÄKAEKITPE GOBCEEZ BATEZPÄEEKPBPÄÄE QGHJJGKJ EGEÄUJPZ QGPVVJZ MBHCBZ KBPVIÄKE. KJVJ WPIÄKP BZ ÄEGEKKO KPIKBKOAWEFOAÄÄPGGI QFÄPEEFFBÄKBÄEGEEMEGGE."
print(text)

# Lasketaan tekstin kirjainten esiintymiskerrat
char_freq = {}
ignore = [",", ".", " "]

for ch in text:
  if ch not in ignore:
    if ch in char_freq:
      char_freq[ch] += 1
    else:
      char_freq[ch] = 1

# Järjestykseen
text_char_ranking = sorted(char_freq.items(), key=lambda item: item[1], reverse=True)

# Merkkijonoksi
text_char_ranking_string = ""
for char, amount in text_char_ranking:
  text_char_ranking_string += (char + " ")

print("\n" + char_ranking + " --- suomen kielen kirjainten yleisyys järjestyksessä")
print(text_char_ranking_string + " --- salatun viestin kirjainten yleisyys järjestyksessä")

char_pairs = []

while True:
  x = input("\nVaihda merkit: ")

  if x == "-1":
    break

  char1 = x[0]
  char2 = x[1]

  char_pairs.append((char1, char2))

  new_text = ""

  for char in text:
    if char == char1:
      new_text += char2
    elif char == char2:
      new_text += char1
    else:
      new_text += char
  
  text = new_text

  print("\n" + text)

print(char_pairs)
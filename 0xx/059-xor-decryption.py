def from_ascii(lst):
  text = map(chr, lst)
  s = ""
  for c in text:
    s += c
  return s

def sublist(l1,l2):
  return set(l1) <= set(l2)

def main():
  message = []
  with open("059-xor-decryption.txt","r") as f:
    message = (f.read()).split(",")

  message = map(lambda x: int(x.rstrip()), message)
  common = ['this', 'that', 'the', 'be', 'of', 'have']

  decrypted = ""
  for c1 in range(97,97+26):
    for c2 in range(97,97+26):
      for c3 in range(97,97+26):
        bad = 0
        key = [c1,c2,c3]
        decrypt = []
        for i in range(len(message)):
          decrypt.append(message[i] ^ key[i % 3])
        decrypt = from_ascii(decrypt)
        for word in common:
          if word not in decrypt:
            bad = 1
        if not bad:
          decrypted = decrypt
  print decrypted
  sum_of_ascii = sum(map(ord, list(decrypted)))
  print sum_of_ascii

main()
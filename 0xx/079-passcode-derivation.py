def check(pw, att):
  counter = 0
  sp = str(pw)
  sa = str(att)
  for c in sp:
    if counter < 3:
      if c == sa[counter]:
        counter += 1
  if counter != 3:
    print att
    return False
  return True


def main():
  attempts = []
  with open("079-passcode-derivation.txt") as f:
    for line in f:
      if int(line) not in attempts:
        attempts.append(int(line))
  print attempts
  # got this using pencil and paper!
  password = 73162890
  for a in attempts:
    if not check(password, a):
      print "failed! thanks to "+str(a)
      exit()
  print "success!"

main()
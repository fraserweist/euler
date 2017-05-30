def main():
  names = []
  with open("022-names.txt","r") as fh:
    for line in fh:
      names = line.split(",")

  for i in range(len(names)):
    names[i] = names[i][1:len(names[i])-1]
  names.sort()

  result = 0
  for i in range(len(names)):
    score = 0
    for char in names[i]:
      score += ord(char) - 64
    score *= i+1
    result += score
    if names[i] == "COLIN":
      print score
  print result

main()
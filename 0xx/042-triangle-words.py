def word_score(w):
  score = 0
  for c in w:
    score += ord(c) - 64
  return score

def main():
  with open("042-triangle-words.txt","r") as f:
    words = f.read().split(',')

  for i in range(len(words)):
    words[i] = words[i][1:-1]

  scores = [0]*len(words)
  for i in range(len(words)):
    scores[i] = word_score(words[i])

  maximum = max(scores)
  tri = []
  i = 1
  cur = 0
  while cur < maximum:
    cur = i*(i+1)/2
    tri.append(cur)
    i += 1

  tri_words = []
  for i in range(len(words)):
    if scores[i] in tri:
      tri_words.append(words[i])

  print tri_words, len(tri_words)

main()
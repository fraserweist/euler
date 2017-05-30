def card_val(c):
  result = [0,0]
  face = c[:1]
  suit = c[1:]
  result[1] = suit
  if face == 'A':
    result[0] = 14
  elif face == 'K':
    result[0] = 13
  elif face == 'Q':
    result[0] = 12
  elif face == 'J':
    result[0] = 11
  elif face == 'T':
    result[0] = 10
  else:
    result[0] = int(face)
  return result

def flush(suits):
  suit = suits[0]
  for i in range(1,len(suits)):
    if suits[i] != suit:
      return False
  return True

def four_kind(cards):
  for i in range(1,15):
    if cards.count(i) == 4:
      return True, i
  return False, 0

def three_kind(cards):
  flag = 0
  max_i = 0
  for i in range(1,15):
    if cards.count(i) == 2:
      return False, max_i
    if cards.count(i) == 3:
      flag = 1
      max_i = i
  return flag, max_i

def pairs(cards):
  ps = 0
  max_i = 0
  for i in range(1,15):
    if cards.count(i) == 2:
      ps += 1
      max_i = max(i, max_i)
  return ps, max_i

def full_house(cards):
  max_i = 0
  for i in range(1,15):
    if cards.count(i) == 1 or cards.count(i) == 4:
      return False,0
    if cards.count(i) == 3:
      max_i = i
  return True, max_i

def straight(cards):
  for i in range(1,len(cards)):
    if cards[i]-cards[i-1] != 1:
      return False
  return True

def hand_val(h):
  rank = 0
  cards = sorted([hand[0] for hand in h])
  suits = [hand[1] for hand in h]
  high_card = max(cards)
  if flush(suits):
    if straight(cards):
      if high_card == 14:
        rank = 10
      else:
        rank = 9
    else:
        rank = 6
  four, fhigh = four_kind(cards)
  if four:
    if rank < 8:
      rank = 8
      high_card = fhigh
  full, fhhigh = full_house(cards)
  if full:
    if rank < 7:
      rank = 7
      high_card = fhhigh
  if straight(cards):
    if rank < 5:
      rank = 5
      high_card = max(cards)
  three, thigh = three_kind(cards)
  if three:
    if rank < 4:
      rank = 4
      high_card = thigh
  ps, phigh = pairs(cards)
  if ps:
    if rank < ps:
      rank = ps
      high_card = phigh

  return rank*100+high_card


def main():
  hands = []
  with open("054-poker-hands.txt","r") as f:
    for line in f:
      hands.append(map(card_val,line.split()))

  for i in range(len(hands)):
    hands[i] = [hands[i][:5], hands[i][5:]]

  p1_wins = 0
  for hand in hands:
    if hand_val(hand[0]) > hand_val(hand[1]):
      p1_wins += 1

  print "player 1 wins "+str(p1_wins)+" rounds"

main()
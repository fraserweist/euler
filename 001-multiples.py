import sys

def main():

  if len(sys.argv) != 2:
    print "usage:\npython 001-multiples.py n"
    quit()

  script, n = sys.argv
  result = 0

  for i in range(int(n)):
    if i % 3 == 0 or i % 5 == 0:
      result += i

  print "result = "+str(result)

main()
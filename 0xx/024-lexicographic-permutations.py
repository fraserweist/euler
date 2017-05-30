import itertools

def nth(iterable, n, default=None):
  "Returns the nth item or a default value"
  return next(itertools.islice(iterable, n, None), default)

def main():
  result = itertools.permutations(range(10))
  print nth(result, 999999)

main()
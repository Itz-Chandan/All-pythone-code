values = [1, 2, 3, 4, 10, 20, 50]

def x_ify (n: int)  -> str:
  return n * 'x'

mapped = map(str, values)

print(list(mapped))
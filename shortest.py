def shortest(lst):
  shorty = lst[0]

  for string in lst:
    if len(string) < len(shorty):
      shorty = string

  return shorty

print(shortest(['Gerrit', 'Dave', 'Joe']))
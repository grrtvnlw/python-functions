def longest(lst):
  longlong = ""

  for string in lst:
    if len(string) > len(longlong):
      longlong = string

  return longlong

print(longest(['Gerrit', 'Dave', 'Joe']))
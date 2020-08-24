def largest(lst):
  count = 0

  for n in lst:
    if n > count:
      count = n

  return count

print(largest([11, 20, 42, 97, 23, 10]))
def smallest(lst):
  count = lst[0]

  for n in lst:
    if n < count:
      count = n

  return count

print(smallest([11, 20, 42, 97, 23, 10]))
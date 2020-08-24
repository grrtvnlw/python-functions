def is_even(num):
  if num % 2 == 0:
    return True
  else:
    return False

def only_evens(lst):
  new_lst = []

  for n in lst:
    if is_even(n):
      new_lst.append(n)

  return new_lst

print(only_evens([11, 20, 42, 97, 23, 10]))
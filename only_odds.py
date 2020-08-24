def is_even(num):
  if num % 2 == 0:
    return True
  else:
    return False

def is_odd(num):
  if not is_even(num):
    return True
  else:
    return False

def only_odds(lst):
  new_lst = []

  for n in lst:
    if is_odd(n):
      new_lst.append(n)

  return new_lst

print(only_odds([11, 20, 42, 97, 23, 10]))
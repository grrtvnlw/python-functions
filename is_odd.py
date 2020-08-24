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

print(is_odd(2))
print(is_odd(3))
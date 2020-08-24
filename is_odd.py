def is_even(num):
  if num % 2 == 0:
    return True
  else:
    return False

def is_odd(num):
  return not is_even(num)

print(is_odd(2))
print(is_odd(3))
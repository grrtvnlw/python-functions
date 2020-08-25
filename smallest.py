def smallest(lst):
  # set a variable to the first number in the list
  small = lst[0]

  for number in lst:
    # for every number in the list, compare it to the first value. 
    # if the new number is smaller than the small variable, re-assign the small variable to be that number
    if number < small:
      small = number

  # return the smallest number
  return small

print(smallest([11, 20, 42, 97, 23, 10]))
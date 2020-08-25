def make_change(total_charge, payment):
  total = total_charge - payment

  bill_total = int(total_charge - payment)

  change_total = total_charge - int(total_charge)
  change_total = round(change_total, 2)

  # print(bill_total, change_total)

  return ((bills(bill_total)), (change(change_total)))

def bills(total):
  if total > 100:
    hundreds = int(total / 100)
    total -= (hundreds * 100)
  else:
    hundreds = 0

  if total > 50:
    fifties = int(total / 50)
    total -= (fifties * 50)
  else:
    fifties = 0

  if total > 20:
    twenties = int(total / 20)
    total -= (twenties * 20)
  else:
    twenties = 0

  if total > 10:
    tens = int(total / 10)
    total -= (tens * 10)
  else:
    tens = 0

  if total > 5:
    fives = int(total / 5)
    total -= (fives * 5)
  else:
    fives = 0

  if total > 1:
    singles = int(total / 1)
    total -= (singles * 1)
  else:
    singles = 0

  return (singles, fives, tens, twenties, fifties, hundreds)

def change(total):

  if total > .25:
    quarters = total / .25
    print(quarters)
    total -= (quarters * .25)
  else:
    quarters = 0
  
  if total > .10:
    dimes = total / .10
    total -= (dimes * .10)
  else:
    dimes = 0
  
  if total > .05:
    nickels = total / .05
    total -= (nickels * .05)
  else:
    nickels = 0
  
  if total > .01:
    pennies = total / .01
    total -= (pennies * .01)
  else:
    pennies = 0

print(make_change(433.59, 300.59))
Fahr = float(input('Give me a temp in Fahrenheit: '))

def f_to_c(temp):
  C = (Fahr - 32) * 5/9
  return f'Temp in Celsius: {C}'

print(f_to_c(Fahr))
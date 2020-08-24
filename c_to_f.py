Cels = float(input('Give me a temp in Celsius: '))

def c_to_f(temp):
  F = (temp * 9/5) + 32
  return f'Temp in Fahrenheit: {F}'

print(c_to_f(Cels))
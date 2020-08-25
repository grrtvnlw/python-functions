inp = float(input('Give me a temp in Celsius: '))

def c_to_f(temp):
  F = (temp * 9/5) + 32
  return F

Cels = c_to_f(inp)

print(f'Temp in Fahrenheit: {Cels}')
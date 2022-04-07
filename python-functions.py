def sum_to(num):
  sum = 0
  for n in range(1, num + 1):
    sum += n
  return sum

n = [0, 34, 6, 23, 4, 5, 600]
def largest(numbers):
  x = 0
  for n in numbers:
    if n > x:
      x = n
  return x
print(largest(n))


def occurrences(str, strr):
  x = str.count(strr)
  return x 

print(occurrences('hello', 'l'))

def product(*args):
  product = 1
  for x in args:
    product = x * product 
  return product

print(product(4, 0.5, 5))


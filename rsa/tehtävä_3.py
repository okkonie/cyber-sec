results = [None] * 5

for x in range(1,6):
  results[x-1] = None

  t = x
  for n in range(1,16):
    for i in range(1,n):
      t *= x

    if(t % 15 == 1):
      results[x-1] = n
      break

    t = x

print(results)
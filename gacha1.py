import random, bisect

def cdf(weights):
  total = sum(weights)
  result = []
  cumsum = 0
  for w in weights:
    cumsum += w
    result.append(cumsum / total)
  return result

def choice(population, weights):
  assert len(population) == len(weights)
  cdf_vals = cdf(weights)
  x = random.random()
  idx = bisect.bisect(cdf_vals, x)
  return population[idx]

box_options = ['3', '2', '1', '0']
weights = [0.029, 0.128, 0.83, 0.013]

gacha_list = []
for i in range(30):
  result = choice(box_options, weights)
  gacha_list.append(result)
  if (i+1) % 10 == 0:
    print(gacha_list)
    gacha_list = []

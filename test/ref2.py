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
    selected_list = population[idx]  # Choose a list based on weights
    return random.choice(selected_list)  # Select a random string from the chosen list

# Define box_options as lists of strings
box_options = [['A1', 'A2', 'A3'], ['B1', 'B2'], ['C1', 'C2', 'C3', 'C4'], ['D1']]
weights = [0.029, 0.128, 0.83, 0.013]

gacha_list = []
for i in range(20):
    result = choice(box_options, weights)
    gacha_list.append(result)
    if (i + 1) % 10 == 0:
        print(gacha_list)
        gacha_list = []
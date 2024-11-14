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

#일반 추출: 3성, 2성, 1성, 에고
box_options = ['3', '2', '1', '0']
weights = [0.029, 0.128, 0.83, 0.013]

#10회 추출: 3성, 2성, 에고
box_options_end = ['3', '2', '0']
weights_end = [0.029, 0.958, 0.013]

gacha_list = [] #10회 리스트
gacha_sum = [] #30회 리스트
rare_drop = False #에고나 3성 카운터 플래그

print('<림버스 컴퍼니 리세마라 모의 추출>')

for i in range(30):
  if i == 19 and rare_drop == False: #20번째 추출 이내 3성이나 에고 확정
    result = random.choice(['0', '3'])
  elif i % 10 == 9: #10회 이상 추출 시 2성 이상 획득
    result = choice(box_options_end, weights_end)
    if result in ['0', '3']:
      rare_drop = True
  else:
    result = choice(box_options, weights)
    if result in ['0', '3']:
      rare_drop = True
  gacha_list.append(result)
  if (i+1) % 10 == 0:
    print(gacha_list)
    gacha_sum.append(gacha_list)
    gacha_list = []

result = [item for sublist in gacha_sum for item in sublist]
onestar = result.count('1') * 3
twostar = result.count('2')
threestar = result.count('3')
ego = result.count('0')

print(f'리세 결과: 끈 {onestar}개, 2성 {twostar}개, 3성 {threestar}개, 에고 {ego}개 획득!')
if int(threestar) >= 3:
  print('인격 구성 괜찮으면 진행하세요!')
elif int(threestar) == 2:
  print('최애케 있으면 가세요')
else:
  print('다시 하는 게 좋겠네요...')
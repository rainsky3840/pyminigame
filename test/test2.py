import csv, random, bisect

onestar_num_list = []
twostar_num_list = []
threestar_num_list = []
ego_num_list = []

with open('data.csv', 'r', encoding='utf-8') as file:
  csv_reader = csv.DictReader(file)
  # next(csv_reader) #skip first row
  for row in csv_reader:
    # print(row['수감자'], row['소속'], row['분류'], row['점수'])
    # print(row)
    if row['분류'] == '1':
      name = row['소속'] + ' ' + row['수감자']
      onestar_num_list.append(name)
    elif row['분류'] == '2':
      name = row['소속'] + ' ' + row['수감자']
      twostar_num_list.append(name)
    elif row['분류'] == '3':
      name = row['소속'] + ' ' + row['수감자']
      threestar_num_list.append(name)
    else:
      name = row['소속'] + ' ' + row['수감자']
      ego_num_list.append(name)

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
    return random.choice(selected_list)

box_options = [onestar_num_list, twostar_num_list, threestar_num_list, ego_num_list]
weights = [0.029, 0.128, 0.83, 0.013]

box_options_end = [threestar_num_list, twostar_num_list, ego_num_list]
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
onestar_num = result.count('1') * 3
twostar_num = result.count('2')
threestar_num = result.count('3')
ego_num = result.count('0')

print(f'>> 리세 결과: 끈 {onestar_num}개, 2성 {twostar_num}개, 3성 {threestar_num}개, 에고 {ego_num}개 획득!')
if int(threestar_num) >= 3:
  print('>> 인격 구성 괜찮으면 진행하세요!')
elif int(threestar_num) == 2:
  print('>> 최애케 있으면 가세요')
else:
  print('>> 다시 하는 게 좋겠네요...')
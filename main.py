import csv, random, bisect

onestar_list = []
twostar_list = []
threestar_list = []
ego_list = []

with open('data.csv', 'r', encoding='utf-8') as file:
  csv_reader = csv.DictReader(file)
  # next(csv_reader) #skip first row
  for row in csv_reader:
    # print(row['수감자'], row['소속'], row['등급'], row['점수'])
    # print(row)
    if row['등급'] == '1':
      onestar_list.append(row)
    elif row['등급'] == '2':
      twostar_list.append(row)
    elif row['등급'] == '3':
      threestar_list.append(row)
    else:
      ego_list.append(row)

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

box_options = [threestar_list, twostar_list, onestar_list, ego_list]
weights = [0.029, 0.128, 0.83, 0.013]

box_options_end = [threestar_list, twostar_list, ego_list]
weights_end = [0.029, 0.958, 0.013]

box_options_new = [threestar_list, ego_list]
weights_new = [0.7, 0.3]

ten_name = [] #10회 리스트
thirty_name = [] #30회 리스트: 이름만
thirty_tier = [] #30회 리스트: 티어만
rare_drop = False #에고나 3성 카운터 플래그

print('<림버스 컴퍼니 리세마라 모의 추출>', end='\n\n')

for i in range(30):
  if i == 19 and rare_drop == False: #20번째 추출 이내 3성이나 에고 확정
    result = choice(box_options_new, weights_new)
  elif i % 10 == 9: #10회 이상 추출 시 2성 이상 획득
    result = choice(box_options_end, weights_end)
    if result['등급'] in ['0', '3']:
      rare_drop = True
  else:
    result = choice(box_options, weights)
    if result['등급'] in ['0', '3']:
      rare_drop = True
  
  if (result['등급']) in ['0', '2', '3']: #2성 이상만 표시
    ten_name.append(result['소속'] + ' ' + result['수감자'])
  thirty_tier.append(result['등급'])

  if (i+1) % 10 == 0:
    print(f'* {i//10+1}회: {ten_name}', end = '\n\n')
    thirty_name.append(ten_name)
    ten_name = []

# aggregate = [item for sublist in thirty_tier for item in sublist]
onestar_num = thirty_tier.count('1') * 3
twostar_num = thirty_tier.count('2')
threestar_num = thirty_tier.count('3')
ego_num = thirty_tier.count('0')

print(f'>> 리세 결과: 끈 {onestar_num}개, 2성 {twostar_num}개, 3성 {threestar_num}개, 에고 {ego_num}개 획득!')
if int(threestar_num) >= 3:
  print('>> 인격 구성 괜찮으면 진행하세요!')
elif int(threestar_num) == 2:
  print('>> 최애캐 있으면 가세요')
else:
  print('>> 다시 하는 게 좋겠네요...')

# file.close()
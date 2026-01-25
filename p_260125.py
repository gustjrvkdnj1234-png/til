## 딕셔너리 이해, 딕셔너리 안에 값을 리스트로 이해

black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]

user_list = [
    {'company' : 'Deckow-Crist', 'name' : 'Ervin Howell'},
    {'company' : 'Romaguera-Jacobson', 'name' : 'Clementine Bauch'},
    {'company' : 'Keebler LLC', 'name' : 'Chelsey Dietrich'},
    {'company' : 'Considine-Lockman', 'name' : 'Mrs. Dennis Schulist'},
    {'company' : 'Johns Group', 'name' : 'Kurtis Weissnat'},
    {'company' : 'Hoeger LLC', 'name' : 'Clementina DuBuque'}
]

def create_user(user_list):
    censored_user_list = {}
    for user in user_list:
        if censorship(user):
            if user['company'] not in censored_user_list:
                censored_user_list[user['company']] = [user['name']]
            else :
                censored_user_list[user['company']].append(user['name'])
            
    return censored_user_list

def censorship(user):
    if user['company'] in black_list :
        print(f'{user['company']} 소속의 {user['name']} 은/는 등록할 수 없습니다')
        return False
    else:
        print('이상 없습니다')
        return True

result = create_user(user_list)
print(result)
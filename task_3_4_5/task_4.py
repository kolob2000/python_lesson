import os

def users_hobby_function(users_file: str, hobby_file: str) -> dict:
    if os.path.exists('users_hobby.txt'):
        os.remove('users_hobby.txt')
    with open(users_file, 'r', encoding='utf-8') as users:
        with open(hobby_file, 'r', encoding='utf-8') as hobby:
            while True:

                temp_hobby = hobby.readline()
                temp_users = users.readline().strip('\n')
                temp_hobby = temp_hobby if temp_hobby else str(None) + '\n'
                if temp_users == temp_hobby:
                    break
                if not temp_users:
                    return 1
                with open('users_hobby.txt', 'a', encoding='utf-8') as f:
                    f.writelines(temp_users + ': ' + str(temp_hobby))
                    

users_hobby_function('user.csv', 'hobby.csv')
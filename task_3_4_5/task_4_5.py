import os
import sys


def users_hobby_function(users_file: str, hobby_file: str) -> str:
    if os.path.exists(sys.argv[3]):
        os.remove(sys.argv[3])
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
                with open(sys.argv[3], 'a', encoding='utf-8') as f:
                    f.writelines(temp_users + ': ' + str(temp_hobby))
    return print('ok')


users_hobby_function(sys.argv[1], sys.argv[2])

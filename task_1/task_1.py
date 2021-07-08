import re

email = re.compile(r'^[\w_\.-]+@[A-Za-z\d]+\.[A-Za-z]{2,}$')  # регулярка с возможностью проверки email на поддомены
my_mail = input('Введите адрес электронной почты - ')
msg = f'Некорректный адрес электронной почты : {my_mail}'
if email.match(my_mail):
    print(my_mail)
else:
    raise ValueError(msg)
username = re.compile(r'.+?(?=@)')
domain = re.compile(r'(?<=@).+')
parsed_email = {
    'username': username.search(my_mail).group(),
    'domain': domain.search(my_mail).group(),
}
print(parsed_email)
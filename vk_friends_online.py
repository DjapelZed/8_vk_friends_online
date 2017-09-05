import vk
import getpass


APP_ID = None # Укажи ID своего Standalone-приложения


def get_user_login():
    login = input('Введите свой логин: ')
    if not login:
        print('Ты не ввел логин!')
        exit()
    return login


def get_user_password():
    print('* Пароль не будет отображаться в целях безопасности *')
    password = getpass.getpass('Введите свой пароль:')
    if not password:
        print('Ты не ввел пароль!')
        exit()
    return password


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends',
    )
    api = vk.API(session)
    friends_online_ids = api.friends.getOnline()
    friends_online = api.users.get(user_ids=friends_online_ids)
    return friends_online


def output_friends_to_console(friends_online):
    print('Из друзей сейчас онлайн: ')
    for friend in friends_online:
        print('{0} {1}'.format(friend['first_name'], friend['last_name']))


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    try:
        friends_online = get_online_friends(login, password)
    except vk.exceptions.VkAuthError as error:
        print('Неверный логин или пароль!')
        exit()

    output_friends_to_console(friends_online)

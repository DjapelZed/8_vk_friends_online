import vk
import time


APP_ID = None # Укажи ID своего Standalone-приложения


def get_user_login():
    login = input('Введите свой логин: ')
    if not login:
        print('Ты не ввел логин!')
        get_user_login()
    return login

def get_user_password():
    password = input('Введите свой пароль: ')
    if not password:
        print('Ты не ввел пароль!')
        get_user_password()
    return password


def get_online_friends(login, password):
    try:
        session = vk.AuthSession(
            app_id=APP_ID,
            user_login=login,
            user_password=password,
            scope='friends',
        )
    except:
        print('Ошибка авторизации: неверный логин или пароль!')
        get_online_friends(get_user_login(), get_user_password())
    api = vk.API(session)
    friends_online_ids = api.friends.getOnline()
    friends_online = []
    for friend in friends_online_ids:
        friends_online.append(api.users.get(user_ids=friend))
        time.sleep(0.4)
    return friends_online


def output_friends_to_console(friends_online):
    print('Из друзей сейчас онлайн: ')
    for friend in friends_online:
        print('{0} {1}'.format(friend[0]['first_name'], friend[0]['last_name']))

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)

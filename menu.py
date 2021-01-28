from hash import password
import subprocess
from database_manager import store_passwords, find_users, find_password, delete_users
import pyhibp
from pyhibp import pwnedpasswords as pw


def menu():
    print('-' * 30)
    print(('-' * 13) + 'Menu' + ('-' * 13))
    print('1. Create password')
    print('2. Find all data to an email')
    print('3. Find a password for a site')
    print('4. Delete a existing password')
    print('Q. Exit')
    print('-' * 30)
    return input(': ')


def create():
    print('Please provide the name of the site: ')
    app_name = input()
    print('Please provide a simple password : ')
    plaintext = input()
    passw = password(plaintext, app_name, 12)
    subprocess.run('clip', universal_newlines=True, input=passw)
    print('-' * 30)
    print('')
    print('Your password has now been created and copied to your clipboard: ')
    print('')
    print('-' * 30)
    pyhibp.set_user_agent(ua="Awesome application/0.0.1 (An awesome description)")
    resp = pw.is_password_breached(password=passw)
    if resp:
        print('-' * 30)
        print("Your password breached!")
        print("Your password was used {0} time(s) before.".format(resp))
    else:
        print("Your password is not breached.")
        print('-' * 30)

    user_email = input('Please provide a email address: ')
    username = input('Please provide a username (if applicable): ')

    if username is None:
        username = ''
    url = input('Please provide the url: ')
    store_passwords(passw, user_email, username, url, app_name)


def find():
    print('Please provide the name of the site: ')
    app_name = input()
    find_password(app_name)


def find_accounts():
    print('Please provide the email: ')
    user_email = input()
    find_users(user_email)


def delete():
    print('Please provide the site name that you want to delete')
    app_name = input()
    delete_users(app_name)

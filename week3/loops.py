
PASSWORD = 'abc'

def login():
    """Implement a function that prompts a 
    user for a password until the actual 
    password is entered and the user is 
    authenticated.

    Step 2: allow a maximum of three attempts.

    """
    # ask for initial password
    # while password is incorrect:
    #    tell you wrong password
    #    ask for another password
    # you are logged in
    user_password = input('password: ')
    bad_attempts = 0
    
    while ((user_password != PASSWORD)
          and (bad_attempts < 2)):
         print('wrong password')
         bad_attempts = bad_attempts + 1
         user_password = input('password: ')
    if  user_password == PASSWORD:    
        print(f'you are logged in with {bad_attempts} bad passwords entered')
    else:
        print('contact your sysadmin...locked out')

def main():
    login()

if __name__ == '__main__':
    main()
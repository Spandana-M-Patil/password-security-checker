import hashlib
import requests

def hash_password(password):
    sha_1 = hashlib.sha1(password.encode('utf-8'))
    hexa_digest = sha_1.hexdigest().upper()
    return hexa_digest 

def check_response(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    response = requests.get(url)
    res = response.status_code
    if res != 200:
        raise RuntimeError(f'Error fetching {res}')
    return response

def check_pwned(password):
    hashed_password = hash_password(password)
    prefix, suffix  = hashed_password[:5], hashed_password[5:]
    response = check_response(prefix)
    for i in response.text.splitlines():
        txt = i.split(':')
        hash, count = txt[0], txt[1]
        if hash == suffix:
            return f'{password} was found {count} times.... You should probably change your password!'
    return f'{password} was NOT found. Carry on!!'

def main():
    # get the password from the user
    user = input('Enter the password: ')
    # check if the password is pwned or not
    check = check_pwned(user)
    print(check)


if __name__ == '__main__':
    main()





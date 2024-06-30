import hashlib
import requests

def hash_password(password):
    '''
    Hash the given password using SHA-1 and return the hashed password in upper case

    parameters:
        password (str) - The password to hash

    returns:
        hashed password in upper case
    '''
    sha_1 = hashlib.sha1(password.encode('utf-8'))    # hash the password using hashlib
    hex_digest = sha_1.hexdigest().upper()     # get the hashed answer in hexadigest
    return hex_digest 

def check_response(query_char):
    '''
    It requests a pwned API to get the response

    parameters:
        query character(str): first 5 character of the hashed password

    Returns:
        requests.Response: The API response object.
        
        Raises:
        RuntimeError: If there is an error fetching data from the API.
    '''
    url = 'https://api.pwnedpasswords.com/range/' + query_char    # url to make a request
    response = requests.get(url)
    res = response.status_code
    if res != 200:
        raise RuntimeError(f'Error fetching {res}')
    return response

def check_pwned(password):
    '''
    It checks if the password is being pwned or not, if it's pwned it returns thw count that how many time it has seen in data set

    parameters:
        password(str) : User entered password

    returns:
        Message, whether it's pwned or not!
    '''
    hashed_password = hash_password(password)    # Hash the given password
    prefix, suffix  = hashed_password[:5], hashed_password[5:]   # Split hash into prefix and suffix
    response = check_response(prefix)    # Query the API with the prefix
    for i in response.text.splitlines():
        txt = i.split(':')
        hash, count = txt[0], txt[1]
        if hash == suffix:
            return f'{password} was found {count} times.... You should probably change your password!'
    return f'{password} was NOT found. Carry on!!'

def main():
    """
    Main function to prompt user for a password and check its security against known breaches.
    """
    user_password = input('Enter the password: ') # get the password from the user
    result = check_pwned(user_password) # check if the password is pwned or not
    print(result)


if __name__ == '__main__':
    main()

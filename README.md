# password-security-checker
This Python script checks the security of a password against known breaches using the Pwned Passwords API. It hashes the password locally before querying the API to ensure privacy and security.
## Installation
**1. Clone the repository:**
```bash
git clone https://github.com/Spandana-M-Patil/password-security-checker.git
```
**2. Install dependencies:**
```bash
pip install requests
```
No need to install `hashlib` manually as it conmes with python STL.
## Usage
**1. Run the Script:**
```bash
python script.py
```
2. **Enter the password when prompted**
- Enter the password that you want to check for security against the breaches.
3. **View the Output**
- The script will output whether the password was found in breaches and suggest if it should be changed.
## How it works
1. **Hashing:** The script hashes the password using SHA-1 locally.
2. **API Query:** It sends the first 5 characters of the hashed password to the pwned passwords API using k-Anonymity.
3. **Response Handling:** It checks the API response to determine whether the password has been compromised based on the hashed suffix.
## Acknowledgments
- Thanks to creators of the pwned password for providing the API service.
- Inspired to improve the security of the passwords.

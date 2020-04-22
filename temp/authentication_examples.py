import requests

# Basic Authentication request:
r = requests.post('http://pulse-rest-testing.herokuapp.com/books2',
                  data={'title': 'Anna Karenina', 'author': '111'},
                  auth=('admin', 'pass'))


# Запрос на получение токена (можно сделать один раз и потом им пользоваться.
# Так на практике чаще делают: запращивают токен и потом им пользуются вместо передачи user и password)
r_token = requests.post('http://pulse-rest-testing.herokuapp.com/api-token-auth/',
                        data={'username': 'admin', 'password': 'pass'})
print(r_token.json())
token = r_token.json()['token']
print(token)

# Token Authentication request:
r1 = requests.post('http://pulse-rest-testing.herokuapp.com/books2',
                  data={'title': 'Anna Karenina', 'author': '111'},
                  headers={'Authorization': 'Token 552589d78e17333c6e78529b18303a77c15220e3'})

header_4_token = {'Authorization': f'Token {token}'}
r1 = requests.post('http://pulse-rest-testing.herokuapp.com/books2',
                  data={'title': 'Anna Karenina', 'author': '111'},
                  headers=header_4_token)

print(r1.status_code)
print(r1.json())
print(r1.headers)


### Using Session

s = requests.Session()

# with Basic Authentication
s.auth = ('admin', 'pass')
# with Token Authentication
s.headers.update({'Authorization': f'Token {token}'})

r2 = s.get('http://pulse-rest-testing.herokuapp.com/roles2?level=100500')
print(r2.status_code)
print(r2.headers)
print(r2.text)

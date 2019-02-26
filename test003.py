from requests import put, get

#put('http://127.0.0.1:5000/todo2', data={'data': 'fuck1'}).json()

content = get('http://127.0.0.1:5000/todo4').json()
print(content)
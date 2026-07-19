import requests


url = 'https://www.ibm.com'
res = requests.get(url)
print(res.status_code)
print(res.encoding)
print(res.headers)
print(res.text[0:30])

url = 'http://httpbin.org/get'
params = {'name':'Joseph', 'ID':'123'}
res = requests.get(url, params=params)

print(res.url)
#print(res.content)
print(res.request.body)
print(res.request.headers)
print(res.status_code)
print(res.json())

payload = {'name':'Joseph', 'ID':'123'}
url_post='http://httpbin.org/post'
r_post = requests.post(url_post, data = payload)
print("post")
print(r_post.request.body)
print(r_post.json())
print(r_post.json()['form'])

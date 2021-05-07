import requests
import kuser_agent

url = 'https://www.cnblogs.com/pick/#p81'

content  = requests.get(
    url = url,
    headers = {
        'User-Agent':kuser_agent.get()
    }
).content
with open('aa.html','wb') as f:
    f.write(content)
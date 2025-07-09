import requests
from samba.dcerpc.dcerpc import response
import plotly.express as px
#Create API request

url = "https://api.github.com/search/repositories" #строка
url += "?q=language:python+sort:stars+stars:>10000" #запрос

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")
response_dict = r.json() #преобразование объекта в словарь

print(response_dict.keys())
print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")

#Анализ информации о репозиториях
repo_dicts =response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

repo_names, stars=[],[]
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

#visual

fig = px.bar(x=repo_names, y=stars)
fig.show()
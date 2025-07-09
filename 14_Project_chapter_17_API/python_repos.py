import requests
from samba.dcerpc.dcerpc import response

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


#Анализ первого репозитория
#repo_dict = repo_dicts[0]
#print(f"\nKeys: {len(repo_dict)}")
#for key in sorted(repo_dict.keys()):
#    print(key)
#print("\nSelected information about first repository:")
#print(f"Name: {repo_dict['name']}")
#print(f"Owner: {repo_dict['owner']['login']}")
#print(f"Stars: {repo_dict['stargazers_count']}")
#print(f"Repository: {repo_dict['html_url']}")
#print(f"Created: {repo_dict['created_at']}")
#print(f"Updated: {repo_dict['updated_at']}")
#print(f"Description: {repo_dict['description']}")

#All repositories
count  = 1
print("\nSelected information about first repository:")
for repo_dict in repo_dicts:
    print(f"***************** {count}. ******************\n")
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")
    print(f"--------------------------------------------\n")
    count = count + 1
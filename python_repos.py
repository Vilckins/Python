import requests
def user_request(url = 'http://api.github.com/search/repositories?q=language:Ruby&sort=stars', headers = {'Accept': 'application/vnd.github.v3+json'} ):

# Создание вызова API и сохранение ответа.
# url = 'http://api.github.com/search/repositories?q=language:Ruby&sort=stars'
# headers = {'Accept': 'application/vnd.github.v3+json'}
    r = requests.get(url, headers=headers)
    return r
r = user_request()

print(f"Status code: {r.status_code}")

# Сохранение ответа API в переменной.
response_dict = r.json()

print(f"Total repositories: {response_dict['total_count']}")

# Анализ информации о репозиториях.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:

# Анализ первого репозитория.
# repo_dict = repo_dicts[0]
# print(f"\nKeys: {len(repo_dict)}")
# for key in sorted(repo_dict.keys()):
#    print(key)

# print("\nSelected information about first reposytory:")
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
# print(f"Created: {repo_dict['created_at']}")
# print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")

# Обработка результатов.
# print(response_dict.keys())

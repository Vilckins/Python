from operator import itemgetter

import requests
from plotly import offline

# Создание вызова API и сохранение ответа.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Обработка информации о каждой статье.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Создание отдельного вызова API для каждой статьи.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Построение словаря для каждой статьи.

    try:
        submission_dict = {
            'title': response_dict['title'],
            'hh_link': f"http://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
        }
    except KeyError:
        submission_dict = {
            'title': response_dict['title'],
            'hh_link': f"http://news.ycombinator.com/item?id={submission_id}",
            'comments': 0,
        }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

repo_titles, repo_comments, repo_labels = [], [], []
for submission_dict in submission_dicts:
    repo_title = submission_dict ['title']
    repo_titles.append(repo_title)
    repo_comment = submission_dict['comments']
    repo_comments.append(repo_comment)
    repo_label = submission_dict['hh_link']
    repo_labels.append(repo_label)

# Построение визуализации
data = [{
    'type': 'bar',
    'x': repo_titles,
    'y': repo_comments,
    'hovertext': repo_labels,
    'marker': {
        'color': 'rgb(60,100,150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'Submissions hacker-news',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Comments',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='my_submissions.html')

# for submission_dict in submission_dicts:
#    print(f"\nTitle: {submission_dict['title']}")
#    print(f"Discussion link: {submission_dict['hh_link']}")
#    print(f"Comments: {submission_dict['comments']}")

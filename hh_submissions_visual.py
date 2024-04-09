from operator import itemgetter

import requests
# from plotly import offline
import plotly.graph_objects as go

# Создание вызова API и сохранение ответа.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Обработка информации о каждой статье.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:10]:
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
        pass

    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

sub_titles, sub_comments, sub_labels, sub_links = [], [], [], []
for submission_dict in submission_dicts:
    sub_title = submission_dict['title']
    sub_titles.append(sub_title)
    sub_comment = submission_dict['comments']
    sub_comments.append(sub_comment)
    sub_label = submission_dict['hh_link']
    sub_labels.append(sub_label)
    sub_link = f"<a href='{sub_label}'>{sub_title}</a>"
    sub_links.append(sub_link)

# Построение визуализации
data = [{
    'type': 'bar',
    'x': sub_links,
    'y': sub_comments,
    'hovertext': sub_links,
    'text': sub_links,
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
        'title': 'Submissions',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Comments',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'clickmode': 'event+select',
}

# fig = {'data': data, 'layout': my_layout}
# offline.plot(fig, filename='my_submissions.html')

fig = go.Figure(
    data=data,
    layout=my_layout,
)
# fig = go.Figure{'data': data, 'layout': my_layout}
fig.write_html("hh_submission_visual.html")
fig.show()

# for submission_dict in submission_dicts:
#    print(f"\nTitle: {submission_dict['title']}")
#    print(f"Discussion link: {submission_dict['hh_link']}")
#    print(f"Comments: {submission_dict['comments']}")

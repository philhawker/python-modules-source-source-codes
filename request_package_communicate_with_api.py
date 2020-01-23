import requests
import pprint

r = requests.get('https://api.dailysmarty.com/posts')
r.json()
pprint.pprint(r.json()['posts'][0])
pprint.pprint(r.json()['posts'][0]['url_for_post'])



### Practice pulling from json libraries

# daily_smarty_api = {
#   'posts' : [
#     {
#       'title': 'apis are cool',
#       'url_for_api' : 'https://www.apiland.com'
#       },
#     {
#       'title': 'apis are cool',
#       'url_for_api': 'https://www.apiland.com'
#       },
#     {
#       'title': 'apis are cool',
#       'url_for_api': 'https://www.apiland.com'
#       },
#     {
#       'title': 'apis are cool',
#       'url_for_api': 'https://www.apiland.com'
#       },
#   ]
# }

# print(daily_smarty_api['posts'])
# print(daily_smarty_api['posts'][0])
# print(daily_smarty_api['posts'][0]['title'])
# print(daily_smarty_api['posts'][0]['url_for_api'])
# print(daily_smarty_api['posts'][3])
# print(daily_smarty_api['posts'][3]['title'])
# print(daily_smarty_api['posts'][3]['url_for_api'])
# print(daily_smarty_api['posts'][0:2])
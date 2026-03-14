import urllib.request, re
req = urllib.request.Request('https://www.youtube.com/results?search_query=sri+lanka+train+ride+cinematic+4k', headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8')
items = list(set(re.findall(r'\"videoId\":\"([a-zA-Z0-9_-]{11})\"', html)))
print(items[:5])

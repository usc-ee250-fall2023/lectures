import requests
import json

def extractData(url):
  resp = requests.get(url)
  db=json.loads(resp.text)
  data = []
  for row in db:
    data.append(row["Cases"])
  return data

# Download 3 lists of cumulative totals on each day of the pandemic
confirmed = extractData('https://api.covid19api.com/total/country/united-states/status/confirmed')
recovered = extractData('https://api.covid19api.com/total/country/united-states/status/recovered')
deaths = extractData('https://api.covid19api.com/total/country/united-states/status/deaths')

# Now process the lists to show the active cases fraction/percent
# and print that result for each day.

td = 0
tc = 0
for i in range(len(confirmed)):
    td += deaths[i]
    tc += confirmed[i]
    print("Day",i,":",confirmed[i], recovered[i], deaths[i], round(td/tc,4))


import json

url = raw_input("url : ")
deckId = raw_input("deckId : ")
timings = raw_input("timings : ")

result_json = ""

slides = {}
base_url = "https://speakerdeck.com/" + deckId

timingsList = timings.split("_")

for i in range(len(timingsList)):
	originTime = timingsList[i].split("-")
	time = originTime[1]

	slides['url'] = base_url + '#' + str(i+1)
	slides['time'] = int(time)
	json_data = json.dumps(slides)

	if (i == len(timingsList)-1):
		result_json += json.dumps(slides)
	else :
		json_data = json.dumps(slides) + ", "
		result_json += json_data

videoJson = '{"title": "Agile, Git Flow; Google Play","chapters": [{"title": "Agile, Git Flow; Google Play","duration": 1495,"video": {"url": "'+ url +'"},"slides": [' + result_json + ']}]}'
parsed = json.loads(videoJson)
print json.dumps(parsed, indent=4, sort_keys=True)

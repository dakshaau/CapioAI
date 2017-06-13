import requests, json
from docx import Document
from docx.enum.dml import MSO_THEME_COLOR
from docx.shared import RGBColor
# from datetime import timedelta

class time(object):
	hours = 0
	mins = 0
	secs = 0
	millis = 0
	
	def __init__(self, seconds):
		self.hours, temp = divmod(seconds, 3600)
		self.mins, temp = divmod(temp, 60)
		self.secs, self.millis = divmod(temp, 1)
		self.millis *= 100

	def __str__(self):
		return '{:02.0f}:{:02.0f}:{:02.0f}.{:02.0f}'.format(self.hours, self.mins, self.secs, self.millis)


def getTranscript(transcriptID, APIKey):
	url = 'https://api.capio.ai/v1/speech/transcript/{}'.format(transcriptID)
	param = {'apiKey': '{}'.format(APIKey), 'word_confidence': 'true'}
	# param = json.dumps(param)
	result = requests.get(url, headers=param)
	transcript = []
	try:
		transcript = result.json()
	except:
		print('Error Code: {}'.format(result.status_code))
	return transcript

def createDocx(results, transcriptID):
	purple = RGBColor(0x64, 0x62, 0x96)
	red = RGBColor(0xfc, 0x2a, 0x35)
	doc = Document()
	results = sorted(results, key=lambda x: x['result_index'])
	for result in results:
		alternatives = result['result']
		# for index in range(bestTrans):
		scentence = alternatives[0]['alternative'][0]
		transcript = scentence['transcript']
		words = scentence['words']
		start_time = time(words[0]['from'])
		# td = timedelta(seconds=start_time)
		# print(start_time)
		para = doc.add_paragraph('')
		r = para.add_run('{}\t'.format(start_time))
		r.bold = True
		r.font.color.rgb = purple
		for word in words:
			r = para.add_run(' {}'.format(word['word']))
			if word['confidence'] < 0.75:
				r.font.color.rgb = red
		# para = doc.add_paragraph(transcript)
	doc.save('{}.docx'.format(transcriptID))
	return doc

if __name__ == '__main__':
	transcriptID = '593f237fbcae700012ba8fcd'
	APIKey = '262ac9a0c9ba4d179aad4c0b9b02120a'
	transcript = getTranscript(transcriptID, APIKey)
	doc = createDocx(transcript, transcriptID)
	

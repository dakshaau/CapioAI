import requests, json
from docx import Document

def getTrans(transcriptID, APIKey):
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

if __name__ == '__main__':
	transcript = getTrans('593f237fbcae700012ba8fcd','262ac9a0c9ba4d179aad4c0b9b02120a')
	

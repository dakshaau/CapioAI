from main import getTranscript, createDocx
from bottle import Bottle, route, get, request, run, static_file, error, redirect
import sys

capio = Bottle()

@capio.route('/')
def default():
	return

@capio.get('/transcript/<transcriptID>')
def executeMain(transcriptID):
	APIKey = request.headers.get('apiKey')
	transcript = getTranscript(transcriptID, APIKey)
	if type(transcript) is str:
		print(transcript)
		return transcript

	elif len(transcript) > 0:
		doc, path = createDocx(transcript, transcriptID)
		if doc is None:
			print(path)
			return 'Unable to create file'

		else:
			print('File saved at: {}'.format(path))
			path = path.split('{}.docx'.format(transcriptID))[0]
			return static_file('{}.docx'.format(transcriptID), root=path)


if __name__ == '__main__':
	if len(sys.argv) == 3:
		ip = sys.argv[1]
		
		try:
			assert sys.argv[2].isdigit()
		except AssertionError:
			print('\nUsage:\n')
			print('python server.py <IP> <PORT_integer>')
			exit()

		port = int(sys.argv[2])
		run(capio, host=ip, port=port, reloader=True)
	else:
		print('\nUsage:\n')
		print('python server.py <IP> <PORT_integer>')
		exit()
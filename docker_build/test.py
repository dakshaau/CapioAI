import unittest
import main

class CapioAITestCases(unittest.TestCase):

	def test_timestamp_0(self):
		'''
		Test timestamp output for 0
		'''
		t = main.timestamp(0)
		self.assertEqual(str(t), '00:00:00.00')
	
	def test_timestamp_normal(self):
		'''
		Test timestamp for random input
		'''
		t = main.timestamp(523.6987)
		self.assertEqual(str(t), '00:08:43.70')
	
	def test_timestamp_negative(self):
		'''
		Test timestamp for negative input
		'''
		t = main.timestamp(-980)
		self.assertEqual(str(t), '00:00:00.00')

	def test_timestamp_greater(self):
		'''
		Test timestamp for input greater than 1 day
		'''
		t = main.timestamp(92000)
		self.assertEqual(str(t), '01:33:20.00')

	def test_transcript_valid_keys(self):
		transcriptID = '593f237fbcae700012ba8fcd'
		APIKey = '262ac9a0c9ba4d179aad4c0b9b02120a'
		transcript = main.getTranscript(transcriptID, APIKey)
		'''
		The following assertions make sure that the results argument parameter has the following format:

		[
			{
				'result': <value>
				'result_index': <int value>
			}
		]
		'''
		self.assertIsInstance(transcript, list)
		self.assertGreater(len(transcript), 0)
		self.assertIsInstance(transcript[0], dict)
		self.assertIn('result_index', transcript[0])
		self.assertIn('result', transcript[0])
		self.assertIsInstance(transcript[0]['result_index'], int)
		self.assertGreater(transcript[0]['result_index'], -1)
		self.assertLess(transcript[0]['result_index'], len(transcript))
		for result in transcript:
			alternatives = result['result']
			'''
			The following assertions make sure that each 'result' has the following format:

			[
				{
					'alternative': [
									{
										'confidence': <float value>
									}
					]
				}
			]
			'''
			self.assertIsInstance(alternatives, list)
			self.assertIsInstance(alternatives[0], dict)
			self.assertIn('alternative', alternatives[0])
			self.assertIsInstance(alternatives[0]['alternative'], list)
			self.assertIsInstance(alternatives[0]['alternative'][0], dict)
			self.assertIn('confidence', alternatives[0]['alternative'][0])
			x = alternatives[0]['alternative'][0]['confidence']
			self.assertTrue((type(x) is float) or (type(x) is int))
			self.assertLessEqual(alternatives[0]['alternative'][0]['confidence'], 1)
			self.assertGreaterEqual(alternatives[0]['alternative'][0]['confidence'], 0)

			scentence = alternatives[0]['alternative'][0]

			'''
			The following assertions make sure that 'scentence' has the folowing format:

			{
				'words':[
						{
							'from': <float value>
							'confidence': <float value>
							'word': <string>
						}
				]
			}
			'''
			self.assertIsInstance(scentence, dict)
			self.assertIn('words', scentence)
			self.assertIsInstance(scentence['words'], list)
			self.assertIsInstance(scentence['words'][0], dict)
			self.assertIn('from', scentence['words'][0])
			self.assertIn('confidence', scentence['words'][0])
			self.assertIn('word', scentence['words'][0])
			self.assertIn('word', scentence['words'][0])
			self.assertTrue((type(scentence['words'][0]['from']) is float) or (type(scentence['words'][0]['from']) is int))
			self.assertGreaterEqual(scentence['words'][0]['from'], 0)
			self.assertTrue((type(scentence['words'][0]['confidence']) is float) or (type(scentence['words'][0]['confidence']) is int))
			self.assertLessEqual(scentence['words'][0]['confidence'], 1)
			self.assertGreaterEqual(scentence['words'][0]['confidence'], 0)
			self.assertIsInstance(scentence['words'][0]['word'], str)
	
	def test_transcript_invalid_keys(self):
		transcriptID = '593f237fbcae700012ba8fcd'
		APIKey = '8'
		transcript = main.getTranscript(transcriptID, APIKey)
		self.assertIsInstance(transcript,str)

if __name__ == "__main__":
	unittest.main()
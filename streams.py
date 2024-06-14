from time import sleep

from solo import Solo


class Streams:
	@staticmethod
	def usage():
		text = """
		Привет, если хочешь начать переписываться со мной, то тебе нужно знать парочку команд, которые доступные мне\n
Команды:
- e#d (prompt) example e#d Lorem Ipsum
- d#e (prompt) example d#e 61601065811100924810368 583210804112501155210368"""
		for l in text:
			yield l
			sleep (0.05)

	@staticmethod
	def encoding(data: str):
		data = data.replace('e#d', '')
		if not data:
			for l in "Request value not found":
				yield l
				sleep(0.05)
			return
		
		encode = Solo(data).encode_eve()
		for l in encode:
			yield l
			sleep(0.05)

	@staticmethod
	def decoding(data: str):
		data = data.replace('d#e', '')
		if not data:
			for l in "Request value not found":
				yield l
				sleep(0.05)
			return
		
		decode = Solo(data).decode_eve()
		for l in decode:
			yield l
			sleep(0.05)

	@staticmethod
	def notFound():
		for l in "Command not found":
			yield l
			sleep(0.05)
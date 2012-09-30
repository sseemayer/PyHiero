import re

class HieroFont(object):
	"""Class for a Hiero-generated bitmap font"""

	# quote-aware splitting using RE_SPLIT.findall
	RE_SPLIT = re.compile(r"'.*?'|\".*?\"|\S+")

	def __init__(self, font_file):

		self.info = {}
		self.common = {}

		self.pages = {}
		self.chars = {}

		f = open(font_file)
		
		for line in f:

			l = HieroFont.RE_SPLIT.findall(line)

			command = l[0]
			l = l[1:]
			
			vals = { k:v for k,v in ( elem.split("=") for elem in l ) }

			if command == "info":
				self.info = vals

			elif command == "common":
				self.common = vals

			elif command == "page":
				self.pages[vals['id']] = vals['file']

			elif command == "chars":
				pass

			elif command == "char":
				self.chars[vals['id']] = vals
			
			else:
				raise Error("Unknown command: {0}".format(command))

		pass

	def get_glyph(self, character):
		# TODO make pygame subclass of HieroFont and keep this class framework-agnostic!
		pass


	def get_alphabet(self, character):
		pass

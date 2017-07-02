def build_lexicon(mydoc):
	s = set()
	for doc in mydoc:
		s.update([word for word in doc.split()])
	return s


def term_freq(word, doc):
	return doc.split().count(word)


mydoc=['Julie loves me more than Linda loves me','Jane likes me more than Julie loves me','He likes basketball more than baseball']

print(build_lexicon(mydoc))

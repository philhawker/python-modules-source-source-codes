class Invoice(object):
	def __init__(self, client, total):
		self.client = client
		self.total = total

	def __str__(self):
		return f'Invoice from {self.client} for {self.total}'   #use __str__ to make the return data look pretty

	def __repr__(self):
		return f'invoice <value: {self.client}, total: {self.total}>'   # use __repr__ for pure data dump return

inv = Invoice('Google', 500)
print(str(inv))
print(repr(inv))

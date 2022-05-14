
class Component():
	def __init__(self):
		self.parent = None

	@property
	def Parent(self):
		return self.parent

	@Parent.setter
	def SetParent(self, new_parent):
		self.parent = new_parent

	def Update(self):
		pass

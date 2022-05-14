from EntityManager import EntityManager

class Entity(EntityManager):
	def __init__(self):
		super().__init__()
		self._name = None
		self.components = []
		self._parent = None

	def add_component(self, component):
		component.set_parent(self)
		self.components.append(component)

	@property
	def parent(self):
		return self._parent

	@parent.setter
	def parent(self, new_parent):
		self._parent = new_parent

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, new_name):
		self._name = new_name

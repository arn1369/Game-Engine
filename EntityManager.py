

class EntityManager():
	def __init__(self):
		self.entities = []
		self.label = {0 : "Entity_1",  # 'self.label' contains name & id of entity
					  1 : "Entity_2",
			   		  2 : "Entity_3",
					  3 : "Entity_4",
					  4 : "Entity_5"}
		self.label_keys = list(self.label.keys())
		self.label_vals = list(self.label.values())

	def get_ID_by_name(self, name: str) -> str:
		# return the key(id) of dict 'self.label' that has value(name) 'name'
		# {key : value}
		return self.label_keys[self.label_vals.index(name)]

	def get_name_by_ID(self, id: int) -> int:
		# if the id is not attributed
		if id not in self.label:
			# create a new name -> should I create a new entity ?
			return f"Empty_{id}"
		# return the name
		return self.label[id]

	def set_ID(self, new_id: int, name: str):
		# setting the key(id) in 'self.label' that has the name(value) 'name'
		self.label_keys[self.label_vals.index(name)] = new_id

	def set_name(self, id: int, new_name: str):
		# setting the value(name) in 'self.label' that has the key(id) 'id'
		self.label[id] = new_name

	def add(self, entity):
		if entity != None:
			# print the debug : name of entity and name of his class
			print(f"HaloInfo >>> Entity \'{entity.name}\' has been added to \'{type(self).__name__}\'.")
			# add the entity to his group
			self.entities.append(entity)

	def update(self):
		pass

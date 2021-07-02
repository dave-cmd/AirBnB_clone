import json 
import os


class FileStorage(object):
	"""docstring for FileStorage"""
	__file_path = "file.json"
	__objects = {}
	def __init__(self):
		super(FileStorage, self).__init__()

	def all(self):
		#return dictionary __objects
		return self.__objects

	def new(self, obj):
		# stores objects in __objects
		self.__objects[f"{obj.__class__.__name__}" + "." + str(obj.id)] = obj.__dict__

	def save(self):
		#serilize __objects to json file path
		with open(self.__file_path, "r+") as file:
			for item in self.__objects.items():
				str_ = "{ "
				str_ = str_+str(item[0]) + " : "
				str_ = str_+json.dumps(item[1])
				str_+" }\n"
				file.write(str_)
			file.close()
			
	def reload(self):
		# deserialize json file to __objects
		if self.__file_path:
			with open(self.__file_path, 'w+') as file:
				for item in file.read():
					#self.__objects[item[0]] = json.loads(item[1])
					obj = json.loads(item)
					self.__objects[item.keys()[0]] = item[item.keys()[0]]
				file.close()


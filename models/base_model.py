import uuid
import datetime

class BaseModel(object):
	"""docstring for BaseModel"""
	id = None
	created_at = None
	updated_at = None
	def __init__(self, *args, **kwargs):
		if len(kwargs) > 0:
			if "id" in kwargs:
				self.id = kwargs["id"]
			elif "my_number" in kwargs:
				self.my_number = kwargs["my_number"]
			elif "name" in kwargs:
				self.name = kwargs["name"]
			elif "created_at" in kwargs:
				self.created_at = kwargs["created_at"]
			elif "updated_at" in kwargs:
				self.updated_at = kwargs["updated_at"]
		else:
			self.my_number = ""
			self.name = ""
			self.id = uuid.uuid4()
			self.created_at = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')

	def to_dict_(self):
		return dict((key, value) for key, value in BaseModel.__dict__.items() if key[:2] != "__" )

	def to_dict(self):
		self.__dict__["__class__"] = self.__class__.__name__
		return self.__dict__

	def save(self):
		self.updated_at = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f') 
	def __str__(self):
		return f"[{self.__class__.__name__}] ({self.id}) {self.to_dict()}"







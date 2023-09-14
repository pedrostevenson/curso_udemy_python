class Conection():
	def __init__(self, host='localhost'):
		self.host = host
		self.user = None
		self.password = None

	def set_user(self, user):  # setter
		self.user = user

	def set_password(self, password):  # setter
		self.password = password

	@classmethod
	def create_with_auth(cls, user, password):
		connection = cls()
		connection.user = user
		connection.password = password
		return connection

# c1 = Conection()
c1 = Conection.create_with_auth('Pedro', '1234')
# c1.set_user('Pedro')
print(c1.user)
print(c1.password)
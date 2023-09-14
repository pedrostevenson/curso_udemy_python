class Caneta:
	def __init__(self, cor):
		self.cor_tinta = cor

	@property  # faz um método se comportar como um atributo
	def cor(self):
		return self.cor_tinta

#################################

# Código cliente
caneta = Caneta('Azul')
print(caneta.cor)  # Não precisa de parenteses 

#################################

# class Caneta:
# 	def __init__(self, cor):
# 		self.cor_tinta = cor
	
# 	def get_cor(self):
# 		return self.cor_tinta
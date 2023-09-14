# Atributos começados com underline 
# não devem ser usados fora da classe

class Caneta:
	def __init__(self, cor):
		self._cor = cor		
		# self.cor = cor  # Dessa forma, iria utilizar o setter já no init		
		self._cor_tampa = None	

	@property  # getter
	def cor(self):
		return self._cor
	
	@cor.setter
	def cor(self, nova_cor):
		self._cor = nova_cor

	@property
	def cor_tampa(self):
		return self._cor_tampa
	
	@cor_tampa.setter
	def cor_tampa(self, nova_cor):
		self._cor_tampa = nova_cor


caneta = Caneta('Azul')
caneta.cor = 'Vermelha'
caneta.cor_tampa = 'Azul'
print(caneta.cor)
print(caneta.cor_tampa)


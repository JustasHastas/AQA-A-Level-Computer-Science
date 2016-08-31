class Piece(object):
	def __init__(self, name, location_x, location_y):
		self.name = name
		self.location_x = location_x
		self.location_y = location_y
		
	def pasakyk_varda_ir_lokacija(self):
		print(self.name, self.location_x, self.location_y)

	def keiskis(self):
		self.location_x = self.name * 50

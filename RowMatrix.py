class RowMatrix:

	def __init__(self, rows, columns):
		self.rows = rows
		self.columns = columns
		self.matrix = []
		for i in range(rows):
			tmp = []
			for j in range(columns):
				tmp.append(0)
			self.matrix.append(tmp)

	def GetRows(self, rows):
		for i in range(self.rows):
			self.matix[i] = rows[i]

	def GetInPut(self):
		for i in range(self.rows):
			self.matrix[i] = list(map(int, input().split()))

	def  __repr__(self):
		result = ""
		for i in range(self.rows-1):
			result += str(self.matrix[i][0])
			for j in range(1,self.columns):
				result += " "+ str(self.matrix[i][j])
			result += "\n"
		for i in range(self.rows - 1,self.rows ):
			result += str(self.matrix[i][0])
			for j in range(1,self.columns):
				result += " "+ str(self.matrix[i][j])
			

		return(result)


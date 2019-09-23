class ColumnMatrix:


	def __init__(self, rows, columns):
		self.rows = rows
		self.columns = columns
		self.matrix = []
		for i in range(columns):
			tmp = []
			for j in range(rows):
				tmp.append(0)
			self.matrix.append(tmp)

	def GetColumns(self, columns):
		for i in range(len(columns)):
			self.matrix[i] = columns[i]

	def GetOneColumn(slef, column , place):
		place = place-1
		self.matrix[place] = column

	def GetInPut(self):
		ColumnsArray = []
		for i in range(self.columns):
			ColumnsArray.append([])
		for i in range(self.rows):
			lineArray = list(map(int, input().split()))
			for j in range(self.columns):
				ColumnsArray[j].append(lineArray[j])
		self.GetColumns(ColumnsArray)

	def __repr__(self):
		result = ""
		for i in range(self.rows-1):
			
			result += str(self.matrix[0][i])
			for j in range(1,self.columns):
				result += " " + str(self.matrix[j][i])  
			result += "\n"

		for i in range(self.rows - 1, self.rows ):
			
			result += str(self.matrix[0][i])
			for j in range(1,self.columns):
				result += " " + str(self.matrix[j][i])  
			

		return result

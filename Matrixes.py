#not throwing any Errors so it's risky to use 
#using  * and / is not clever cos there are not precise
#can take off deepcopy form Ees for memory performance 

from copy import deepcopy

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




def ConRow2Column(rmatrix):
	result = ColumnMatrix(rmatrix.rows, rmatrix.columns)
	for i in range(rmatrix.rows):
		for j in range(rmatrix.columns):
			result.matrix[j][i] = rmatrix.matrix[i][j]
	return result

def ConColumn2Row(cmatrix):
	result = RowMatrix(cmatrix.rows, cmatrix.columns)
	for i in range(cmatrix.rows):
		for j in range(cmatrix.columns):
			result.matrix[i][j] = cmatrix.matrix[j][i]
	return result

def plus2matrix(first, second):
	x = deepcopy(first)
	y = deepcopy(second)
	if isinstance(x, RowMatrix):
		x = ConRow2Column(x)
	if isinstance(y, RowMatrix):
		y = ConRow2Column(y)

	result = ColumnMatrix(x.rows, y.columns)

	for i in range(x.rows):
		for j in range(x.columns):
			result.matrix[j][i] = x.matrix[j][i] + y.matrix[j][i]

	return result

def matrix2Cmulty(cmatrix, c):
	x = deepcopy(cmatrix)

	if isinstance(x, RowMatrix):
		x = ConRow2Column(x)

	result = ColumnMatrix(x.rows, x.columns)
	for i in range(x.rows):
		for j in range(x.columns):
			result.matrix[j][i] = x.matrix[j][i] * c

	return result

def arr2cmul(arr , c):
	result = []
	for i in range(len(arr)):
		result.append(c*arr[i])
	return result

def arr2plus(first, second):
	result = []
	for i in range(len(first)):
		result.append(first[i] + second[i])

	return	result

def multiplication(first, second):
	x = deepcopy(first)
	y = deepcopy(second)
	if isinstance(x, RowMatrix):
		x = ConRow2Column(x)
	if isinstance(y, RowMatrix):
		y = ConRow2Column(y)

	#Once more errors are not cheking in code
	result = ColumnMatrix(x.rows, y.columns)
	for i in range(y.columns):

		tmp = arr2cmul(x.matrix[0], y.matrix[i][0])
		for j in range(1, y.rows):
			tmp = arr2plus(tmp , arr2cmul(x.matrix[j], y.matrix[i][j]))

		result.matrix[i] = tmp

	return result

def transpose(x):
	tmp = []
	if isinstance(x, RowMatrix):
		tmp = ColumnMatrix(x.columns, x.rows)
		for i in range(x.rows):
			tmp.matrix[i] = x.matrix[i]
	if isinstance(x, ColumnMatrix):
		tmp = RowMatrix(x.columns, x.rows)
		for i in range(x.columns):
			tmp.matrix[i] = x.matrix[i]
	if isinstance(tmp, RowMatrix):
		tmp = ConRow2Column(tmp)
	return tmp



class Ees:

	def __init__(self, kind):
		self.kind = kind 

class ChangeRow(Ees):

	def __init__(self, kind, first , second):
		Ees.__init__(self, kind)
		self.first = first -1
		self.second = second -1
		self.kind = "C"


	def action(self, x):
		tmp = deepcopy(x)
		if isinstance(x, ColumnMatrix):
			tmp = ConColumn2Row(tmp)

		change1 = tmp.matrix[self.first]
		change2 = tmp.matrix[self.second]

		tmp.matrix[self.second] = change1
		tmp.matrix[self.first] = change2

		return tmp

	def __repr__(self):
		result = self.kind + str(self.first+1) + "," + str(self.second+1)
		return result

class MultyRow(Ees):

	def __init__(self, kind , row , c ):
		Ees.__init__(self, kind)
		self.row = row -1 
		self.c = c

	def action(self, x):
		tmp = deepcopy(x)
		if isinstance(x, ColumnMatrix):
			tmp = ConColumn2Row(tmp)

		tmp.matrix[self.row] = arr2cmul(x.matrix[self.row] , self.c)
		return tmp

	def __repr__(self):
		result = self.kind + str(self.row+1) + "*" + str(self.c)
		return result


class PlusRow(Ees):

	def __init__(self,kind, row1 , row2 , row2c):
		Ees.__init__(self,kind)	
		self.row1 = row1 -1 
		self.row2 = row2 -1 
		self.row2c = row2c
		self.kind = "P"

	def action(self ,x):
		tmp = deepcopy(x) 
		if isinstance(x, ColumnMatrix):
			tmp = ConColumn2Row(tmp)


		addrow = arr2cmul(x.matrix[self.row2], self.row2c)
		tmp.matrix[self.row1] = arr2plus(x.matrix[self.row1], addrow)

		return tmp

	def __repr__(self):
		result = self.kind + str(self.row1+1) + "," + str(self.row2+1) + "*" + str(self.row2c)
		return result

class rref:

	def __init__(self,matrix):

		tmp = deepcopy(matrix)
		if isinstance(tmp, ColumnMatrix):
			tmp = ConColumn2Row(tmp)
		self.matrix = tmp
		self.rref = deepcopy(tmp)
		self.seq = []
	


	def procces(self):
		currentrow = 0
		for i in range(self.rref.columns):
			if currentrow == self.rref.rows :
				break
			for j in range(currentrow,self.rref.rows):

				if self.rref.matrix[j][i] != 0 :
					if j <= currentrow :
						for k in range(j):
							if self.rref.matrix[k][i] != 0 :
								t = (self.rref.matrix[k][i] / self.rref.matrix[j][i])* - 1 
								if t != 0 :
									tt = PlusRow("P",k+1,j+1,t)
									self.seq.append(tt)
									self.rref = tt.action(self.rref)
						for k in range(j+1,self.rref.rows):
							if self.rref.matrix[k][i] != 0 :
								t = (self.rref.matrix[k][i] / self.rref.matrix[j][i])* - 1 
								if t != 0 :
									tt = PlusRow("P",k+1,j+1,t)
									self.rref = tt.action(self.rref)
									self.seq.append(tt)
						if 1/self.rref.matrix[j][i] != 1 :
							uu = MultyRow("M",currentrow+1, 1/self.rref.matrix[j][i])
							self.seq.append(uu)
							self.rref = uu.action(self.rref)
						currentrow += 1
					else :
						c = ChangeRow("c",j+1, currentrow+1)
						self.seq.append(c)
						self.rref = c.action(self.rref)
						for k in range(currentrow):
							if self.rref.matrix[k][i] != 0 :
								t = (self.rref.matrix[k][i] / self.rref.matrix[currentrow][i])* - 1 
								if t != 0 :
									tt = PlusRow("P",k+1,currentrow+1,t)
									self.seq.append(tt)
									self.rref = tt.action(self.rref)
						for k in range(currentrow+1,self.rref.rows):
							if self.rref.matrix[k][i] != 0 :
								t = (self.rref.matrix[k][i] / self.rref.matrix[currentrow][i])* - 1 
								if t != 0 :
									tt = PlusRow("P",k+1,currentrow+1,t)
									self.seq.append(tt)
									self.rref = tt.action(self.rref)
						if 1/self.rref.matrix[currentrow][i] != 1:
							uu = MultyRow("M",currentrow+1, 1/self.rref.matrix[currentrow][i])
							self.seq.append(uu)
							self.rref = uu.action(self.rref)
						currentrow += 1
		
		return self.rref




class elimination:

	def __init__(self, matrix):
		tmp = deepcopy(matrix)
		if isinstance(tmp, ColumnMatrix):
			tmp = ConColumn2Row(tmp)
		self.matrix = tmp
		self.eliminate = deepcopy(tmp)
		self.seq = []
		self.can = True	
		self.done = False

	def procces(self):
		times = min(self.eliminate.rows, self.eliminate.columns)

		for t in range(times):
			if self.eliminate.matrix[t][t] == 0 :
				chk = True
				for k in range(t+1, self.eliminate.rows):
					if self.eliminate.matrix[k][t] != 0 :
						chk = False
						tes = ChangeRow("C",t+1,k+1)
						self.seq.append(tes)
						self.eliminate = tes.action(self.eliminate)
				if chk :
					self.can = False
					break
				# adding else
				for k in range(t+1, self.eliminate.rows):
					if self.eliminate.matrix[k][t] != 0 :
						cel = (self.eliminate.matrix[k][t] / self.eliminate.matrix[t][t]) * -1
						if cel != 0 :
							el = PlusRow("P",k+1,t+1, cel)
							self.seq.append(el)
							self.eliminate = el.action(self.eliminate)
			else:
				for k in range(t+1, self.eliminate.rows):
					if self.eliminate.matrix[k][t] != 0 :
						cel = (self.eliminate.matrix[k][t] / self.eliminate.matrix[t][t]) * -1
						if cel != 0 :
							el = PlusRow("P",k+1,t+1, cel)
							self.seq.append(el)
							self.eliminate = el.action(self.eliminate)

		if self.can :
			return(self.eliminate)
		print(":(")
		return ":("


def solveaxeqb(a,b):

	tmpa = deepcopy(a)
	tmpb = deepcopy(b)
	if isinstance(tmpa , ColumnMatrix):
		tmpa = ConColumn2Row(tmpa)
	if isinstance(tmpb , ColumnMatrix):
		tmpa = ConColumn2Row(tmpb)
			
	eact = elimination(tmpa)
	eact.procces()

	if eact.can == False :
		return "Can't be done"

	refa = rref(tmpa)
	refa.procces()

	print(refa.seq)
	print(refa.rref)
	print("--------------------")

	#Actions
	for i in range(len(refa.seq)):
		tmpb = refa.seq[i].action(tmpb)

	for i in range(a.columns,tmpb.rows):
		if tmpb.matrix[i][0] != 0:
			#print ("Can't be done2")
			return "Can't be done2"

	print(tmpb)

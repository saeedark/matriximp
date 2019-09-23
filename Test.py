from Matrixes import *

#x = ColumnMatrix(3,5)
#x.GetInPut()
#print(x.matrix)
#print(x)
#y = ConColumn2Row(x)
#y = RowMatrix(3,5)
#y.GetInPut()
#print(y.matrix)
#print(type(y))

#print (matrix2Cmulty(y, -2))
#print(plus2matrix(y,matrix2Cmulty(y, -2)))
#x = ConRow2Column(y)
#print(x)
#print(x)
#print(x.matrix)

#first = ColumnMatrix(3,2)
#first.GetInPut()

#x = ColumnMatrix(3,4)
#x.GetInPut()
#print(x)

#ghg = rref(x)
#print(ghg.procces())
#second = RowMatrix(2,2)
#second.GetInPut()

#print(transpose(first))

#multiplication(y, x)

#print(y)

#x = ChangeRow("c",1,3)
#print(x.action(y))

#print("______________________")
#print(y)
#print("______________________")
#z = MultyRow("M", 2, 10)
#print(z.action(y))
#print("______________________")
#print(y)
#print("______________________")

#t = PlusRow("P" ,3,2,-2)
#print(t.action(y))
#print("______________________")
#print(y)
#print("______________________")

#x = ColumnMatrix(3,6)
#x.GetInPut()
#print(x)

#ghg = rref(x)
#print(ghg.procces())
#print(ghg.rref)
#print(ghg.seq)

#eli = ColumnMatrix(3,3)
#eli.GetInPut()
#print(eli)

#eilm = elimination(eli)
#print(eilm.procces())

#the input
#1 1
#2 -1
#3 0
#6 
#3
#9
#
a = RowMatrix(3,2)
#x = RowMatrix(2,1)
b = RowMatrix(3,1)
a.GetInPut()
#x.GetInPut()
b.GetInPut()

#print(multiplication(a,x))
print("__________________")

#eliminate = elimination(a)
#eliminate.procces()
#print(eliminate.seq)
#for i in range(len(eliminate.seq)):
#	b = eliminate.seq[i].action(b)
#	print(b)

#print("__________________")
#rf=  rref(a)
#rf.procces()
#print(rf.seq)
#print(rf.rref)
#print("__________________")
#for i in range(len(rf.seq)):
#	b = rf.seq[i].action(b)
#	print(b)
#print("__________________")
#print(b)

solveaxeqb(a,b)

#ภายใน array ต้องมีข้อมูลชนิดเดียวกัน เเละมีขนาดที่เเน่นอน จึงต่างกับList
#สามารถสังเกตมิติได้จากการซ้อนกันของ [] เช่น [[]] = 2, [[[]]] = 3
import numpy as np
arr = np.array(3) # array 0 dimen
print(arr)
print(arr.ndim, "dimen") #check dimension in arr

array1di = np.array([1,2,3,4]) #array 1 dimension
print(array1di)
print(array1di.ndim, "dimen")

#tu = (1,2,3,4)
#arraybyTuple = np.array(tu) เเบบนี้ก็ได้นะ เอาตัวเเปรไปใส่ใน () เเล้วไม่ต้องใส่ []

#2 dimen
array2di = np.array([[1,2,3],[4,5,6],[7,8,9]]) #ควรเข้าใจว่า ตัวเลขใน[[]] คือcolumn ส่วนจำนวน [] คือ row  
print(array2di)
print(array2di.ndim, "dimen")

#3 dimen
array3di = np.array([[[1,2,3],[4,5,6]]]) #(1 depth)
print(array3di)
print(array3di.ndim, "dimen")
array3di = np.array([[[1,2,3],[4,5,6]],
                     [[7,8,9],[10,11,12]]]) #2 depth (การจะสร้าง depth row,column ต้องเท่ากัน ในกรณีนี้ มี 2 row 3 column ทั้งคู่)


#การเข้าถึง array 1 dimen
array1di = np.array([1,2,3,4,5]) #array 1 dimension
print(array1di[0], "is index 0(1di,index)") #ก็ใช้ index ธรรมดานั่นเเหละ 

#การเข้าถึง array 2 dimen
array2di = np.array([[1,2,3],[4,5,6],[7,8,9]]) 
print(array2di[1][2], "is row1 column2(2di,index)") #ก็เข้าถึงตัว row ก่อน เเล้วค่อย column

#การเข้าถึง array 3 dimen
array3di = np.array([[[1,2,3],[4,5,6]],
                     [[7,8,9],[10,11,12]]])
print(array3di[1][1][2], "is depth1 row1 column2 (3di,index)") #เข้าถึง depth ก่อน เเล้ว row column

#check dataType in array
print(arr.dtype)

arr = np.array([1.6, 2.1, 3.99], dtype="int")
print(arr) #1,2,3 เพราะกำหนดเป็น int เลยตัดพวก. ออกหมด โดยไม่ปัดใดๆ

#zero matrix 1d
zeroMatrix1d = np.zeros(5)
print(zeroMatrix1d)

#zero matr 2d
zeroMatrix2d = np.zeros([2,2]) #ขนาด 2*2
print(zeroMatrix2d)
#zero 3d  ก็ทำเหมือนเดิมอะ เเค่เพื่มเป็น depth, row,* colum. ex :  ([2,3,4]) 2ชั้น 3เเถว 4ช่อง

#ones matr
oneMatrix1d = np.ones(5) #2d 3d ก็ทำเหมือนเดิม
print(oneMatrix1d)

#matrix ค่าคงที่
FullMatr = np.full([3,2], 5) #ตัวเเรกคือจำนวนสมาชิก ตัวที2คือเลขที่จะให้สมาชิกเป็น
print(FullMatr) #เลข5, 2ตัว 3บรรทัด
#3d ก็เหมือนเดิมอะ ใส่เพิ่มใน ()

#empty เป็นการสร้าง array ว่างเปล่าขึ้นมา กำหนดกรอบได้ เเต่สมาชิกจะ random
empty = np.empty([3,4])
print(empty)

#identity คือ matrix ที่มีเลข1 เป็นเส้นทเเยงมุม ที่เหลือเป็น0  
iden = np.identity(4) #กำหนดเลขตัวเดียว เพื่อทำกรอบเเบบ n*n เช่น 4 = 4*4
print(iden)

eye = np.eye(3,4) #เหมือนกับ iden but สามารถกำหนด row column เเยกกันได้ เช่น 3 row 4 column
print(eye)

#เปลี่ยนตำเเหน่งเส้นทเเยงมุม
eyeChangeK = np.eye(3,4, k=1) #เปลี่ยนตำเเหน่งเส้นทเเยงมุม โดยเริ่มต้น k=0 ขยับขวา +1 ซ้าย -1
print(eyeChangeK)

#Linspace (start, stop, output)
Lin = np.linspace(1,5,3) #มันจะเเสดงผลในขอบเขตของ เลขตัวที่1 ถึง เลขตัวที่2 ส่วนตัวที่3คือจำนวนตำเลขที่จะ output
print(Lin) #output = 1,3,5 จะเห็นว่ามันอยู่ใขอบเขต ของ1-5 เเละออกมาเเค่3ตัว

Linend = np.linspace(1,5,5, endpoint=False) #เหมือนเดิม เเต่เเค่ไม่เอาเลข5 เอาเเค่ถึง4.99999....

#Arange
Arange = np.arange(1,10) #output เลข 1-9 (เหมือนการทำงนของ for loop) เเเนะนำให้ใช้เเทนการเขียนarray 1 มิติที่เรียงลำดับชัดเจน เพราะประหยัดเวลากว่า
print(Arange)
Arange = np.arange(1,10,2) #อันนี้ก็ให้เพิ่มทีละ2 outputก็  1 3 5 7 

#random 
ran = np.random.random([2,2]) #สุ่มค่าเลขตั้งเเต่ 0-1 ใน array  2*2
print(ran)

#check row, column
a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(a.shape) #(4, 3) show row and column เเต่ถ้าเป้นarray 1มิติ จะบอกเเค่ column

#check จำนวนสมาชิก
print(a.size) #3row 4column = 3*4 = มีข้อมูล 12 ตัว

#bit
# dataType ของ a คือ int32 itemsize คิดจากตัวเลขด้านหลังtype / 8 เช่น (int) 32 / 8 = 4
print(a.itemsize, "bites")

#slice array 2d
array2di = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array2di[:2,:1]) #เอาหลักการ slice มาใช้ เเต่อันนี้เป็น row, column เช่นอันนี้ เเสดงเเค่ row start:2, column start:1

#เข้าถึง index array โดยใช้ List
array1 = np.arange(1,10)
List = [1,2,3] 
print(array1[List]) #output = 2,3,4 cuz index1 = 2 .. blah blah

#เข้าถึง row โดยใช้ [[]] ไม่ก็ [List]
b = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b[[0,2]]) #ในกรณีที่มี [[]] มันจะเข้าถึงเเถวเลย ก็คือ0,2 = เเถว1 กับเเถว3
#อันนี้เข้าถึง column ด้วย
print(b[[0,2],[0,1]]) #output = 1,8 เพราะ row0 col0 =1 , row2 col1 = 8

#การเข้าถึง array ด้วย เงือนไข
idk = np.array([[1,2,3],[-4,-5,-6]])
print(idk[idk<0]) #output = -4 -5 -6

#about math
math = np.arange(1,4) #1,2,3 (ใข้ได้ทุกเครื่องหมาย)
print(math+2) #output= 3,4,5
#array and array
math2 = np.arange(10,13) #ก็คือเอาindex ที่ตรงกันไปตำนวณกันนั่นเเหละ
print(math+math2) #output = 11,13,15 เงื่อนไขคือColumnต้องเท่ากัน หรือตัวที่เอามาบวกต้องมีจำนวน = 1 (1+10, 2+11, 3+12)

#change 1d to 2d
change1d = np.arange(10)
print(change1d.reshape([2,5])) #เงื่อนไขคือการ reshape ต้องมีสมาชิกเหมือนเดิม ดังนั้นช่อง ([x,y]) x*y ต้องได้ = change1d(a)

change1d.resize([2,5]) #เหมือน reshape เเต่เเค่มันเปลี่ยนถาวร ไม่ต้องสร้างตัวเเปรมารับ
print(change1d)

#change dimensions to 1d
print(change1d.flatten())
change1d2 = change1d.ravel() #อันนี้เหมือนเดิม เเเต่เเค่เวลาข้อมูลในตัวเเปรเปลี่ยนเเปลง(change1d2) change1d ก็จะเปลี่ยนตาม

#swap row and column
a = np.array([[1,2,3],[4,5,6]])
print(a.transpose()) #from 2row 3column to 3row 2 column 

#sumation
#(+)
print(a.sum()) #21
#(*) 
print(a.prod()) # 720
#ค่าเฉลี่ย
print(a.mean()) #3.5
#มากสุด
print(a.max()) #6
#น้อยสุด
print(a.min()) #1
#index ที่มี value มากสุด
print(a.argmax()) #6 เพราะ index5 เพราะindex5 เก็บเลข6ไว้ ซึ่ง6มีค่ามากสุด จึงoutput 5 ที่เป็น index ออกมา 
#index value น้อยสุด
print(a.argmin()) #0 cuz index 0 = 1 and 1 is lowest
#ค่าต่ำสุดเเบบ เเนวตั้ง-เเนวนอน เเนวตั้ง=row=axis0, เเนวนอน=column=axis1
print(np.max(a, axis=1)) #answer : 3,6
print(np.min(a, axis=0)) #answer : 1,2,3

#dot product (เอาสมาชิกมาคุณกัน (มีสูตร)) เงื่อนไขคือสมาชิกต้องเท่ากัน (row*column)
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]]) 
c = a.dot(b) #วิธีทำ (1*5+2*7, 1*6+2*8, 3*5+4*7, 3*6+4*8)
print(1*5+2*7, 1*6+2*8, 3*5+4*7, 3*6+4*8)
print(c)

#เอา array มาต่อกัน เหมือนappend เเต่เอาไปทั้ง array
print(np.concatenate([a,b]))
#append ต่อท้ายทีละตัว
print(np.append(a, 9)) #เอา9 ไปต่อท้าย
print(np.append(a, [[10],[11]], axis=1)) #10,11 ต่อท้าย but เเนวนอน
#เพิ่มเหมือนกัน เเต่อันนี้จะต่อตัวที่ต้องการ เเบบเเทรก ไม่ใช่replace ไม่ใช่ต่อท้าย โดยจะเข้ามาเเทรกด้านหน้าของ index ที่เลือก
print(np.insert(a,0,100)) #(variableที่ต้องการ, index, ตัวที่จะใส่) before : 1,2,3 after : 100,1,2,3 
#อันนี้เเบบหลายตัวพร้อมกัน just a trick
print(np.insert(a, (0,3), 100)) #เอา100 ไปเเทรกหน้า index 0,3
#insert in 2d
insert2d = np.array([[1,2,3], [4,5,6]])
print(np.insert(insert2d,(0,1),((100,200)),axis=1)) #ก๋ทำเหมือนเดิมเเต่เอา axis 
print(np.insert(insert2d,(0),(100,200),axis=1)) #ก๋ทำเหมือนเดิมเเต่เอา axis มาประยุก
print(np.insert(insert2d,(0,1),(100),axis=0)) #ก๋ทำเหมือนเดิมเเต่เอา axis มาประยุก
#(ไม่รู้ทำไม เเต่ axis0 ,มันใส่ตัวเเทรก2ตัวไม่ได้)

#delete member
delArray = np.arange(1,11)
print(np.delete(delArray, 0)) #del index0@
#delete member from 2d
delArray = np.arange(1,11).reshape(2,5)
print(np.delete(delArray, 1, axis=1)) #ลบทั้งเเถว

#เเบ่ง member ใน array หรือก็คือเอามาหารให้เท่าๆ
GroupAr = np.arange(1,21)
print(np.split(GroupAr,2)) #ก็คือบอกว่าจะเเบ่งเป็นกี่กลุ่ม อันนี้มีสมาชิก20 เเบ่ง4 ก็กลุ่มละ5 เงื่อนไขคือต้องหารลงตัวให้ได้เท่าๆ

#เเบ่ง member 2d
GroupAr2d = np.arange(1,21)
GroupAr2d = GroupAr2d.reshape(5,4)
print(np.vsplit(GroupAr2d, 5)) #เเนวนอน row
print(np.hsplit(GroupAr2d, 2)) #เเนวตั้ง col

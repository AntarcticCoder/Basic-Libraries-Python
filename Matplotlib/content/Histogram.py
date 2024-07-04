import matplotlib.pyplot as plt
#Histogram 
#for เเสดงความถี่ ข้อมูลไม่ต่อเนื่อง

age = [18,16,12,16,16,17,19,20,16,17,19,19,12]
plt.hist(age)
plt.xlabel("age")
plt.ylabel("total")
plt.show()
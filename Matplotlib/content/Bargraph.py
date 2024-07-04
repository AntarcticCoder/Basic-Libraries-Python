import matplotlib.pyplot as plt
#กราฟเเท่ง
#ข้อมูลเเกนx,y ต้องเป็นเเบบชุด เช่น list numpy series dataframe เเละ x,y ต้องมีจำนวนเท่ากัน
x = [1,2,3,4,5]
y = [10, 20, 30, 40, 50]
plt.bar(x, y, color=['g', 'r', "orange", "purple", 'c'], width=0.5, edgecolor="black", linewidth=2) #set info and color
plt.show()
#plt.barh ก็คือกราฟเเท่งเเนวนอน ซึ่งห้ามใส่ width

#default width = 0.8
#edge color = สีขอบ 
#linewidth = ความหนาขอบ
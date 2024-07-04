import matplotlib.pyplot as plt
#เป็นกราฟเเบบใช้จุดล้วนๆ
x = [1, 2, 3, 4, 5]
y = [1, 2, 4.5, 5.6, 7]
sizes = [10, 20, 12, 15, 10] #ขนาดของเเต่ละจุด default ไม่เเน่ใจ เเต่ไม่ต้องใส่ก็ได้
color = ["green", "pink", "cyan", "red", "orange"] #ตั้งสีให้เเต่ละจุด

plt.scatter(x, y, c=color) 
plt.show()
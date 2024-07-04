import matplotlib.pyplot as plt

#กราฟเส้น
product1 = [10,20,30,40,50]
product12 = [15,30,10,4,20]
mouth = ["jan", "feb", 'march', 'april', 'may']

# 2 เส้น
plt.plot(mouth, product1, linestyle= '--') # line style(เส้นปะ)
plt.plot(mouth, product12, marker='.') # ทำจุดพลอตตำเเหน่งที่ตรงกับข้อมูลที่กำหนด
#plt.plot(mouth, product12,"r.--") (red, . , --) อันนี้เขียนย่อ

plt.xlabel("mouth", size=20, color="w", backgroundcolor='r') #header x 
plt.ylabel("Sales", size=20) #header y

#title ชื่อกราฟ
plt.title("Graph name", loc="left", size=20)

#การเขียนข้อวามเเบบกำหนด เเกนx,y เอง กรณีนี้ใช้ "may" เพราะset เเกน x ไว้เป็นชืื่อเดือนเลยทำได้ เเต่จะกำหนดเป็นเลขก็ทำได้เช่นกัน ตาม normal index
plt.text("may", 40, "this is in may")
plt.text(3, 30, "normal index case")
plt.text(-0.2, 8, "first right?", fontsize=10)

plt.savefig("testsave.png") #save ถ้าอยากได้เเบบไม่มีbackground ก็ใช้ transparent=True เผื่อเอาเข้า photoshop ไรงี้

plt.show()

import matplotlib.pyplot as plt
#bar ซ้อนกัน
room = ['A', 'B', 'C']
boys = [10, 15, 5]
girls = [20, 7, 15]

plt.bar(room, boys, color="blue")
plt.bar(room,girls, bottom=boys, color="pink")
plt.legend(["boy", "girl"])
plt.show() #มันคือการบอกให้ boy ไปอยู่ด้านล่าง girls
#เอาจริงๆมันดูไม่ต่อยชัด เพราะถ้าจะเอาจำนวน bar ด้านบน มันก็ต้องเอามาลบออกด้วยจำนวน bar ด้านล่างก่อน
#เเนะนำให้ใช้ตอนจะดูเเบบรวมๆ เช่น ห้องนี้มี"ทั้งหมด"กี่คน ไม่ก็ไปใช่graph อื่นเหอะ
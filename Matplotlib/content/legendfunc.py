import matplotlib.pyplot as plt
import numpy as np
t = np.arange(1,5)
plt.plot(t**2,t, color='r', marker='.', linestyle="--")
plt.plot(t**3,t, color='g', marker='.')
plt.legend(["Mouse", "Keyboard"], loc="best", fontsize=10, edgecolor='b', facecolor='w', title="explain", labelspacing=1, borderpad=1.4) #มันคือทำกรอบมาอธิบายว่าเส้นเเต่ละสี คืออะไร เช่นอันนี้มันจะบอกว่า เส้นเเดงคือ Mouse เส้นเขียวคือ Keyboard
plt.show()#you can set loc behind data in legend too
#edge = สีขอบ legend
# facecolor = สีbackground legend
#title in legend = หัวข้อด้านบนคำอธิบาย เเต่ไม่สำคัญเท่าไหร่หรอก ตัวอย่างเช่น title = "คำอธิบายสัญญลักษณ์"
#labelspacing = ระยะห่างข้อความ
#borderpad = boder size
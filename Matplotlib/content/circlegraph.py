import matplotlib.pyplot as plt
#ใช้สำหรับshow data ที่รวมกันได้ 100%
data = [15,34,40,23,25] #อันนี้ข้อมูลนะ ไม่ใช่ %  โปรเเกรมมันจะเอาไปคิด percent เอง
lang = ["c#", "py", "javascript", "golang", "c++"] #มันจะจับคู่กับด้านบน 

plt.pie(data, labels=lang, colors=["red", "orange", "pink", "cyan", "green"], autopct="%.1f%%", explode=[0.8, 0, 0, 0.1,0]) 
#autopct คือการเเสดง % 
#explode คือระยะห่างระหว่างเเต่ละส่วน ถ้ากำหนดไว้1 มันจะเหมือนมันการหยิบออกมา
#shadow=True ใส่เงา
#startangle=x พลิกองศาวงกลม

plt.title("programming lang most people use")
plt.show()


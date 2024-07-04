import pandas as pd
import numpy as np
#series คือ array 1d ที่เก็บข้อมูลต่างชนิดกันได้
#dataFrame คือ array 2d  หรือ series หลายอันเรียงกัน
#Panel คือ array 3d , dataframe มาซ้อนกัน 

dataArray = np.array(["test", 1, True, 1.4])
dataList = ["test", 1, True, 1.4]
dataTuple = ("test", 1, True, 1.4)
print(dataArray)

# create Series
series = pd.Series(dataArray) #or dataTuple or dataList 
print(series)

# set Index for Series (หัวข้อด้านหน้า)
idx = [10,20,30,40]
series = pd.Series(dataArray, index=idx)
print(series)

#set index by key in dic
color = {"red": "เเดง", "green": "เขียว"}
print(pd.Series(color["red"])) 

#ต่อ jupyter
#(เสริม) ในjupyter เราไม่ต้องใส่ print เเล้วมันจะทำเป็นตารางให้เเบบสวยๆ เเต่ถ้าใส่ print มันจะทำออกมาทุเรศเเบบข้อความไม่ตรง ซึ่งนี่คือข้อดีของ jupyter เเต่ vs code ต้อง print
#google colab ก็มีความสามารถเเบบ jupyter


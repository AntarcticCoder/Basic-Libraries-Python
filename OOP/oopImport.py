from oop import Name #import class เเม่มาทำงาน จะได้จัดการcodeได้ง่าย
class nameButCopy(Name): #การสีบทอดคุณสมบัติจาก class อื่น ซึ่งทำให้สามารถเข้าถึงข้อมูลทั้งหมดใน class อื่น ยกเว้น private (ถ้าไม่ทำ init(constructor) ให้class ลูก มันจะดึงของเเม่มาทำงาน)
    __nameInCopy = "iJust whoLOl"  #กำหนดเอง จะได้ไม่ต้องรับเข้ามา
    def __init__(self, Meterage, cardID, status): #เพิ่ม parameter ที่class เเม่ไม่มีได้ เช่น status
        super().__init__(self.__nameInCopy, Meterage, cardID) #ส่งไปให้ class เเม่ (init ด้านหน้าที่.ไว้ มันคือตัวที่อยู่ใน classเเม่นะ)
        self.stat = status

    def _showData(self): #เอา method จากclassเเม่ มาเขียนใหม่ใน class ลูก return ข้อมูลจาก showData classเเม่ เเล้วเพิ่มข้อมูลที่ต้องการ
        return super()._showData() + f"\nstatus : {self.stat}"
     
print(nameButCopy.noname) #i can call .noname by class nameButCopy
print(nameButCopy._Name__private) #เข้าถึง private ได้ เนื่องจากมีการเข้าถึง class เเม่ก่อน

classNameCopy = nameButCopy(8, 1111, "married") #ใน objects ใส่ status ด้วย
#classNameCopy._showData() จะใช้เเบบนี้ หรือไปเขียนsuper ก็ได้ ถ้าจะเรียก method จากclassเเม่ เรียกใช้ showdata จาก class เเม่ โดยใส่เเค่ age, Id, status เพราะใน classลูกกำหนด name ไว้เเล้ว เเละส่งไปให้class เเม่ด้วย super

print(classNameCopy._showData())

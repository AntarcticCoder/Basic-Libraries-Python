#create class
class Name:
    #class variable หรือในภาษาปกติเรียก global variable ซึ่งไม่จำเป็นต้องสร้าง objects วิธีสังเกตคือ class variable จะอยู่ในพื้นที่ class โดยตรง ไม่ได้อยู่ใน method
    noname = "noname but public kub p"
    __private = "gu private kub" #ถ้าเป็น private มันจะเข้าถึงไม่ได้ถ้าไม่เข้าถึง class เเม่ก่อน เช่น classลูก._classเเม่__private

    def __init__(self, Metername, Meterage, cardID): #constructor(method ประเภทหนึ่งนั่นเเหละ) (ไม่จำเป้น จะสร้างmethod ธรรมดาก็ได้ เเต่อันนี้มันเรียกใช้auto ตามจำนวน objects ที่สร้าง)
        #ทั้ง 3 อันนี้ คือ instance variable ก็คือจำเป็นต้องสร้าง objects ก่อน ถึงจะใช้ได้ วิธีสังเกตคือ instance variable จะอยู่ใน method ใน class อีกที
        #public attribute ไม่มี_ เเก้ไขข้อมูลได้
        self.name = Metername #attribute ไอ้ตัวหน้า เเค่ตั้งชื่อเฉยๆ เอาไว้ใส่ใน {} .format
        #protected attribute (_) จะทำให้เรียกใช้งานหรือเเก้ไขได้เเค่ class ของตัวมันเอง เเละ classลูก สืบทอด หรือพวก objectอะ เเก้ได้
        self._age = Meterage 
        #Private (__) มีเเต่ class method ของตัวมันเองที่เรียกใช้งานได้ เเก้ไขไม่ได้ เเม้จะเข้าถึงผ่าน objectsก็ตาม
        self.__card = cardID

    #create method (protected med)
    def _showData(self): #med in Name class (ไม่ต้องใส่ Parameters เพื่ม เพราะอยู่ในclass เดียวกัน)
        return f"name : {self.name} \nage : {self._age} \nIDcard : {self.__card}"


    #method setter คือการเปลี่ยนค่า private ด้วย method
    def setIDCARD(self, newID):
        self.__card = newID

    #method getter คือการเรียกใช้งาน private เพราะปกติ private ไม่สามารถถูกเรียกได้จาก objects หรืออะไรก็ตามนอกจากตัวมันเองใน class จึงต้องทำ getter method ขึ้นมา return private ออกไป
    def getIDCARD(self):
        return self.__card


    def __del__(self): #เรียกใช้ตามจำนวน objects จะเเสดงเมื่อทำงานจบเเล้ว (ไม่จำเป็น)
        #print("end")
        pass

print(Name.noname) #เรียกใช้ class variable เเค่เข้าถึง class กับ variable เท่านั้น

#create objects
nameID1 = Name("who's kongpop", 1, 11)
nameID2 = Name("iJust likeCats", 13, 69)

print(isinstance(nameID1, Name)) #จะเช็คว่า objects nameID1 เป็นส่วนหนึ่่งของ class Name หรือไม่ (คำตอบตือ True ในกรณีนี้)
#print(dir(nameID1)) show ข้อมูลทั้งหมด
print(nameID1.__class__) #บอกว่าอยู่ใน class ไหน

nameID2.__card = 20 #เปลี่ยนไม่ได้ เพราะIDcard เป็น private นอกจากจะใช้ Method Setter อันนี้ที่เห็นไม่ error เพราะมันคิดว่าเรากำหนดตัวเเปรเฉยๆ
print(nameID2._showData())

#เรียกใช้ method setter ทำให้สามารถเปลี่ยนค่าใน private ได้
nameID2.setIDCARD(19)
print(nameID2._showData())

#เรียกใช้งาน method getter เพื่อดูข้อมูลที่เป้น private 
print(f"likecat's id : {nameID2.getIDCARD()}")

#ความต่างของ instance variable กับ class variable
print(nameID2.name) #instance เรียกใช้โดย objects (จำเป็นต้องสร้าง objects)
print(Name.noname) #class เรียกใช้โดย class 
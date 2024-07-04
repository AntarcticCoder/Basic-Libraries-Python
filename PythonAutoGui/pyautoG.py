import pyautogui as pg
CurrentPosition = pg.position() #looking for current mouse cursor position
for i in range(20):
    #pg.click(CurrentPosition) #click
    pass

#transform class to point
list = [1, 2]
point = pg.Point(list[0], list[1])
print(point)

greeting = "HELLO"

#move your mouse
#pg.moveTo(point, duration=2) #duration จะทำให่ cursor เลื่อนช้าลง ให้ไปถึงจุดหมายตามระยะเวลาที่กำหนด

def chatToGay(): #test chat
    pg.moveTo(x=403, y=12)
    pg.click()
    pg.moveTo(x=1390, y=977)
    pg.click
    for i in greeting:
        pg.press(i)
    pg.press("ENTER")

#chatToGay()

#hot key
#pg.hotkey("ctrl", "c")

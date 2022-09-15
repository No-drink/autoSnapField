from datetime import datetime
from time import sleep
import pyautogui

vertical=73
horizontal=175
base_x=778
base_y=451
wanted=list(map(int,input('输入想要预定的时间段:').split()))
#默认为17，18点场
if(not list(wanted)):
    wanted=[17,18]   

print("等待规定时间中......")
while (datetime.now().minute!=0):
    pass
sleep(0.1)
print("开始抢场......")

#点击后一天 
pyautogui.click(1191,104)   

#验证是否加载完成
while(not pyautogui.pixelMatchesColor(995,521, (255, 255, 255))):
    pass

#点击下拉菜单   
pyautogui.click(1201,372)  

#点击预定
pyautogui.click(1164,770)   

#滚动页面
while(not pyautogui.pixelMatchesColor(1120,944, (14, 160, 142))):
    pass
pyautogui.scroll(-10000)
sleep(0.05)

#点击想要预约的时间
for x in list(wanted):
    location_x=(x-17)%3
    location_y=(x-17)//3
    x=base_x+location_x*horizontal
    y=base_y+location_y*vertical
    pyautogui.click(x, y)

#确定预定
pyautogui.click(1170,940)    

# x, y = pyautogui.locateCenterOnScreen('c.png')
# # pyautogui.click(x1, y1)
# print(x,y)
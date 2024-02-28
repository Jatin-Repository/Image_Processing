import cv2 as c
import pyautogui as p
import numpy as np

#Create Resolution
rs = p.size() # screen size of mine
print(rs)
fn = input("Please Enter any file name and path:")
#Fix the frame rate
fps = 0.5

fourcc = c.VideoWriter.fourcc('X','V','I','D')
ouput = c.VideoWriter(fn,fourcc,fps,rs)


c.namedWindow("Live Recording",c.WINDOW_NORMAL)
c.resizeWindow("Live_Recording",(600,400))


while True:
    img = p.screenshot()
    f = np.array(img)
    f  = c.cvtColor(f,c.COLOR_BGR2RGB)
    ouput.write(f)
    c.imshow("Live_Recording",f)
    if c.waitKey(1) & 0xFF == ord("q"):
        break

ouput.release()
c.destroyAllWindows()


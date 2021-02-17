#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tensorflow import keras
from keras.models import load_model
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
import numpy as np 
import cv2
import os 
import random
from pynput.keyboard import Key,Controller
keyboard = Controller()


model = keras.models.load_model('C:/kaggle/newdataset/working/newdata.h5')

def make_1080p():
    cap.set(3,1920)
    cap.set(4,1080)
    

listpred=[]
count = 0

CATEGORIES = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "unknown"]

L0 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
L1 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
L2 = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
L3 = [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
L4 = [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]
L5 = [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
L6 = [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]
L7 = [7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7]
L8 = [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8]
L9 = [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]

 
def act(listpred1):
    LCV = listpred1
    if L0 == LCV :
        # Volume up by 10%
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
       
    elif L1 == LCV:
        # Volume down by 10%
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        
    elif L2 == LCV:
        #Space Bar Press
        keyboard.press(Key.space) 
        keyboard.release(Key.space)
    elif L3 == LCV:
        #Right Arrow Key Press
        keyboard.press(Key.right) 
        keyboard.release(Key.right)
    elif L4 == LCV:
        #Left Arrow Key Press
        keyboard.press(Key.left) 
        keyboard.release(Key.left)
    elif L5 == LCV:
        #Open Google Webpage
        import subprocess
        import webbrowser

        def process_exists(process_name):
            call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
            # use buildin check_output right away
            output = subprocess.check_output(call).decode()
            # check in last line for process name
            last_line = output.strip().split('\r\n')[-1]
            # because Fail message could be translated
            return last_line.lower().startswith(process_name.lower())

        if process_exists('chrome.exe') == True :
            print("Task is already running")
        else :
            webbrowser.open("http://www.google.com")
            
            
    elif L6 == LCV:
        #Play and Pause Music and Video
        keyboard.press(Key.media_play_pause) 
        keyboard.release(Key.media_play_pause)
    elif L7 == LCV:
        print(7)
        
    elif L8 == LCV:
        #Minimize Current Program Screen
        keyboard.press(Key.cmd) 
        keyboard.press(Key.down)
        keyboard.release(Key.cmd)
        keyboard.release(Key.down)
    elif L9 == LCV:
        music_dir = 'C:\Songs n'
        songs = os.listdir(music_dir)
        while True :
            no = random.randint(0,len(songs)-1)
            if os.path.join(music_dir,songs[no]).endswith('.mp3') == True:
                os.startfile(os.path.join(music_dir,songs[no]))
                break
    
    else:
        cv2.putText(frame, CATEGORIES[pred], (50,50),font, 1.0, color, 2)
        
    
    

cap = cv2.VideoCapture(0)
make_1080p()
font = cv2.FONT_HERSHEY_SIMPLEX
while True:

    ret, frame = cap.read()
    cv2.rectangle(frame, (100, 100), (500, 500), (255, 255, 255), 2)
    roi = frame[100:500, 100:500]
    img = cv2.resize(roi, (64,64))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = img.astype('float32')/255
    pred = np.argmax(model.predict(img))
    color = (0,0,255)
    listpred.append(pred)
    count = count + 1 
    if count == 25 :
        act(listpred)
        count = 0
        listpred.clear()
    #cv2.putText(frame, CATEGORIES[pred], (50,50),font, 1.0, color, 2)
    #print(CATEGORIES[pred])
    
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:





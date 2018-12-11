#Coded by:- Kushal Bhavsra
#From:- Techmicra IT solution
import time
import cv2
import label_image
import os,random
import subprocess
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

size = 4
# We load the xml file
classifier = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
global text
webcam = cv2.VideoCapture(0)  # Using default WebCam connected to the PC.
now = time.time()###For calculate seconds of video
future = now + 10  ####here is second of time which taken by emotion recognition system ,you can change it
while True:
    (rval, im) = webcam.read()
    im = cv2.flip(im, 1, 0)  # Flip to act as a mirror
    # Resize the image to speed up detection
    mini = cv2.resize(im, (int(im.shape[1] / size), int(im.shape[0] / size)))
    # detect MultiScale / faces
    faces = classifier.detectMultiScale(mini)
    # Draw rectangles around each face
    for f in faces:
        (x, y, w, h) = [v * size for v in f]  # Scale the shapesize backup
        cv2.rectangle(im, (x, y), (x + w, y + h), (255, 255 ,25), 7)
        # Save just the rectangle faces in SubRecFaces
        sub_face = im[y:y + h, x:x + w]
        FaceFileName = "test.jpg"  # Saving the current image from the webcam for testing.
        cv2.imwrite(FaceFileName, sub_face)
        text = label_image.main(FaceFileName)  # Getting the Result from the label_image file, i.e., Classification Result.
        text = text.title()  # Title Case looks Stunning.
        font = cv2.FONT_HERSHEY_TRIPLEX
        cv2.putText(im, text, (x + w, y), font, 1, (0, 25, 255), 2)

    # Show the image/
    cv2.imshow('Music player with Emotion recognition', im)
    key = cv2.waitKey(30)& 0xff
    if time.time() > future:##after 20second music will play
        try:
            cv2.destroyAllWindows()
            mp = 'C:/Program Files (x86)/Windows Media Player/wmplayer.exe'
            # mp = 'C:/Program Files (x86)/Winamp/winamp.exe'
            if text == 'Angry':
                randomfile = random.choice(os.listdir("C:/Users/kusha/PycharmProjects/Face_Sentiment_analysis/songs/Angry/"))
                print('You are angry !!!! please calm down:) ,I will play song for you :' + randomfile)
                file = ('C:/Users/kusha/PycharmProjects/Face_Sentiment_analysis/songs/Angry/' + randomfile)
                subprocess.call([mp, file])


            if text == 'Smile':
                randomfile = random.choice(os.listdir("C:/Users/kusha/PycharmProjects/Face_Sentiment_analysis/songs/Smile/"))
                print('You are smiling :) ,I playing special song for you: ' + randomfile)
                file = ('C:/Users/kusha/PycharmProjects/Face_Sentiment_analysis/songs/Smile/' + randomfile)
                subprocess.call([mp, file])

            if text == 'Fear':
                randomfile = random.choice(os.listdir("C:/Users/kusha/PycharmProjects/Face_Sentiment_analysis/songs/Fear/"))
                print('You have fear of something ,I playing song for you: ' + randomfile)
                file = ('C:/Users/kusha/PycharmProjects/Face_Sentiment_analysis/songs/Fear/' + randomfile)
                subprocess.call([mp, file])

            if text == 'Sad':
                randomfile = random.choice(os.listdir("C:/Users/kusha/PycharmProjects/Face_Sentiment_analysis/songs/Sad/"))
                print('You are sad,dont worry:) ,I playing song for you: ' + randomfile)
                file = ('C:/Users/kusha/PycharmProjects/Face_Sentiment_analysis/songs/Sad/' + randomfile)
                subprocess.call([mp, file])
            break

        except :
            print('Please stay focus in Camera frame atleast 15 seconds & run again this program:)')
            break

    if key == 27:  # The Esc key
        break



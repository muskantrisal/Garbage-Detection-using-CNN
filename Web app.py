import numpy as np 
import pandas as pd
import os
import keras
import matplotlib.pyplot as plt
from glob import glob 
import cv2
from PIL import Image
from pathlib import Path
from keras.models import load_model
from flask import Flask, request, jsonify, render_template
import smtplib, ssl

model = load_model('final_garbage_detector.h5')

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
print('model loaded')


def predict_fromCCTV(path,model):
    number_of_images = len(path)
    i = 0
    predictions = []
    while i < number_of_images:
        img = cv2.imread(path[i])
        img = cv2.resize(img,(300,300))
        img = np.reshape(img,[1,300,300,3])
        a = model.predict_classes(img)
        if a == 0:
            return True
        else:  
            return False
        i = i+ 1 

path_CCTV1 = glob('C:/Users/My HP Pavilion/Desktop/data sets/CCTV1/*.jpg')
        
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "nikunjjoshi5022@gmail.com"  # Enter your address
receiver_email = "shivamkumar682000@gmail.com"  # Enter receiver address
password = 'Muskan@5022'
message = """\
Subject: Area to be cleaned is found
 
Garbage is found in front of CCTV1 
location:Brij Vihar C-60."""

if predict_fromCCTV(path_CCTV1,model):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)   
print('mail sent')        
        
#@app.route('/', method = ['GET'])
#def home():
 #   return render_template('CCTV.html')

        
#@app.route('/predict', methods=['GET', 'POST'])
#def predict():
 #   if request.method == 'POST':
  #      # Get the image from post request
   #     img = base64_to_pil(request.json)
        
    #    predict=predict_fromCCTV(image,model)
        
     #   return jsonify(predict)
                       
            
                       
                       
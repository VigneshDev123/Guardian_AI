# views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Video
from .forms import VideoUploadForm
import os
import cv2
from tensorflow.keras.models import load_model
import numpy as np
import easygui
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

recipients={"flood":"floodinfoguardian@gmail.com","cyclone":"cycloneinfoguardian@gmail.com"}
def first(request):
    return render(request,"index.html")
def send_email(subject, body, sender, recipients, password, video_path):
  msg = MIMEMultipart()
  msg['Subject'] = subject
  msg['From'] = sender
  msg['To'] = recipients

  # Attach video file
  video_attachment = MIMEBase('application', 'octet-stream')
  video_attachment.set_payload(open(video_path, 'rb').read())
  encoders.encode_base64(video_attachment)
  video_attachment.add_header('Content-Disposition', f'attachment; filename="{video_path}"')
  msg.attach(video_attachment)

    # Add text body
  msg.attach(MIMEText(body, 'plain'))

  with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")
def preprocess_frame(frame):
  resized_frame = cv2.resize(frame, (224, 224))
  normalized_frame = resized_frame / 255.0
  return normalized_frame
def upload_video(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video_file = request.FILES['video']
            video_name=video_file.name
            output_dir=r'C:\Users\ramak\OneDrive\Desktop\guardian_ai\videos'
            video_path=os.path.join(output_dir,video_name) 
            video = Video(file=video_file) 
            cap = cv2.VideoCapture(filename="video", apiPreference=cv2.CAP_FFMPEG)
            video.save()
            easygui.msgbox("Video Uploaded Successfully. Email will be generated in few seconds...","Success")
            flag=0
            disaster_classification =load_model(r'C:\Users\ramak\OneDrive\Desktop\guardian_ai\Models\disaster_classification.h5') 
            real_ai = load_model(r'C:\Users\ramak\OneDrive\Desktop\guardian_ai\Models\real_ai.h5')
            predictions_1= []
            predictions_2=[]
            while cap.isOpened():
              ret, frame = cap.read()
              if not ret:
                break
            # Preprocess the frame
              preprocessed_frame = preprocess_frame(frame)

              # Expand dimensions to match the shape expected by the model
              preprocessed_frame = np.expand_dims(preprocessed_frame, axis=0)

              # Perform inference with the model
              prediction = real_ai.predict(preprocessed_frame)
              predictions_1.append(prediction)

            # Close the video file
            cap.release()

            # Analyze the predictions to determine the overall classification result
            average_prediction = np.mean(predictions_1, axis=0)
            result = np.argmax(average_prediction)

            # Interpret the result
            if result == 0:
              flag=1
              print("The video is classified as real.")
            else:
              print("The video is classified as AI-generated.")
            if(flag==1):
              while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                  break
              # Preprocess the frame
                preprocessed_frame = preprocess_frame(frame)

                # Expand dimensions to match the shape expected by the model
                preprocessed_frame = np.expand_dims(preprocessed_frame, axis=0)

                # Perform inference with the model
                prediction = disaster_classification.predict(preprocessed_frame)
                predictions_2.append(prediction)
                average_prediction = np.mean(predictions_2, axis=0)
                result = np.argmax(average_prediction)
              cap.release()
              if result == 0:
                print("The video is classified as Flood.")
                latitude, longitude ="12.8259° N", "80.0413° E"
                print("Latitude:", latitude)
                print("Longitude:", longitude)
                subject = "Flood Alert"
                body = "Geolocation:Latitude:"+latitude+"longitude:"+longitude
                sender = "yourmailid@gmail.com"
                password = "********"
                send_email(subject, body, sender, recipients["flood"], password, video_path)
              else:
                disaster_type="cyclone"
                print("The video is classified as Cyclone.")
                latitude, longitude ="12.8259° N", "80.0413° E"
                print("Latitude:", latitude)
                print("Longitude:", longitude)
                subject = "Cyclone Alert"
                body = "Geolocation:Latitude:"+latitude+"longitude:"+longitude
                sender = "ramakrishnanvignesh705@gmail.com"
                password = "jrgs nkrg kfsu cddk"
                send_email(subject, body, sender, recipients["cyclone"], password, video_path)
              easygui.msgbox("Email Sent!!","Success")
            else:
              easygui.msgbox("You posted Invalid video Input. Try to provide authenticated input")    
    else:
        form = VideoUploadForm()
    return render(request, 'index.html', {'form': form})



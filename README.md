
## GUARDIAN AI: A MACHINE LEARNING MODEL FOR SWIFT RECOGNITION, VALIDATION, AND ALERTING OF UNUSUAL INCIDENTS

This project is a machine learning-based system designed to classify disaster videos, determine their authenticity (real or AI-generated), and extract geolocation data for real videos. If a video is classified as real, the system sends an email with the type of event, the video file, and the extracted geolocation data.

## Table of Contents

- [Project Overview](#project-overview)
- [Key Components](#key-components)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
## Project Overview

This project aims to classify videos into different types of disasters, check their authenticity, and extract geolocation data for real videos. The system then sends an email with relevant details to the concerned Authorities.

## Key Components

1. **Video Classification**:
   - **Disaster Type Classification**: Classify videos into various unusual incidents include natural and man-made disasters and physical and mental abuses, etc.,
   - **Authenticity Check**: Determine if the video is real or AI-generated.

2. **Geolocation Extraction**:
   - Extract geolocation data (latitude and longitude) from the video's metadata for videos classified as real.

3. **Email Notification**:
   - Send an email containing the type of disaster event, the video file, and the extracted geolocation data.

4. **User Interface**:
   - Develop a front-end using Django to allow users to upload videos.
   - Process the uploaded videos through the machine learning models and display the results.

## Requirements

- Python 3.x
- Django
- OpenCV
- TensorFlow/Keras
- Pyngrok
- ExifRead (for geolocation extraction)
- SMTP server or email service for sending emails

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/VigneshDev123/Guardian_AI
   cd Guardian_AI
   ```

2. **Create a virtual environment and activate it**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Django**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser  # Follow the prompts to create a superuser
   ```

5. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

6. **Start Ngrok**:
   ```python
   from pyngrok import ngrok
   public_url = ngrok.connect(port='8000')
   print('Public URL:', public_url)
   ```

## Usage

1. **Upload Videos**: Access the User Interface and upload the video
2. **Process Videos**: The system will classify the videos, check their authenticity, and extract geolocation data for real videos.
3. **Email Notification**: If the video is real, an email will be sent with the type of disaster event, the video file, and the geolocation data to the concerned Authorities

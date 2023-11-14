import PIL
from PIL import ImageGrab
import os
from datetime import datetime
import requests
import json

# Taking Screenshot Function
def screenshot():
    screenshot = ImageGrab.grab()
    screenshot_file = "Screenshot.png"
    screenshot_path = screenshot.save(screenshot_file)
    return screenshot_file

# Sending API request Function
def api_request(image_path,remarks,phone):
    url = "https://trogon.info/interview/python/index.php/"
    image_file = {'image':open(image_path,'rb')}
    data = {'remarks':"App Name",'phone':"9048419922"}
    response = requests.post(url,files=image_file,data=data)
    print(response.json())
    return response.json()

if __name__ == "__main__":
    remarks = "Screenshot App"
    phone = "1234567890"

    screenshot_path = screenshot()
    response = api_request(screenshot_path,remarks,phone)

    if response.get('status') == 'sucsess':
        print("Screenshot Uploaded successfully")
    else:
        print("Failed to upload screenshot. Error:",response['message'])



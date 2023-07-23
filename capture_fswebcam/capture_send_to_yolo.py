import subprocess
import requests
import schedule
import time
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
captured_folder  = os.path.join(current_directory, "captured")

def capture_and_send():
	try:
		timestamp = time.strftime("%Y%m%d_%H%M%S")
		image_path = f"{captured_folder}/image_{timestamp}.jpg"
		skip_frames = 20
		command = f"fswebcam -r 1920x1080 --no-banner -S {skip_frames} {image_path}"
		subprocess.run(command, shell=True, check=True)
	
		with open(image_path, 'rb') as f:
			image_data = f.read()
		
		files = {'image': (image_path, image_data, 'image/jpeg')}
		
		
		url = 'yolov5_endpoint'
		
		response = requests.post(url, files=files)
		if response.status_code == 200:
			print('Image sent succesfully!')
		else:
			print('Failed to send the image. Status code: ', response.status_code)
	except Exception as e:
		print('Error occurred while capturing or sending the image: ', e)

schedule.every(4).hours.do(capture_and_send)

while True:
	schedule.run_pending()
	time.sleep(1)

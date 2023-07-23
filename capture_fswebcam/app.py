import os
import time
from flask import Flask, send_file
import subprocess

app = Flask(__name__)

def capture_image():
	timestamp = time.strftime("%Y%m%d_%H%M%S")
	image_path = f"/home/orangepi/Desktop/capture_fswebcam/captured/image_{timestamp}.jpg"
	skip_frames = 20
	command = f"fswebcam -r 1920x1080 --no-banner -S {skip_frames} {image_path}"
	subprocess.run(command, shell=True, check=True)
	return image_path

@app.route('/capture', methods=['GET'])
def capture_and_send_image():
	image_path = capture_image()
	return send_file(image_path, mimetype="image/jpeg")

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=5000)

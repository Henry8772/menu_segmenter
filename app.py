from flask import Flask, render_template, redirect, url_for
import os
import glob

app = Flask(__name__)
IMAGE_FOLDER = 'image_folder'

@app.route('/')
def index():
    # Get list of image files in the folder
    images = glob.glob(os.path.join(IMAGE_FOLDER, '*.jpg'))  # Adjust as per image type
    # Extract just the filenames (excluding path) for display/selection
    image_filenames = [os.path.split(image)[-1] for image in images]
    return render_template('index.html', images=image_filenames)

@app.route('/review/<filename>')
def review(filename):
    # Load and display the image alongside extracted text/boxes for user review.
    # Implement interaction using JavaScript/Canvas for user review and confirmation.
    return render_template('review.html', image_filename=filename)

if __name__ == "__main__":
    app.run(debug=True)

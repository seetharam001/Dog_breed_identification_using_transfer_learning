from flask import Flask, render_template, request
import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# load trained model
model = load_model("dogbreed.h5")

# class labels
class_names = [
'affenpinscher','beagle','appenzeller','basset','bluetick','boxer',
'cairn','doberman','german_shepherd','golden_retriever',
'kelpie','komondor','leonberg','mexican_hairless','pug',
'redbone','shih-tzu','toy_poodle','vizsla','whippet'
]

# Home page
@app.route('/')
def home():
    return render_template('index.html')


# Step 1: Upload image → show processing page
@app.route('/predict', methods=['POST'])
def predict():

    file = request.files['image']
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    filepath = os.path.abspath(filepath)
    file.save(filepath)

    # show processing page
    return render_template("predict.html", filepath=filepath)


# Step 2: Actual prediction → show result page
@app.route('/result')
def result():

    filepath = request.args.get('filepath')
    filepath = os.path.abspath(filepath)

    # preprocess image
    img = image.load_img(filepath, target_size=(224,224))
    img = image.img_to_array(img)
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    # predict
    preds = model.predict(img)
    index = np.argmax(preds)
    prediction = class_names[index]

    return render_template("output.html", prediction=prediction)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

# run app
if __name__ == "__main__":
    app.run(debug=True)
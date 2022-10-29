from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired

application = Flask(__name__)
app = application
application.config['SECRET_KEY'] = 'supersecretkey'
application.config['UPLOAD_FOLDER'] = 'static/files'

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

@application.route('/', methods=['GET',"POST"])
@application.route('/home', methods=['GET',"POST"])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data # First grab the file
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),application.config['UPLOAD_FOLDER'],secure_filename(file.filename))) # Then save the file
        # Getting uploaded file name
        img_filename = secure_filename(file.filename)
        # Storing uploaded file path in flask session
        uploaded_img_path = os.path.join(application.config['UPLOAD_FOLDER'], img_filename)
        return render_template("uploaded_successfully.html",user_image = uploaded_img_path)
    return render_template('index.html', form=form)

if __name__ == '__main__':
    application.run(debug=True)

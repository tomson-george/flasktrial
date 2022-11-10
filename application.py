from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired

application = Flask(__name__)
app = application
application.config['SECRET_KEY'] = 'supersecretkey'
application.config['UPLOAD_FOLDER'] = '/static/files'

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

@application.route('/', methods=['GET',"POST"])
@application.route('/home', methods=['GET',"POST"])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data # First grab the file
        # Getting uploaded file name
        img_filename = secure_filename(file.filename)
        # file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),application.config['UPLOAD_FOLDER'],secure_filename(file.filename))) # Then save the file
        filepath = os.path.join(application.config['UPLOAD_FOLDER'], secure_filename(file.filename))
        file.save(filepath)
        #filepath = os.path.join(app.config['UPLOAD_FOLDER'], img_filename)
        #file.save(filepath)
        return render_template("uploaded_successfully.html",user_image = filepath)
    return render_template('index.html', form=form)

if __name__ == '__main__':
    application.run(debug=True)
    # application.run(host='0.0.0.0', port = '8080')

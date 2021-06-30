# noinspection PyUnresolvedReferences
import json
from flask import Flask, jsonify, request, redirect, url_for, render_template, flash
from werkzeug.utils import secure_filename
# noinspection PyUnresolvedReferences
import os
# noinspection PyUnresolvedReferences
import numpy as np
# noinspection PyUnresolvedReferences
import cv2
# from predict_bdr import *
# noinspection PyUnresolvedReferences
import time
from datetime import timedelta
from PIL import Image
# noinspection PyUnresolvedReferences
from predict_picture import *
from predict import *

app = Flask(__name__)

UPLOAD_FOLDER = 'static/images/upload'  # 上传的文件保存目录
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}  # 允许的上传文件类型

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=5)
print(app.config['SEND_FILE_MAX_AGE_DEFAULT'])

# model = predict_init()  # 导入模型，以便节省Predict时间


def allow_filename(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    # 文件名必须有效


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('not file part!')
            return redirect(request.url)

        f = request.files['file']
        if f.filename == '':
            flash('not file upload')
            return redirect(request.url)

        if f and allow_filename(f.filename):
            filename = secure_filename(f.filename)
            # secure_filename 不支持中文文件名称的获取……

            filepath = './' + app.config['UPLOAD_FOLDER'] + '/' + f.filename
            f.save(filepath)
            img = predict_brain(filepath,filename)
            # print(img)
            # img = np.array(Image.open('./upload/'+filename))
            outfilename = 'images/output/'+filename
            return render_template('upload_ok.html',outfilename = outfilename ,inputfilename='images/upload/'+filename)
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)

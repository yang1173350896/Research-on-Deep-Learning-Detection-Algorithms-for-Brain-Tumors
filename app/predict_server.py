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
# noinspection PyUnresolvedReferences
from trans_color import *
# noinspection PyUnresolvedReferences
from imageA_B import *

app = Flask(__name__)

UPLOAD_FOLDER = 'static/images/upload'  # 上传的文件保存目录
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}  # 允许的上传文件类型

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=5)
print(app.config['SEND_FILE_MAX_AGE_DEFAULT'])




def allow_filename(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    # 文件名必须有效


@app.route('/BrainTumor', methods=['GET', 'POST'])
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
            #上传文件保存
            filepath = './' + app.config['UPLOAD_FOLDER'] + '/' + f.filename
            f.save(filepath)
            #脑肿瘤检测
            predict_picture1(filepath,filename)
            predict_picture4(filepath, filename)
            #改变检测肿瘤颜色并融合
            trans_lv(filename)
            trans_red(filename)
            image_lv_and_red(filename)
            #输出图片地址
            outfilename1 = 'images/output1/'+filename
            outfilename3 = 'images/output3/' + filename
            outfilename4 = 'images/output4/' + filename
            #输出图片地址传入网页
            return render_template('upload_ok.html',outfilename1 = outfilename1 ,outfilename3 = outfilename3,outfilename4 = outfilename4,inputfilename='images/upload/'+filename)
    return render_template('BrainTumor.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
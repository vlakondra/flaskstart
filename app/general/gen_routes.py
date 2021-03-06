from email import message
from pyexpat.errors import messages
from webbrowser import get
from flask import ( Blueprint, flash, g, after_this_request,
 redirect, render_template, current_app,
  request,  url_for, jsonify,send_from_directory,send_file)
from flask import session as sess
import requests

from werkzeug.utils import secure_filename
import os,sys

import shutil
import zipfile

# from flask import current_app

from app import db

bp_gen = Blueprint('general', __name__, template_folder='templates')
print('name - general', __name__)


@bp_gen.route('/')
@bp_gen.route('/index' )
def index():
    return render_template(
        '/general/index.html',
        title='Home Page',
    )


@bp_gen.route('/getdata')
def get_data():
    text = request.args.get('txt', 0, type=str)

    if text.lower() == 'python':
        return jsonify(result='Выбран правильный язык')
    else:
        return jsonify(result='Попробуйте еще')


@bp_gen.route('/session')
def session():
    return render_template(
        '/general/session.html',
        title='Сессия',
    )


@bp_gen.route('/getsession')
def get_session():
    if request.method == 'GET':
        data = {
            'fam': request.args.get('fam'),
            'age': request.args.get('age'),
            'session': [{'математика': 5},
                        {'Экономика': 4},
                        {'Информатика': 5}]
        }

        print(data)

        return jsonify(data)


@bp_gen.route('/carusel')
def owl():
    return render_template(
        '/general/owl.html',
        title='Карусель',
    )



# @bp_gen.after_app_request
# def clear_sess(response):
#     print("???",response)
#     sess['file_mess']=""
#     return response


@bp_gen.route('/file')
def file():
    
  return render_template(
        '/general/upload.html',
        title='Выгрузка файла',
        mess=sess.get( 'file_mess',"")
    )    

@bp_gen.route('/savefile',methods=['POST'])
def savefile():
    if request.method == 'POST':
      print(request.files)

      if 'datafile' not in request.files:
          return redirect(request.origin+url_for('general.file',message="Сохранение файла невозможно"))

      txt = request.form['taria'] 
      print('TEXT-ARIA ', txt)


      sl = request.form.getlist('sel')
      print('SEL: ', sl )
       
      file = request.files['datafile']  
      fls =  request.files.getlist("datafile") 
      filename = secure_filename(file.filename) #mimetype
      #https://stackoverflow.com/questions/11817182/uploading-multiple-files-with-flask

      print('arr? ',type(file), file,type(fls), fls)

      print("filename",file.filename)
      print('secfilename ',filename)  
      print('cwd',os.getcwd())


      for f in fls:
          print("from file list",f.mimetype)

  
      sess['file_mess']= filename

      file.save(os.path.join(current_app.config['UPLOAD_FOLDER'],filename))
    #   return redirect(request.origin+url_for('general.file',message="Файл "+ filename+ " сохранен"))
     
      files=os.listdir(current_app.config['UPLOAD_FOLDER'])
      print(files)
     
      return redirect(request.origin+url_for('general.file'))



#############

@bp_gen.route('/loadfile')
def load():
  return render_template(
        '/general/down.html',
        title='Загрузка файла',
    ) 

@bp_gen.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename,as_attachment=True)

@bp_gen.route('/downfiles')
def downfiles():

    shutil.make_archive(current_app.config['TMP_FOLDER'] +'/'+'myfiles','zip',current_app.config['UPLOAD_FOLDER'])

    # zf = zipfile.ZipFile(current_app.config['TMP_FOLDER'] +'/'+'myfiles.zip','w', compression = zipfile.ZIP_STORED) # Compression type 

    # for  files in os.walk(current_app.config['UPLOAD_FOLDER']):
    #     for file in files:
    #         zf.write(current_app.config['UPLOAD_FOLDER'] +'/'+file)
    # zf.close()

    return send_file(current_app.config['TMP_FOLDER'] +'/'+'myfiles.zip',
            mimetype = 'zip',
            attachment_filename=  'myfiles.zip',
            as_attachment = True)







@bp_gen.route('/req')
def req():
  url = 'https://old.ursei.su/Services/GetGsSched'
  
  # https://old.ursei.su/Services/GetGsSched?grpid=26033&yearid=26&monthnum=5
  # https://betacode.net/12451/html-list

  params = dict( grpid=26033, yearid=26,monthnum=5)

  resp = requests.get(url=url, params=params)
  data = resp.json()
#   print(data)

  return render_template(
        '/general/req.html',
        title='Расписание')


@bp_gen.route('/getgroups')
def getgroups():
    if request.method == 'GET':
        url='https://old.ursei.su/Services/GetGSSchedIniData'
        resp = requests.get(url=url)
        data = resp.json()
        # print(data)
        return jsonify(data)


from email import message
from pyexpat.errors import messages
from webbrowser import get
from flask import ( Blueprint, flash, g, after_this_request,
 redirect, render_template, current_app,
  request,  url_for, jsonify,send_from_directory)
from flask import session as sess

from werkzeug.utils import secure_filename
import os,sys
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
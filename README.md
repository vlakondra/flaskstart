--Рабочий вариант 1
image: 
  file:  .gitpod.Dockerfile

tasks:
  # - name: start
- before: |
    pyenv virtualenv flvenv
    source activate flvenv

    export FLASK_APP=learnflask
    export FLASK_ENV=development
      
    pip install flask
  init:  |
    echo "проверка init"
    #   source activate flvenv
    #   pip install Flask  



ports:
  - port: 5000
    onOpen: open-preview

--Рабочий вариант 2    

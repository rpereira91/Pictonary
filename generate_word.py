from flask import Flask, render_template,request
import random
# from flask_bootstrap import Bootstrap
app = Flask(__name__)
# Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def method_name():
    diff = ['Easy',
    'Medium',
    'Hard',
    'Objects',
    'HOTS']
    if request.method=='POST':
        difficulty = request.form.get('difficulty')
        return render_template('index.html',diff=diff,selected=difficulty, word=get_word(difficulty))
    return render_template('index.html',diff=diff)
    
def get_word(difficulty):
    file_path = "word-lists/" + difficulty.lower()+".txt"
    text_file =  open(file_path,'r')
    words = text_file.read().split('\n')
    return words[random.randint(0,len(words)-1)]

if __name__ == '__main__':
  app.run(host= '127.0.0.1', port=5000, debug=True)
 
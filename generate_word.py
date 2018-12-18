from flask import Flask, render_template,request
import random
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def method_name():
    diff = ['Easy',
    'Medium',
    'Hard',
    'Object',
    'HOTS']
    if request.method=='POST':
        difficulty = request.form.get('difficulty')
        return render_template('index.html',diff=diff,selected=difficulty, word=get_word(difficulty))
    return render_template('index.html',diff=diff)
def get_word(difficulty):
    if difficulty == 'Easy':
        text_file =  open("word-lists/easy.txt", "r")
        words = text_file.read().split('\n')
        return words[random.randint(0,len(words)-1)]
    elif difficulty == 'Medium':
        text_file =  open("word-lists/medium.txt", "r")
        words = text_file.read().split('\n')
        return words[random.randint(0,len(words)-1)]
    elif difficulty == 'Hard':
        text_file =  open("word-lists/hard.txt", "r")
        words = text_file.read().split('\n')
        return words[random.randint(0,len(words)-1)]
    elif difficulty == 'Object':
        text_file =  open("word-lists/objects.txt", "r")
        words = text_file.read().split('\n')
        return words[random.randint(0,len(words)-1)]
    elif difficulty == 'HOTS':
        text_file =  open("word-lists/hots.txt", "r")
        words = text_file.read().split('\n')
        return words[random.randint(0,len(words)-1)]
    
    return "NO WORD"
if __name__ == '__main__':
  app.run(host= '127.0.0.1', port=8000, debug=True)
 
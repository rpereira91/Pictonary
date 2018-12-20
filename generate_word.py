from flask import Flask, render_template,request,redirect,url_for
import random,time
from apscheduler.schedulers.background import BackgroundScheduler
from hue_control import HueControl

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def method_name():
    diff = ['Easy',
    'Medium',
    'Hard',
    'Objects',
    'HOTS']
    if request.method=='POST':
        difficulty = request.form.get('difficulty')
        scheduler.remove_all_jobs()
        start = start_time()
        scheduler.add_job(check_time, 'interval', seconds=1,args=(start,))
        if not scheduler.running:
            scheduler.start()
        return render_template('index.html',diff=diff,selected=difficulty, word=get_word(difficulty))
    return render_template('index.html',diff=diff)
    
def get_word(difficulty):
    file_path = "word-lists/" + difficulty.lower()+".txt"
    text_file =  open(file_path,'r')
    words = text_file.read().split('\n')
    start_time()
    return words[random.randint(0,len(words)-1)]

def check_time(s_time):
    if (time.time()-s_time) > 10:
        hc.flash_blubs()
        scheduler.remove_all_jobs()
def start_time():
    return time.time()

if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    hc = HueControl('192.168.1.3')
    app.run(host= '127.0.0.1', port=8000, debug=True)
 
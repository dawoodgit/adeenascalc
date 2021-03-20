from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        number = int(request.form['number'])
        times = int(request.form['times'])
        your_ans = int(request.form['your_ans'])
        if your_ans==number*times:
            return render_template('index.html',prediction_text= f"{number}x{times} = {your_ans}.  Right Answer!")
        else:
            return render_template('index.html',prediction_text= f"Beda Gharq!!!  {number}x{times} equals {number*times} not {your_ans}")
        
    
    
    else:
        return render_template('index.html')
    
if __name__=="__main__":
    app.run()

from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/",methods=['GET'])
def home():
    return render_template('home.html')

@app.route("/add",methods=['GET'])
def addition():
    return render_template('add.html')

@app.route("/addpredict", methods=['POST'])
def addpredict():
    if request.method == 'POST':
        number = int(request.form['number'])
        times = int(request.form['times'])
        your_ans = int(request.form['your_ans'])
        if your_ans == number+times:
            return render_template('add.html',addprediction_text= f"{number} + {times} = {your_ans}.  Right Answer!")
        else:
            return render_template('add.html',addprediction_text= f"Beda Gharq!!!  {number} + {times} equals {number+times} not {your_ans}")

@app.route("/subt",methods=['GET'])
def subtraction():
    return render_template('subt.html')

@app.route("/subtpredict", methods=['POST'])
def subtpredict():
    if request.method == 'POST':
        number = int(request.form['number'])
        times = int(request.form['times'])
        your_ans = int(request.form['your_ans'])
        if your_ans == number-times:
            return render_template('subt.html',subtprediction_text= f"{number} - {times} = {your_ans}.  Right Answer!")
        else:
            return render_template('subt.html',subtprediction_text= f"Beda Gharq!!!  {number} - {times} equals {number-times} not {your_ans}")

@app.route("/mult",methods=['GET'])
def multiplication():
    return render_template('mult.html')

@app.route("/multpredict", methods=['POST'])
def multpredict():
    if request.method == 'POST':
        number = int(request.form['number'])
        times = int(request.form['times'])
        your_ans = int(request.form['your_ans'])
        if your_ans==number*times:
            return render_template('mult.html',multprediction_text= f"{number}x{times} = {your_ans}.  Right Answer!")
        else:
            return render_template('mult.html',multprediction_text= f"Beda Gharq!!!  {number}x{times} equals {number*times} not {your_ans}")

@app.route("/division",methods=['GET'])
def division():
    return render_template('division.html')

@app.route("/divisionpredict", methods=['POST'])
def divpredict():
    if request.method == 'POST':
        number = int(request.form['number'])
        times = int(request.form['times'])
        your_ans = int(request.form['your_ans'])
        if your_ans==number/times:
            return render_template('division.html',divprediction_text= f"{number} / {times} = {your_ans}.  Right Answer!")
        else:
            return render_template('division.html',divprediction_text= f"Beda Gharq!!!  {number} / {times} equals {number/times} not {your_ans}")
        
    
        
if __name__=="__main__":
    app.run(debug=True)

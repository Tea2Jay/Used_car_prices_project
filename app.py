from flask import Flask , render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
    
@app.route('/',methods=['POST'])
def pred():
    data1 = request.form
    print(data1)
    return render_template('home.html')
    
if __name__ == '_main__':
    app.run(debug=True)
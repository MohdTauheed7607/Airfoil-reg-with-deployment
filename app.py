import pickle
import sklearn
from flask import Flask,request,jsonify,url_for,render_template



app=Flask(__name__)

# @app.route('/predict_api',methods=['POST'])
# def predict_api():
#     data=request.json['data']
#     print(data)
#     fin_data=[list(data.values())]
#     model=pickle.load(open(r'E:\i neuron\FSDS 2.0\ML\New folder\28thmay\model.pkl','rb'))
#     predict_result=model.predict(fin_data)[0]
#     print(predict_result)
#     return jsonify(predict_result)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict',methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()]
    print(data)
    final_data=[data]
    print(final_data)
    model=pickle.load(open(r'E:\i neuron\FSDS 2.0\ML\New folder\28thmay\model.pkl','rb'))
    output=model.predict(final_data)[0]
    return render_template('home.html',prediction_text='Pressure level is {}'.format(output))



if __name__=='__main__':
    app.run(debug=True)
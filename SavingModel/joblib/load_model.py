import joblib

model = joblib.load('dib_23.pkl')
output = model.predict([[0,0.7,0.3,0.7,0.6,1,2,0.7]])
if output[0] == 1:
    print('Diabatic')
else:
    print('not diabetic')
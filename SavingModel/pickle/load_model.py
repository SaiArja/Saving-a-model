import pickle

model = pickle.load(open('dib_23.pkl','rb'))
output = model.predict([[0,0.7,0.3,0.7,0.6,1,2,0.7]])
if output[0] == 1:
    print('Diabatic')
else:
    print('not diabetic')

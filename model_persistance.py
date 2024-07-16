# import dataset
# create a model
# train it
# and then ask it to make predictions


# joblib object has methods for saving and loading modules
# joblib to have our trained model in a file
# the .dump() method gives us an array that contains the name of our model file
# in a real application we don't want to train a model every time, so comment out the model and the training code
# then load the file joblib.load('music-recommender.joblib')

'''done in jupyter notebook'''

# import pandas as pd
# from sklearn.tree import DecisionTreeClassifier
# import joblib

# # music_data = pd.read_csv('music.csv')
# # X = music_data.drop(columns=['genre'])
# # y = music_data['genre']

# # model = DecisionTreeClassifier()
# # model.fit(X, y)

# # joblib.dump(model, 'music-recommender.joblib')

# model = joblib.load('music-recommender.joblib')
# predictions = model.predict([[21, 1]])
# print(predictions)

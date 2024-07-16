'''done in jupyter notebook'''
# then get the .dot file and open it in vs code
# open live preview to see the visualization of the tree

# import pandas as pd
# from sklearn.tree import DecisionTreeClassifier
# import joblib
# from sklearn import tree
#
#
# music_data = pd.read_csv('music.csv')
# X = music_data.drop(columns=['genre'])
# y = music_data['genre']
#
#
# model = DecisionTreeClassifier()
# model.fit(X, y)
#
# tree.export_graphviz(model, out_file='music-recommender.dot',
#                      feature_names=['age', 'gender'],
#                      class_names=sorted(y.unique()),
#                      label='all', rounded=True,
#                      filled=True)

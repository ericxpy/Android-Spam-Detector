from sklearn.externals import joblib

def predict(X):
    # Load the model and the vectorizer
    clf = joblib.load('/home/ubuntu/django_projs/tutorial/myapp/DNN.pkl')
    vectorizer = joblib.load('/home/ubuntu/django_projs/tutorial/myapp/vec3.pkl')

    # Generate features
    Xvec = [X]
    features_test = vectorizer.transform(Xvec)

    # Do the prediction and output the result
    pred = clf.predict(features_test)
    result = pred[0]

    if result == 0:
        return 'false'
    else:
        return 'true'

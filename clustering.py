__author__ = 'daijing'
import loader
import numpy as np
from sklearn import cluster
from sklearn.preprocessing import StandardScaler

def split_data(rows, d = 0):
    train = []
    validate = []
    if (d==0):
        for id in rows:
            train.append(id)
    else:
        for id in rows:
            if (id % d ==0):
                validate.append(id)
            else:
                train.append(id)
    return train, validate

def get_feature_vector(rows, dataset):
    feature_vector = []
    columns = ["temperature", "humidity", "windSpeed"] #,"precipitation"]
    for id in dataset:
        s = []
        for col in columns:
            s.append(float(rows[id].info[col]))
        feature_vector.append(s)
    feature_matrix= np.array(feature_vector)
    return feature_matrix

def kmeans_fitting(rows, train):
    x = get_feature_vector(rows, train)
    scaler = StandardScaler()
    scaler.fit(x)
    x = scaler.transform(x)
    model = cluster.MiniBatchKMeans(n_clusters = 6)
    model.fit(x)
    centers = model.cluster_centers_
    print centers
    centers = scaler.inverse_transform(centers)
    print centers
    return model, scaler

def predict(model, pred_features, scaler):
    pred_features = scaler.transform(pred_features)
    y_pred = model.predict(pred_features)
    return y_pred

if __name__ == '__main__':
    reload(loader)
    file = 'NY_State_Historical_Weather_Clusters.csv'
    rows = loader.load_weather(file)
    training_set, validation_set = split_data(rows)
    cl_model, scaler = kmeans_fitting(rows, training_set)
    y = predict(cl_model, [[4.78733,0.69,12.9847]], scaler)
    print y


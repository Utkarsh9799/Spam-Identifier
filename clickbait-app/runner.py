from sklearn.externals import joblib
import os

script_dir = os.path.dirname(__file__)
model_path = os.path.join(script_dir,r'static',r'clickbaitmodelsklearn.pkl')
m1 = joblib.load(model_path)


def score(input_headline):
    pred_score = m1.predict_proba([input_headline])[0]
    if ((pred_score[1]*100 > 40) & ((pred_score[1]*100 < 60))):
        flag = 'Maybe a Bait'
        color = 'is-warning'
    elif (pred_score[1]*100 > 60):
        flag = 'Baity'
        color = 'is-danger'
    else:
        flag = 'Looks Safe'
        color = 'is-success'

    prob = {'clickbait-prob': round(pred_score[1],3), 'notClickbait-prob': round(pred_score[0],3), 'flag': flag, 'color':color}
    return prob

if __name__ == "__main__":
    result = scoring('You won’t believe how these 9 shocking clickbaits work!')
    print(result)

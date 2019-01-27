# IdeaHack-SpamIdentifier

### Clickbait Checker
Web application to check if the news headline is a clickbait or not and deciding wheather a message is spam.

### Requirements
* Python modules (- pandas, - numpy, - scipy, - scikit-learn, - pickle, - flask, - pdb, - sys, - os)



### Running  the App
********************************************************* < Optional > *********************************************************

You may want to create a virtual environment as follows:

1. Create a virtual environment :
          ```virtualenv <YOUR_VIRTUALENV_NAME> ```
  2. Activate virtual environment :
          ```source <YOUR_VIRTUALENV_NAME>/bin/activate - Linux```
          ```<YOUR_VIRTUALENV_NAME>\Scripts\activate - Windows```
 
 ********************************************************* </ Optional > ********************************************************
 
 Installing Dependencies (Ignore if already done)
 
 
          pip install jupyter pandas numpy scipy sklearn
          (jupyter is optional)
          pip intsall pickle
          pip install Flask
          (pdb, sys and os modules installs by default while installing python, in case not you can use pip to install them)

To run the app  navigate to the project folder in bash and run the following command :

```bash
python main.py
```
This will run the app at  http://127.0.0.1:8083

### The Application

The model used for prediction of clickbait used a corpus of clickbait and non-cickbait data aggregated from various sources.<br>
The `clickbait-detection.ipnyb` shows the model training and its accuracy. The `clickbaitmodelsklearn.pkl` file stores the serialised object which is used for prediction.<br>
The `main.py` and `runner.py` files host the flask app and score the headline in runtime.<br>

<p align="center"><img src="https://github.com/Eklavya42/clickbait-webapp/blob/master/screenshots/ss1.png?raw=true"/></p>
<p align="center"><img src="https://github.com/Eklavya42/clickbait-webapp/blob/master/screenshots/ss2.png?raw=true"/></p>
<p align="center"><img src="https://github.com/Eklavya42/clickbait-webapp/blob/master/screenshots/ss3.png?raw=true"/></p>

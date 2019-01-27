# IdeaHack-SpamIdentifier

### Clickbait Checker
Web application to check if the news headline is a clickbait or not.



### Running  the App
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

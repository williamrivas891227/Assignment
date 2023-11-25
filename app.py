from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def homepage():
    
    return render_template("index.html")

@app.route('/gif', methods= ["GET","POST"])
def getMovie():
    print("sdin")

    url = "https://api.giphy.com/v1/gifs/search"
    params = {
        'api_key':"G4ApKkVoSe4U7wMl7ocO8AbfpahoTaA2",
        "q":request.form.get("q"),
        
    }
    
    #'api_key':"G4ApKkVoSe4U7wMl7ocO8AbfpahoTaA2",
	
    
    response=requests.get(url,params=params)
    data = response.json()
    gifs=data.get('data', [])
    
    
    
    return render_template('index.html', gifs=gifs)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5004)
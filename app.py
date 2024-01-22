import requests
import configparser
from flask import Flask, render_template, request
from forms import SignUpForm


def get_api_key():
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config['WEATHERMAPAPIKEY']['API_KEY']


def url(api_key, zipcode, country_code):
    return "https://api.openweathermap.org/data/2.5/weather?zip=" + zipcode + "," + country_code + "&appid=" + api_key


# r = requests.get(url(get_api_key(), ZIP_CODE, Country_Code))
# print(r.json())

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ANKUR'


@app.route('/')
def dashboard():
    return render_template('/html/dashboard.html')


@app.route('/return', methods=['POST'])
def return_page():
    zipcode = request.form['zipcode']
    country_code = request.form['country_code']
    r = requests.get(url(get_api_key(), zipcode, country_code))
    data = r.json()
    temp = str(data["main"]["temp"])
    # return temp
    return render_template('/html/result.html', temp=temp)

@app.route('/<int:zipcode>')
def weather(zipcode):
    # return "This is a weather report for " + zipcode
    posts = [{'title':"Biology", 'author':"Ankur"},{'title':"Maths", 'author':"Anky"}]
    return render_template('/html/blog.html', zipcode=zipcode,posts=posts)


@app.route('/SignUp', methods=['GET','POST'])
def SignUp():
    form = SignUpForm()
    if form.is_submitted():
        result = request.form
        return render_template('/html/user.html',result=result)
    return render_template('/html/signup.html',form=form)


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8000)

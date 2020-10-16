from flask import Flask, render_template, url_for
import infoGrabber, stateInfoGrabber, usInfoGrabber, getNews
import os

app = Flask(__name__)

stateInfo = stateInfoGrabber.getStateData("MN")
usInfo = usInfoGrabber.getUSData()
worldInfo = infoGrabber.getInfo()
newsInfo = getNews.getNewsInfo()
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title= "Home", usInfo = usInfo, stateInfo = stateInfo, worldInfo = worldInfo)
@app.route("/news.html")
def news():
    return render_template('news.html', title="News", newsInfo = newsInfo)
@app.route("/prevention.html")
def prevention():
    return render_template('prevention.html', title="Prevention")
@app.route("/references.html")
def references():
    return render_template('references.html', title="References")
@app.route("/about.html")
def about():
    return render_template('about.html', title="About")
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

if __name__ == '__main__':
    app.run(debug=True)
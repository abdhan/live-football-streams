from flask import Flask, render_template, request, url_for, flash
from stream import stream
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/streams', methods = ['POST'])
def viewstreams():
    team = request.form['team']
    l = stream(team)
    links = []
    if l not in links:
        links.append(l)
        print (links)
        return render_template("streams.html", team = team, links = links)




if __name__ == '__main__':
    app.run(debug = True)




























import flask
app = flask.Flask(__name__)
@app.route("/")
def index():
    movies =['Money Heist','Squid Game','3%','Hawaii Five-0',"Prison Break"]
    favorites = ['Money Heist', 'Squid Game']
    pics = ['Money Heist.jpg', 'Squid Game.jpg', '3%.jpg', 'Hawaii50.jpg',"Prisonbreak.jpg"]
    return flask.render_template("index.html",length = len(movies), movies = movies, fav = favorites, pic = pics)
app.run()
from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route('/')
def home_page():
        return render_template('index.html')

@app.route('/culture-page')
def culture_page():
    return render_template('culture.html')


@app.route('/history-page')
def history_page():
    return render_template('history.html')

# HISTORY PLACES PASS PLACE
@app.route('/historical-places')
def historical_places():
     return render_template('histplaces.html')

@app.route('/cuisine')
def cuisine():
    return render_template('cuisine.html')


@app.route('/festivals-traditions')
def festivals():
    return render_template('festivals.html')


@app.route('/art-and-handicraft')
def art():
    return render_template('arthand.html')


@app.route('/ottomans-empire')
def ottomans():
    return render_template('ottoman.html')


@app.route('/republic-of-turkey')
def reptur():
    return render_template('turrep.html')


@app.route('/byzantine-constantinopole')
def byzant():
    return render_template('byzera.html')


if __name__ == "__main__":
        # app.run(host='0.0.0.0', port="5000", debug=True)
        app.run()


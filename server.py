from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html', row=8, col=8, color1 = 'black', color2 = 'peachpuff')

@app.route('/4')
def rect_checkerboard():
    return render_template('index.html', row=4, col=8, color1 = 'black', color2 = 'peachpuff')

@app.route('/<int:row>/<int:col>')
def checkerboard(row, col):
    return render_template('index.html', row=int(row), col=int(col), color1 = 'black', color2 = 'peachpuff')

@app.route('/<int:row>/<int:col>/<string:color1>/<string:color2>')
def checkerboard_color(row, col, color1, color2):
    return render_template('index.html', row=int(row), col=int(col), color1 = color1, color2 = color2)

if __name__ == "__main__":
    app.run(debug=True)

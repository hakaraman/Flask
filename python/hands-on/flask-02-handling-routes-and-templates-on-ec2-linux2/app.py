from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def head():
    first = "This is my first condition experience in Flask"
    return render_template("index.html")

@app.route("/for")
def for_example():
    names = ['Feyzullah', 'Muhammed', 'Bulent', 'Murat', 'Veysel', 'Serdar']
    return render_template("deneme.html", isimler = names)
if __name__ == '__main__':
    app.run(debug = True)







if __name__ == '__main__':
    app.run(debug = True)
    #app.run(host='0.0.0.0', port=80)
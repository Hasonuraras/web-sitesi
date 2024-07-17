# Import
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

# İçerik sayfasını çalıştırma
@app.route('/')
def index():
    return render_template('index.html')


# Dinamik beceriler
@app.route('/', methods=["GET",'POST'])
def process_form():
    if request.method == "POST":
        button_python = request.form.get('button_python')
        button_discord = request.form.get('button_discord')
        button_html = request.form.get('button_html')
        button_db = request.form.get('button_db')
        return render_template('index.html', button_python=button_python,
                                            button_discord=button_discord,
                                            button_html=button_html,
                                            button_db=button_db)
    else:
        render_template("index.html")



@app.route('/feedback', methods=['POST'])
def process_feedback():
    email = request.form["email"]
    comment = request.form.get("text")
    with open(f"{email}.txt", "w", encoding="utf-8") as doc:
        doc.write(f"{email}\n{comment}")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)



import sqlite3
from flask import Flask, template_rendered, render_template
app = Flask(__name__)
con = sqlite3.connect('data.db', check_same_thread=False)
cursor = con.cursor()

@app.route("/find/")
def mainpage():
        cursor.execute('select * from medicines')
        data = cursor.fetchall()
        return render_template('preparati.html', data= data)

app.run(debug=True)
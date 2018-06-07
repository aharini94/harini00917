from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

import sqlite3

conn = sqlite3.connect('database.db')
# print("Opened database successfully")

conn.execute('CREATE TABLE xy (name TEXT, grade TEXT, room TEXT, tel TEXT, picture TEXT, keyword TEXT)')
print("Table created successfully")
conn.close()



@app.route('/')
def home():
   return render_template('home.html')

@app.route('/enternew')
def new_student():
   return render_template('student.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         name = request.form['name']
         grade = request.form['grade']
         room = request.form['room']
         tel = request.form['tel']
         picture = request.form['picture']
         keyword = request.form['keyword']
         
         with sql.connect("database.db") as con:
            cur = con.cursor()
            
            cur.execute("INSERT INTO xy (name,grade,room,tel,picture,keyword) VALUES (?,?,?,?,?,?)",(name,grade,room,tel,picture,keyword) )
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("result.html",msg = msg)
         con.close()

@app.route('/list')
def list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from xy")
   
   rows = cur.fetchall();
   return render_template("list.html",rows = rows)

if __name__ == '__main__':
   app.run(debug = True)





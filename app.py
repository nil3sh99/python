from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Setitng up application -- referencing to name file
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# /// is relative path
# //// is absolute path

# initialize DB from the settings of our app
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default = 0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id
    
with app.app_context():
        db.create_all()

# Setting up routes
# adding two methods, POST and GET
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        #  passing the id of the content for which we want to post
         task_content = request.form['content']
        #  create a todo model
         new_task = Todo(content=task_content)
        #  adding entries to the DB
         try:
              db.session.add(new_task)
              db.session.commit()
              return redirect('/')
         except:
              return 'There was an issue adding your task'
    else:
        #  quering our DB --> look into all of the DB contents in the order of their date_created
         tasks = Todo.query.order_by(Todo.date_created).all()
        #  need to pass this to our template
         return render_template('index.html', tasks = tasks)
        # no need to specify the folder name ^^ as it looks for the file name



# New route for delete
@app.route('/delete/<int:id>')
def delete(id):
     task_to_delete = Todo.query.get_or_404(id)

     try:
          db.session.delete(task_to_delete)
          db.session.commit()
          return redirect('/')
     except:
          return 'There was a problem deleting that task'
     

# New route for update
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
     task = Todo.query.get_or_404(id)
     if request.method == 'POST':
         #  passing the id of the content for which we want to post
         task.content = request.form['content']
        
        #  adding entries to the DB
         try:
              db.session.commit()
              return redirect('/')
         except:
              return 'There was an issue updating your task'
     else:
          return render_template('update.html', task = task)


if __name__ == "__main__":
    app.run(debug = True)

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista temporária (array)
tarefas = []

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        nova_tarefa = request.form.get('tarefa')
        if nova_tarefa:
            tarefas.append(nova_tarefa)
        return redirect(url_for('home'))  
 
    return render_template('index.html', tarefas=tarefas)

if __name__ == '__main__':
    app.run(debug=True)
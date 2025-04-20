from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/classifica')
def classifica():
    # Qui metti la logica per recuperare i dati della classifica
    classifica_piloti = [
        {'pilota': 'Lewis Hamilton', 'punteggio': 380},
        {'pilota': 'Max Verstappen', 'punteggio': 350},
        {'pilota': 'Charles Leclerc', 'punteggio': 240},
    ]
    return render_template('classifica.html', classifica=classifica_piloti)

if __name__ == '__main__':
    app.run(debug=True)

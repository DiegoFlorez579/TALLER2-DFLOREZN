from flask import Flask, jsonify, render_template
from models.gato import Gato
from models.perro import Perro
from models.huron import Huron
from models.boa_constrictor import Boa_Constrictor
import os

app = Flask(__name__)

animales = {
    "gato": Gato("Whiskers", 4.5, 2),
    "perro": Perro("Rex", 10.0, 3),
    "huron": Huron("Fuzzy", 1.2, 1, "Argentina", 15.0),
    "boa_constrictor": Boa_Constrictor("Slither", 25.0, 5, "Brasil", 20.0)
}

@app.route('/')
def documentacion():
    return render_template('documentacion.html')

@app.route('/animales', methods=['GET'])
def obtener_animales():
    return jsonify({nombre: animal.hacer_sonido() for nombre, animal in animales.items()})

@app.route('/animales/<nombre>', methods=['GET'])
def obtener_animal(nombre):
    animal = animales.get(nombre.lower())
    print(animal)
    if animal:
        return jsonify({"nombre": animal.obtener_nombre(), "sonido": animal.hacer_sonido()})
    return jsonify({"error": "Animal no encontrado"}), 404

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

from flask import Flask, jsonify, request
from repositories.persona_repository import PersonaRepository
from services.persona_service import PersonaService

app = Flask(__name__)
service = PersonaService(PersonaRepository())

@app.get("/personas")
def listar():
    return jsonify([p.to_dict() for p in service.listar()])

@app.get("/personas/<int:dni>")
def obtener(dni):
    try:
        return jsonify(service.obtener(dni).to_dict())
    except LookupError as e:
        return jsonify(error=str(e)), 404

@app.post("/personas")
def crear():
    data = request.get_json()
    try:
        persona = service.crear(data["dni"], data["nombre"])
        return jsonify(persona.to_dict()), 201
    except (ValueError, KeyError) as e:
        return jsonify(error=str(e)), 400

@app.put("/personas/<int:dni>")
def modificar(dni):
    data = request.get_json()
    try:
        return jsonify(service.modificar(dni, data["nombre"]).to_dict())
    except LookupError as e:
        return jsonify(error=str(e)), 404
    except (ValueError, KeyError) as e:
        return jsonify(error=str(e)), 400

## @app.delete("/personas/<int:dni>")
## def eliminar(dni):
##    try:
##        service.eliminar(dni)
##        return "", 204
##    except LookupError as e:
##        return jsonify(error=str(e)), 404

if __name__ == "__main__":
    app.run(debug=True)
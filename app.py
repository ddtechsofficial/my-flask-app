from flask import Flask
from flask_jwt_extended import JWTManager
from routes.students import students_bp
from routes.auth import auth_bp


app = Flask(__name__)

app.secret_key = "ddt"
app.config["JWT_SECRET_KEY"] = "jwt-secret-ddt"

jwt = JWTManager(app)

app.register_blueprint(students_bp, url_prefix="/api")
app.register_blueprint(auth_bp, url_prefix="/auth")


# app.run(debug=True)

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)


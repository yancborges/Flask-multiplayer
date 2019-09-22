# Modules

from flask import Flask, request, jsonify, make_response, render_template
# Consts

DB_NAME = "test"
USER_PASSWORD = '123'

# Config

app = Flask(__name__)
app.secret_key='hiddenpass'

@app.route('/joken-po', method=['POST'])
def joken_po():
    if()

	

# Running

if __name__ == '__main__':
    app.secret_key='hiddenpass'
    app.run(debug=True)


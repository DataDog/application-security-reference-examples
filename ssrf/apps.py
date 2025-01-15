from flask import Flask
from website import create_app
import subprocess


app = create_app()


if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=5000)
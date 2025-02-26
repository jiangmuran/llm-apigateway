import argparse
from flask import Flask

def cli():
    parser = argparse.ArgumentParser(description="Open Api Gateway Webui.Debug your AI programs with ease through a web-based interface. Modify inputs and outputs, and leverage the power of custom Python filters.\n\n Github: https://github.com/jiangmuran/llm-apigateway")
    parser.add_argument('--host', type=str, default="127.0.0.1", help='Host to open the webui.')
    parser.add_argument('--port', type=str, default="10049", help='Port to open the webui.')
    args = parser.parse_args()
    host = args.host
    port = args.port
    print("Opening webui on http://" + host + ":" + port)
    print("API route: http://"+host+":"+port+"/v1")
    run_flask_app(host, port)

def run_flask_app(host, port):
    app = Flask(__name__)

    @app.route('/')
    def home():
        return "Hello world!"

    app.run(host=host, port=int(port))

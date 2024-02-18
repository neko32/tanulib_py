
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import json

class CatInfo:
    def __init__(self, name, pattern):
        self.name = name
        self.pattern = pattern

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys = True, indent = 4, ensure_ascii = False)

store = {"Shima": CatInfo("Shima", "Tabby"), "Torachan": CatInfo("Tora", "orangetabby")}

class SimpleRestServer(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path.startswith("/neko"):
            # [TODO] add try except 
            print(self.path)
            parsed_url = urlparse(self.path)
            queries = parse_qs(parsed_url.query)
            print(queries)
            names = queries["name"]
            if len(names) == 0:
                resp_code = 400
                resp_body = "{}"
            elif names[0] not in store:
                resp_code = 204
                resp_body = "{}"
            else:
                resp_code = 200
                resp_body = store[names[0]].toJSON()

            self.send_response(resp_code)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(resp_body, "utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(bytes("{}", "utf-8"))

def build_simple_rest_srv() -> HTTPServer:
    return HTTPServer(("localhost", 8030), SimpleRestServer)

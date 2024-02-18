from unittest import TestCase, main
from http.server import HTTPServer
from tlib.testutil import *
import threading
import requests
import time

websrv = None

class SimpleRestSrvTest(TestCase):

    def run_srv(self):
        global websrv
        print("starting rest ..")
        websrv = HTTPServer(("localhost", 8030), SimpleRestServer)
        websrv.allow_reuse_address = True
        self.server_thread = threading.Thread(target = websrv.serve_forever(), daemon = True) 
        #self.server_thread.start()

    def setUp(self):
        self.server_thread = threading.Thread(target = self.run_srv, daemon = True) 
        self.server_thread.start()

    def tearDown(self):
        global websrv
        print("shutting down rest ..")
        websrv.shutdown()
        if self.server_thread.is_alive():
            self.server_thread.join()

    def testGet(self):
        time.sleep(2)
        resp = requests.get("http://localhost:8030/neko?name=Shima")
        self.assertEqual(resp.status_code, 200)
        js = resp.json()
        self.assertEqual(js['name'], "Shima")
        resp204 = requests.get("http://localhost:8030/neko?name=Tako")
        self.assertEqual(resp204.status_code, 204)

        # [TODO] add 400

if __name__ == "__main__":
    main()

from tlib.testutil import *

def main() -> None:
    srv = build_simple_rest_srv()
    try:
        print("running simple rest server..")
        print("try the below command from console:")
        print("curl -X GET http://localhost:8030/neko?name=Shima")
        srv.serve_forever()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()

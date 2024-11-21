from flask import Flask, request, Response
import requests

app = Flask(__name__)

# route onr-isr traffic
@app.route('/onr-isr/<path:subpath>', methods=["GET", "POST"])
def onr_isr(subpath):
    port = 5000
    return relay_request(f"http://localhost:{port}/{subpath}")

# example route for cec traffic
@app.route('/cec', methods=["GET", "POST"])
def cec(subpath):
    return relay_request(f"https://cec.gatech.edu")

# simple proxy: relays the request and returns the response
def relay_request(url, request):
    try:
        # forward the request to the target
        response = requests.request(
            method=request.method,
            url=url,
            headers={key: value for key, value in request.headers if key != 'Host'},
            data=request.get_data(),
            cookies=request.cookies,
            allow_redirects=False
        )
        # return the response back to the client
        return Response(
            response.content,
            status=response.status_code,
            headers=dict(response.headers)
        )
    except requests.exceptions.RequestException as e:
        return f"ERROR: {url}: {str(e)}", 502

# run the server
if __name__ == "__main__":
    print("Launching relay server")
    app.run(host="0.0.0.0", port=8080)

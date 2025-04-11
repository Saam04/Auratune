from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/callback')
def spotify_callback():
    code = request.args.get("code")
    if code:
        return f"Authentication successful! Your code: {code}"
    else:
        return "Error: No code received from Spotify"

if __name__ == '__main__':
    app.run(port=8080)

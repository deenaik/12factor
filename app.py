from flask import Flask

app = Flask(__name__)

# Global variable to keep track of the number of visits
visitCount = 0

@app.route('/')
def WelcomeToKodeKloud():
    global visitCount
    # Increment the visit count
    visitCount += 1
    return "Welcome to KodeKloud! Visit Count: " + str(visitCount) + "\n"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)


from flask import Flask
from redis import Redis

app = Flask(__name__)
# RedisDB to keep track of the number of visits
redisDb = Redis(host='redis', port=6380)


@app.route('/')
def WelcomeToKodeKloud():
    # Increment the visit count
    redisDb.incr('visitCount')
    visitCount = str(redisDb.get('visitCount').decode('utf-8'))
    return "Welcome to KodeKloud! Visit Count: " + str(visitCount) + "\n"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)


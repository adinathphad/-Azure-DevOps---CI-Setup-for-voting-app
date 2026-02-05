# Flask = lightweight web framework to build frontend quickly
from flask import Flask, request, render_template_string

# Redis client library to send votes to Redis queue
import redis

# Used to read environment variables inside Docker
import os


# Create Flask app
app = Flask(__name__)

# Get Redis host name from docker-compose service name
# Docker automatically provides DNS between containers
redis_host = os.getenv("REDIS_HOST", "redis")

# Connect to Redis server
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)


# Simple HTML page (no templates to keep project simple)
HTML = """
<h2>Vote Your Favorite Animal 🗳️</h2>
<form method="POST">
<button name="vote" value="cats">Cats 🐱</button>
<button name="vote" value="dogs">Dogs 🐶</button>
</form>
"""


# When user opens page OR submits vote
@app.route("/", methods=["GET", "POST"])
def vote():

    # If vote submitted
    if request.method == "POST":

        # Read button value (cats/dogs)
        choice = request.form["vote"]

        # Push vote into Redis list (acts like queue)
        # rpush = add item at right side of list
        r.rpush("votes", choice)

    return render_template_string(HTML)


# Start server on port 80 inside container
app.run(host="0.0.0.0", port=80)

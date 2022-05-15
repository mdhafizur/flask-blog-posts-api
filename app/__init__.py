import time
from flask import Flask, Response, request
import json

import requests
import requests_cache

requests_cache.install_cache('posts_cache', backend='sqlite', expire_after=100)


def create_app():
    app = Flask(__name__)

    @app.route("/api/ping/", methods=["GET"])
    def api_ping():
        return Response(json.dumps({
            "success": True
        }), status=200, mimetype="application/json")

    @app.route("/api/posts/")
    def get_posts():
        data = []
        tags = request.args.get('tags', default=None)
        sortBy = request.args.get('sortBy', default=None)
        direction = request.args.get('direction', default=None)

        ALLOWED_SORT_BY = ["id", "reads", "likes", "popularity"]
        ALLOWED_DIRECTION = ["asc", "desc"]

        if not tags:
            return handle_error("Tags parameter is required")

        if not sortBy:
            sortBy = "id"
        if not direction:
            direction = "asc"

        if tags or tags is not None:
            tags = tags.split(",")
            if len(tags) <= 0 or not tags:
                return handle_error("Tags parameter is required")

        if direction is not None and direction not in ALLOWED_DIRECTION:
            return handle_error("sortBy parameter is invalid")

        if sortBy is not None:
            if sortBy not in ALLOWED_SORT_BY:
                return handle_error("sortBy parameter is invalid")

        for tag in tags:
            url = "https://api.hatchways.io/assessment/blog/posts?tag={}".format(
                tag)
            now = time.ctime(int(time.time()))
            response = requests.get(url)
            print("Time: {0} / Used Cache: {1}".format(now,
                  response.from_cache))
            posts = json.loads(response.text)['posts']
            for post in posts:
                data.append(post)
            data = list({v['id']: v for v in data}.values())

        if sortBy is not None and direction is not None:
            data = sorted(
                data, key=lambda d: d[sortBy], reverse=direction == "desc")

        return Response(json.dumps({
            "posts": data
        }), status=200, mimetype="application/json")

    def handle_error(error):
        return Response(response=json.dumps({
            "error": error
        }), status=400,
            mimetype="application/json")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(threaded=True, processes=3)

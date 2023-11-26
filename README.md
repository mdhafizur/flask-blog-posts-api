# Flask Blog Posts API

This is a simple Flask-based API for retrieving blog posts based on specified tags, with optional sorting and direction
parameters. The blog posts are fetched from the Hatchways Blog API.

## Installation

Clone the repository:

```bash
git clone https://github.com/mdhafizur/flask-blog-posts-api.git
```
Create a VirtualEnv 

Install the required dependencies:
```bash
pip install -r requirements.txt
```

Usage
Run the Flask application:

```bash
python app.py
```

## API Endpoints

### Ping Endpoint

- **Method:** `GET`
- **Path:** `/api/ping/`
- **Description:** Pings the API to check if it's running.

### Posts Endpoint

- **Method:** `GET`
- **Path:** `/api/posts/`
- **Description:** Retrieves blog posts based on specified tags, with optional sorting and direction parameters.

#### Query Parameters

- **tags (required):** Comma-separated list of tags.
- **sortBy (optional):** Sorting parameter (allowed values: "id", "reads", "likes", "popularity").
- **direction (optional):** Sorting direction (allowed values: "asc", "desc").

## Caching

The application uses requests caching with an SQLite backend. The cache is configured to expire after 100
seconds (`expire_after=100`). This helps improve response times by serving cached data for repeated requests within the
expiration period.

## Example

To retrieve posts with tags "python" and "flask," sorted by "popularity" in descending order:

```bash
curl -X GET "http://127.0.0.1:5000/api/posts/?tags=python,flask&sortBy=popularity&direction=desc"
```

## Error Handling

If a required parameter is missing or invalid, the API returns a JSON response with an error message and a `400` status
code.

## Notes

- The application is configured to run in threaded mode with three processes (`app.run(threaded=True, processes=3)`).
  Adjust these parameters based on your deployment environment.
- The fetched posts are unique based on their "id" values to avoid duplicates.
- The application prints the time of each request and indicates whether the response was served from the cache.

Feel free to customize and extend this Flask application based on your specific requirements!

**App Requirements**
![Request Requirenets](https://github.com/mdhafizur/blog-posts-flask-api/blob/main/images/request_requirements.png?raw=true)

![Response Example](https://github.com/mdhafizur/blog-posts-flask-api/blob/main/images/response_requirements.png?raw=true)

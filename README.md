# FastAPI endpoint template

A FastAPI endpoint template that can be cloned and/or forked to create new endpoints based off the simple one implemented here.


# Installation

We assume Python, `pip`, and `git` are installed, as well as an internet connection.

1. Clone the repository by running `git clone "https://github.com/JordiCarreraVentura/fastapi_endpoint_template"`.
2. Install the dependencies with `python3.11 -m pip install -r requirements.txt`.


# Running the server

1. Start the server by executing `uvicorn main:app --reload`. INFO: _The `--reload` flag ensures that the app reloads if there are any changes in the source code._
2. On an internet browser, go to "http://127.0.0.1:8000" (localhost). The app description should be visible there. If so, the server started up successfully and is running.
3. To submit a request to the server,
   1. run the following command on the command line:
    ```
    curl -X 'POST' \
      'http://localhost:8000/predict/' \
      -H 'Content-Type: application/json' \
      -d '{
         "prefix": "ves"
    }'
    ```
   2. Alternatively, navigate to FastAPI's UI at `http://127.0.0.1:8000/docs`, where  for the endpoint can be tested conveniently tweaking manually the parameters of the call.


# References

1. [FastAPI Tutorial: Build APIs with Python in Minutes](https://www.kdnuggets.com/fastapi-tutorial-build-apis-with-python-in-minutes)
2. [Using FastAPI for Building ML-Powered Web Apps](https://www.kdnuggets.com/using-fastapi-for-building-ml-powered-web-apps)


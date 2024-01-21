# Flask App Routing
from flask import Flask

# create a simple web application
app = Flask(__name__) # we are creating the object for Flask that specifies the entry point of program.


if __name__ == "__main__": # entry point of the application
    app.run(debug = True)
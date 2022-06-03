# Portfolio tracker 
![Black](https://img.shields.io/static/v1?label=code%20style&message=black&color=black&style=flat-squar) 
![tests](https://img.shields.io/github/workflow/status/m-janusz/Portfolio-Tracker/tests)

Python program which helps with tracking of your portfolio. Works as web-app hosted offline on your localhost.

## Installation

Clone the repository to your machine
```
git clone https://github.com/m-janusz/Portfolio-Tracker.git
```
or using ssh
```
git clone git@github.com:m-janusz/Portfolio-Tracker.git
```

move to application directory

### Using Docker (Platform Independent)

You need to have [Docker](https://docs.docker.com/get-docker/) software installed. 

Build `docker` image in repository
```
docker build -t <your-image-name> <path-to-respository>
```
Run the app with your image name on port 8501.
```
docker run -d --name <container-name> -p 8501:8501 <your-image-name>
```
Example:
```
docker build -t tracker:latest .
docker run -d --name portfolio-tracker -p 8501:8501 tracker
```

App should be available  on http://localhost:8501/ in your browser.

### Using Python (Linux)

create virtual environment, for example
```
python3 -m venv venv
```

enter into the virtual environment
```
. venv/bin/activate
```

install application dependencies
```
pip install -r requirements.txt
```

run the application
```
streamlit run portfolio_tracker.py
```

You should see the local address of your application in console.
Default address is http://localhost:8501/

## Testing ✔️
Testing could be done using pytest framework or built-in python unit tests.

using unit-test
```
python3 -m unittest -v
```

using pytest
```
python3 -m pytest -v
```

to add more tests, create them in tests directory in compliance to [unittest documentation](https://docs.python.org/3/library/unittest.html).

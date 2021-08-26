## Objective

This is a sample python Point of Sale system API. Currently, it covers the following functional requirements:

The system will only control the menu and order CRUD operations. The POS system should have the following capabilities
- Retrieve a menu of all the items in the POS. An item can have description, a price, a quantity and an ID
- Add a new item to the menu
- Update an item by ID
- Delete an item by ID
- Create a new order. An order should contain
	-a list of item IDs, with a quantity for each item
	- a payment amount
	- an order note
	- Creating a successful order should return the order ID
- Each route should perform business logic validation to prevent common errors. The order endpoint specifically should enforce payment correctness, and item availability.

### How to use (Docker)
```bash
git clone git@github.com:Shahed-Zaman/POS-sampleAPI.git
docker build -t mysample-pos-api ./POS-sampleAPI
docker run -d --name mysample-pos-server -p 80:80 mysample-pos-api
```
As per the docker run command above, the API server will listen at port 80

## How to use (in a Linux based Dev machine)
```bash
git clone git@github.com:Shahed-Zaman/POS-sampleAPI.git
cd POS-sampleAPI
# assuming python3 and virtualenv is already installed and available in PATH of the dev machine
# if not, please install python3 and virtualenv, add them to PATH
virtualenv -p `which python3` venv3
source venv3/bin/activate
# Install required python modules; following command is expected to finish without any error
pip install -r requirements.txt
# Set PYTHONPATH so that python interpreter can find modules
export PYTHONPATH=${PYTHONPATH}:${PWD}/src
# Run the following command to start the web application using uvicorn
python -m uvicorn src.main:app --reload
```
Once started, you can see the API endpoints and related docs here: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### Tech Stack choice:
Here, we are building this API in python [FastAPI](https://fastapi.tiangolo.com/)

Overall starting point for this project started from [this specific guide](https://fastapi.tiangolo.com/tutorial/sql-databases/?h=sqlalchemy#sql-relational-databases)

### Tech stack:
- Python
- SQLite
- ORM - [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://pydantic-docs.helpmanual.io/) - API input validation
- [FastAPI](https://fastapi.tiangolo.com/) - web framework for building API
- [Uvicorn](https://www.uvicorn.org/) - web server

## Unit tests 
Testcase for this project are under `tests` dir. Please run `pytest`
For development convenience, a script to bootstrap some dummy data is provided under `tests/create_dummydata.py`

## Next ToDo

[❌] Currently not covered: An item can contain modifier groups, with each modifier group containing modifiers. For example
Item: Burger
Modifier Group 1: Toppings
    Modifiers: Lettuce, Tomato, Pickles, Onions
Modifier Group 2: Bun Choice
    Modifiers: Sesame, Whole Wheat, Keto





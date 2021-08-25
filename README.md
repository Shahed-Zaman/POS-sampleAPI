## Objective

For now, here is a brief description of the sample API and it's capabilities we aim to build.

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
Provide the project in a github repo or a zip file
The project should run out of the box, if an included README is followed
BONUS IF YOU HAVE TIME: An item can contain modifier groups, with each modifier group containing modifiers. For example

Item: Burger
Modifier Group 1: Toppings
    Modifiers: Lettuce, Tomato, Pickles, Onions
Modifier Group 2: Bun Choice
    Modifiers: Sesame, Whole Wheat, Keto



## Next ToDo
[ ✅] Unit tests

[ ❌] Check/add DB level constraints
    - on delete cascade
    - prevent deleting

[ ❌] Create Dockerfile, deployment notes

[ ❌] Research on modifier groups

[❌ ] add to github

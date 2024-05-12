# pickerApp

an automated picking app to reduce errors and boost efficiency for warehouses.

## how to run MAC OS

## Create a virual enviroment

`python3 -m venv testenv`

`source test/bin/activate`

## install dependacies on the backend

`cd Backend/pickingApp`

`pip install -r requirements.txt`

## run backend

`python3 manage.py runserver`

django should now be running on http://localhost:8000/

## install dependacies on the frontend

`cd Frontend/pickingapp_react`

`npm install`

`npm start`

the app should now be running on http://localhost:3000/

## notes

with db.sqlite3 file commited to this repo you don't have to run any migrations, however to reset test data in database to the original test data run the script

`python3 manage.py runscript populate`

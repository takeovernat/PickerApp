# pickerApp

an automated picking app to reduce errors and boost efficiency for warehouses.

## how to run MAC OS

## Create a virual enviroment

`python3 -m venv testenv`

`source test/bin/activate`

## install dependacies on the backend

`cd Backend/pickingApp`

`pip install -r requirements.txt`

## run banceknd

`python3 manage.py runserver`

django should now be running on http://localhost:8000/

## install dependacies on the frontend

`cd Frontend/pickingapp_react`

`npm install`

`npm start`

## notes

to reset test data in database run the script

`python3 manage.py runscript populate`

To get this running, simply run the  the following 

## Step 1: Install requirements.txt

`pip install -r requirements.txt`

## Step 2: Create databases

Create the databases and the initial migrations with the following command:
`python manage.py migrate`

## Step 3: Run server

And start the server with 

`python manage.py runserver`

You should now be able to go to localhost:8000/

## Step 4: call /show from Telegram app to get three buttons which will show 
## values "Stupid","Fat","Dumb". 
## On clicking on any of them, respective joke will be displayed on screen
## which will automatically update postgres DB at the backend to record number of hits
## to each of the buttons


## Step 5 : call URL localhost:8000/callinfo from browser
## this URL will display a table/grid showing no of calls per buttons

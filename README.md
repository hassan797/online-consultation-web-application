# eHealth-consultation

An online consultation system that supports Creating an account as a Doctor or Patient, booking appointments without any conflicts, and seeing, updating and deleting records.

Install requirements by running `pip install -r requirements.txt`

##### ESSENTIAL FILES ARE IN APPOINTMENTS FOLDER ####
### To run
`python manage.py makemigrations`
`python manage.py migrate`
`python manage.py runserver 8000`
Then open your browser on localhost:8000

### Usage:
Signup as a Patient -> Modify your account -> Click Book appointment -> Choose a Doctor from list of doctors -> Select time -> Check your list of appointments and manage as you like -> Check your billing report

Signup as a Doctor-> Modify your account -> Check your appointments -> Check your patients and their records

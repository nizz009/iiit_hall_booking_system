# IIIT Auditorium Hall Management Web-app
A management system(web-app) built using Django (Python framework) aiming to reduce the complicacies involved in booking auditorium halls, especifically for International Institute of Information Technology, Bhubaneswar (IIIT-Bh).

## Features:
<ol>
  <li>Schedule to keep track of current events for each hall</li>
  <li>Approved events are automatically added to the schedule</li>
  <li>Separate login for admins and students</li>
  <li>Safety features to avoid unauthorised event approval by the students</li>
</ol>

## Local Set-up:

### Cloning the project

#### Note:
This project is entirely based on <a href="https://www.djangoproject.com/">Django</a> (<a href="https://www.python.org/">Python<a> framework). Make sure to install both, <a href="https://wiki.python.org/moin/BeginnersGuide/Download">Python<a> and <a href="https://docs.djangoproject.com/en/3.2/intro/install/">Django</a> on your system.

Now, it's time to get the project to our local devices.
#### Step 1: Check the directory
Head over to the directory where you want to save the project. You can do so using the ```cd``` command: <br>
``` cd <directory_file_path> ```

#### Step 2: Git Clone
Clone the project to your device using the command below: <br>
 ``` git clone https://github.com/nizz009/iiit_hall_booking_system ```
 
### Running the project

#### Step 1: Check the directory, again
Head over to the main (root) directory of the <em>cloned repo</em>. If you are in the directory in which you ran the git clone command, then simply follow the command below: <br>
``` cd iiit_hall_booking_system ```

#### Step 2: Create superuser
Superusers are allowed to access the admin page which is used for management of the tables, etc. Create a superuser using the following command: <br>
``` python manage.py createsuperuser ```

Enter the username and the password that you desire.

#### Step 3: Run the migrations
Migrations are important to keep our database up-to date or ensure that the databases are up-to date. Run the following commands to run the migrations: <br>
``` python manage.py makemigrations ```
followed by: <br>
``` python manage.py migrate ```

#### Step 4: Run the project!
Kudos! You are almost done with setting up the project in your local computer. In order to run it, use the following command: <br>
``` python manage.py runserver ```

Once the server is set, you can access the web-app typing ``` localhost:8000/hbms/ ``` in the address bar of your web browser.


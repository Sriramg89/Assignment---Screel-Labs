# Assignment: Screel-Labs

### Main.py, Database.py and Model.py are the three Python files used in the assignment. The HTML files named Main.html, Candidate.html and home.html are cretaed to design 3 web pages.

**Main.py**: This Python script is used for sending GET,POST, DELETE requests using Fast API framework. SQL Alchemy ORM modules are also used to create functions that communicate with the database. Database used is SQLite.

**Database.py**: Creates database classes and instances using SQLAlchemy engine. Sessions are created to interact with the database. 

**Model.py**: This file contains tables as classes along with their members.



**Main.html** : This file contains code for the starting career portal web page with options to navigate to recruiter and candidate portals. Jquery and Ajax are used to send requests to the databases. The web page is designed using Javascript, HTML and Semantic UI CSS. Semantic UI CSS and associated JQuery links are referenced.

**Candidate.html** : This file conatins Javascript, HTML and Semantic UI CSS to design the candidate portal.

**Home.html** : Recuiter portal webpage.

### Directions to run the webpages - 

1. Run the virtual environment already setup in the folder by running Activate.ps1 under the folder named *virtual* on command prompt.

2. All dependencies have to be installed by running the command: *pip install -r requirements.txt* on the shell.

3. Run all three Python files. The database file has already been created in the folder.

4. After setting the Python interpreter to 'virtual', run the command *uvicorn Main:job*.

5. Use the address http://127.0.0.1:8000 to open the webpage and navigate



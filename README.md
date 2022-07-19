Install python3.5 and above.
Clone the project to your computer.
Python comes with a package manager like NPM called pip.
Install virtualenv -> pip install virtualenv
Build the virtualenv in your project folder -> virtualenv venv
Activate the virtualenv -> source venv/Scripts/activate or source venv/bin/activate
Once the virtualenv is activated start installing the python modules you need.
in this case, requirements.txt will have the required modules.
just -> pip install -r requirements.txt
Place a file inside the folder then write the name when prompted example -> file.txt, number.pdf
Go to both client.py and server.py file. find this text -> # Owen change this ip to your computer's.
Change the ip address to your local system ip address. find ip  using -> ifconfig for mac or ipconfig for windows
first run the server. 
The server is in server/server.py -> python server.py
the client -> python client.py


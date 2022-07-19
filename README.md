1)Install python3.5 and above.
2)Clone the project to your computer.
3)Python comes with a package manager like NPM called pip.
4)Install virtualenv -> pip install virtualenv
5)Build the virtualenv in your project folder -> virtualenv venv
6)Activate the virtualenv -> source venv/Scripts/activate or source venv/bin/activate
7)Once the virtualenv is activated start installing the python modules you need. in this case, requirements.txt will have the required modules. just -> pip install -r requirements.txt
8)Place a file inside the folder then write the name when prompted example -> file.txt, number.pdf
9)Go to both client.py and server.py file. find this text -> # Owen change this ip to your computer's.
10)Change the ip address to your local system ip address. find ip  using -> ifconfig for mac or ipconfig for windows
11)first run the server. 
12)The server is in server/server.py -> python server.py
13)the client -> python client.py


# telemetry-django-server
## Python REST server based on Django and Django Rest Framework

### ```telemetry_django_server``` Dependencies
* ```python3.8 -m pip install django```
* ```python3.8 -m pip install djangorestframework```
* ```python3.8 -m pip install markdown       # Markdown support for the browsable API.```
* ```python3.8 -m pip install django-filter  # Filtering support```

### ```ios_sensor_pack``` Specific Dependencies:
* ```python3.8 -m pip install numpy```
* ```python3.8 -m pip install astropy```
* ```python3.8 -m pip install pytz```

## Running Server

### Create Dataabase
```bash
python3.8 manage.py makemigrations ios_sensor_pack
python3.8 migrate
```

### Create Superuser
```bash
python3.8 manage.py createsuperuser
```

### Create Test User
```bash
python3.8 manage.py shell
```
Then in the shell, add the following python code:
```python
from django.contrib.auth import get_user_model
UserModel = get_user_model()
user = UserModel.objects.create_user('test1', 'someone@anemailaddress.com', 'telemetry')
user.save()
# check to see if the user was actually created
users = UserModel.objects.all()
for user in users:
    print(user)
```
You should see both your ```superuser``` and your ```test1``` user.

### Run The Django Test/Development Server

The following runs the test/development server so that it is only accessible on this computer.
```bash
python3.8 manage.py runserver
```

To run the test/development server so that it is accessible from outside you computer so that it might be accessed from an iPhone or iPad running the Pythonista application, start the server this way:
```bash
python3.8 manage.py runserver 0.0.0.0:8000
```

### Access From Another Computer
The hosts's IP address is needed to access the server from another computer, phone or tablet.  After running the correct command for your operating system, you may have to pick through a list of network interfaces to find the correct one.  Use that address on the other computer.
* Windows
  ````PowerShell
  ipconfig
  ````
* Linux
  ````bash
  localhost -I
  ````
* Apple Mac
  ````bash
  ifconfig -a
  ````

If, for example, your server's IP address turned out to be ```192.168.1.51```, then the base URL for the web server will be ```http://192.168.1.51:8000/```.

## Compatible Python Clients

### Pythonista Client.
[https://apps.apple.com/us/app/pythonista-3/id1085978097](Pythonista 3) is an Apple IOS application that runs on iPhones and iPads.   The current Pythonista 3 implements Python 3.6 which works fine for this particular application.  The client repository is [https://github.com/thatlarrypearson/telemetry-pythonista](telemetry-pythonista)

#### Pythonista Companion Server Application
The server Django code module (application) supporting the Pythonista client is ```ios_sensor_pack``` which is included in this repository.
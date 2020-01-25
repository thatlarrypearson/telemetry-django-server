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

The following ```python3.8``` commands require the account issuing the commands have write permissions on the local copy of the repository.
* The ```telemetry-django-server/src/telemetry_django_server``` directory to allow the ```settings.py``` file to write the ```secret.py``` file.
* The ```telemetry-django-server/src/ios_sensor_pack``` where ```makemigrations``` will create a ```migrations``` directory containing instructions for required to create database tables.

The following commands must be run from the repository's ```telemetry-django-server/src``` directory where the ```manage.py``` file is foundtelemetry-django-server.

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

To run the test/development server so that it is accessible from outside you computer (e.g. from an iPhone or iPad running the Pythonista application or web browser), start the server this way:
```bash
python3.8 manage.py runserver 0.0.0.0:8000
```

### Web Browser Access

The **Telemetry Django Server** can be accessed via a web browser as shown below.
* Accessing from a web browser on the same machine as the server use [http://127.0.0.1:8000](http://127.0.0.1:8000)
* Using a web browser to access the server from another host, see the section below on **Access From Another Computer**.

![Home Page](docs/HomePage.png)

From the home page, there are two sections of interest - [Admin](http://127.0.0.1:8000/admin/) and [IOS Sensor Pack](http://127.0.0.1:8000/ios_sensor_pack/).

#### Admin

[Admin](http://127.0.0.1:8000/admin/) is an administrative interface for users like the superuser (see the **Create Superuser** section above).  Access to this area requires the superuser username and password.

![Admin Login Page](/docs/AdminLoginPage.png)

Once logged in, a superuser will see the following interface.

![Admin Landing Page](docs/AdminLandingPage.png)

The administrative landing page provides links:

* [Users](http://127.0.0.1:8000/admin/auth/user/) - User administration page where users can be added, be deleted, granted permissions, disabled and passwords reset.
* [IOS_SENSOR_PACK](http://127.0.0.1:8000/admin/ios_sensor_pack/) section where IOS sensor data can be created, destroyed, modified or browsed.

#### IOS Sensor Pack

Developers may want to explore the [IOS Sensor Pack](http://127.0.0.1:8000/ios_sensor_pack/) API's with their web browser.  The web browser will see a web browser version of the REST API's exposed by the web server.  When doing development work, browser access to the same REST API interface is extremely useful.

The web interface uses a different authentication mechanism than the REST API's used by the [telemetry-pythonista](https://github.com/thatlarrypearson/telemetry-pythonista) client program.  As a result, before accessing the [IOS Sensor Pack](http://127.0.0.1:8000/ios_sensor_pack/) pages, the web browser will need to [login](http://127.0.0.1:8000/accounts/login/) first.

The [Gravity API](http://127.0.0.1:8000/ios_sensor_pack/gravity/) is shown below.

![Gravity API](docs/GravityAPI.png)

### Access From Another Computer
The hosts's IP address is needed to access the server from another computer, phone or tablet.  After running the correct command for your operating system, you may have to pick through a list of network interfaces to find the correct one.  Use that address on the other computer.
* Windows 10
  ````PowerShell
  ipconfig
  ````
  In the following screen shot, look for the section ***Wireless LAN adapter Wi-Fi***.  Under that heading, see the line starting with ```IPV4 Address```.  In this case, the IPV4 address is ```192.168.1.51```.

  ![Windows 10 ```ipconfig```](docs/Windows10-ipconfig.png)
* Linux
  ````bash
  hostname -I
  ````
  ![Linux ```hostname -I```](docs/LinuxHostnameDashI.png)
* Apple Mac
  ````bash
  ifconfig -a
  ````

If, for example, your server's IP address turned out to be ```192.168.1.51```, then the base URL for the web server will be ```http://192.168.1.51:8000/```.

## ```ALLOWED_HOSTS```

Because the client software runs on a computer separate from the server machine, testing changes in the server code using ```python3.8 manage.py runserver 0.0.0.0:8000``` will require adding the host's IP address to ```ALLOWED_HOSTS``` in the ```settings.py``` file.

![```settings.py``` file ```ALLOWED_HOSTS``` Setting](docs/ALLOWED_HOSTS.png)

If you are developing on the same host machine as the web server, consider adding ```127.0.0.1``` to the ALLOWED_HOSTS as shown below.  This will enable a browswer or client on the web server machine to access the website locally.

```python
ALLOWED_HOSTS = ['192.168.1.51', '127.0.0.1', ]
```

## Compatible Python Clients

### Pythonista Client.
[Pythonista 3](https://apps.apple.com/us/app/pythonista-3/id1085978097) is an Apple IOS application that runs on iPhones and iPads.   The current Pythonista 3 implements Python 3.6 which works fine for this particular application.  The client repository is [telemetry-pythonista](https://github.com/thatlarrypearson/telemetry-pythonista).

#### Pythonista Companion Server Application
The server Django code module (application) supporting the Pythonista client is ```ios_sensor_pack``` which is included in this repository.

## ```ios_sensor_pack``` Evaluation

A survey of motion data analysis techniques indicated that motion data samples should ideally be made in the 40,000 Hz range.  In other words, the average time between samples should be around 2.5 * 10**(-5) or two point 5 times ten to the minus fifth power. 

Eyeballing the actual time between samples to be around 1 to 4 seconds which was too slow by more than four orders of magnitude.

The following code can be run on the server to provide average time between samples to see just how good or bad things are.
```bash
python3.8 manage.py shell
```
Run the following python inside the Django shell.
```python
from datetime import timedelta
from ios_sensor_pack.models import Location
locations = Location.objects.all().order_by('id')
old_ts = None
td_sum = timedelta(0, 0)
td_count = 0
for location in locations:
    if old_ts:
        td_sum = td_sum + (location.sat_timestamp - old_ts)
        td_count = td_count + 1
    old_ts = location.sat_timestamp

avg_time = td_sum / td_count
print(str(avg_time))
```
The results were ```0:00:03.206183```, roughly 3.2 seconds between each sample.  Not exactly promising.  Some of the performance issues are a result of running on the development evironment.  Will need to explore performance issues later.

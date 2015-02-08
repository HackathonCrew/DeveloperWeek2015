
Install instructions

* Vagrant
* Virtual Box
* Run command "vagrant plugin install vagrant-cachier" for repeat log speed boosts when reprovisioning
* SSH Onto Box
* sudo pip install -r /projects/DeveloperWeek2015/requirements.txt

To Run Website:

* SSH to Box
* cd /projects/DeveloperWeek2015
* python manage.py runserver 0.0.0.0:8000
* Go to http://192.168.33.11:8000/ on your browser

update pip:
sudo easy_install -U pip

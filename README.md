
# API-OFF

This small project aims to allow a user to find a healthy substitute to a food he will have selected
## Getting Started

### **Prerequisites**
Make sure you have at least [MySQL 5.7](https://www.digitalocean.com/community/tutorials/comment-installer-mysql-sur-ubuntu-18-04-fr) or higher and [python3.6.9](https://wiki.python.org/moin/BeginnersGuide/Download) or higher installed
### **Install or Upgrade**

##### first clone the repository:

```
git clone git@github.com:Bainard/activite5.git
```

##### Then activate a virtual environment:

```
python3 -m venv venv
source venv/bin/activate
pip3 -r requirements.txt
```

#####Next create the database
```
sudo python3 fill_bdd.py
```

###Usage


Launch main.py
```
python3 main.py
```
The user chooses a figure which corresponds to a food category (chocolate, baby potty, cereals ...).

The application will then query the OpenFoodFact API, and save the results in a database
The user can then choose the food with the highest nutriscore, which corresponds to the healthiest substitute.


This application uses a mariadb database, which can be seen in the following diagram


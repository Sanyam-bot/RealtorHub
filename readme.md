# RealtorHub
### Description: 
It is a Django desktop appliction using Electron framework, the user can keep track of the real state deals, by adding them on the add page, it includes general data which needs to remembered for a deal. It provides an another page which showcases deal, which was put in by the user

### Distinctiveness and Complexity
No other websites provides a way to just add real estate deals, even if they do they aren't personalized, and for complexity ,I used Django models, forms, which made the addition of new fields easier, also It's not just a Django web application, it's a desktop application made using Electron, and it has launh files for both windows and linux, .bat and .sh respectively

### Models.py
It includes two model classes, User class which extends the default 'AbstractUser', without adding any additional fields and Property class which has several fields to store information about the property, user, property_name, buyer_1, buyer_2, buyer_3, buyer_4, buyer_5, seller, dealer_1, dealer_2, state, city, address1, nearby, total_amount, rate, expenses, registry_date, sai, size, marla, and payment_condition, basically it stored all the information, the reason I choose the a single class is that a single user is going to use it, so I didn't matter to store the data efficiently, also having just one class made it easier to use

### Views.py
It consists of a basic authentication process, other then that it has function which generates a Django form for the User to fill, which is further stored in the database. The index function genreates a page which showcases all the real estate lisitngs in a table which the user stored, and it provides a link to every listing, which the user can further go into to see the all information about the lisiting, actually that link takes to another url, whose function is defined in the views.py. When on the property page the useer gets option to either edit the lisitng or delete it, both of which are handled by different functions in the views.py, which are edit(request, property_id) and property(request, property_id) respectively. The edit and delete both ask for confirmation using javascript.

### Forms.py
I made a PropertyForm which extends the forms.ModelForm, and in the class meta all the fields are defined, and in widgets format of the registry-date is kept default

### Index.js
I basically launches the Django we application as a desktop app using Electron on the localhost

### Realtor.bat, Realtor.sh
These are the launchers for both windows and linux respectively

### Design 
I used bootstrap for the navbar, whose files are stored locally, so It's accesible offline. The Add Page is divided into four sections, the sections are in a container which is given a shadow so it looks raised, also the color is off white, every section has a dashed border, and the text is aligned to the left. The property page has a basic design it just shows the the data stored in the database about that particular property listing.

### How to run the application
In order to run the application the user needs to have python, node, Django, and electron installed. After everything is installed the user should run python manage.py migrate, after that it's all set, by launching either of realtor.bat or realtor.sh based on the OS, it will run the application as a desktop app, If the user wants to just use it as a web application, there is no need to install node and electron, and the application will be able to start by runing python manage.py migrate and then python manage.py runserver.
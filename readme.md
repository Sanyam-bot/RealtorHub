# RealtorHub
### Description: 
It is a Django desktop application using Electron framework, It's general purpose is to store information about real estate deals, it is made keeping in mind that It can be used by the seller, buyer and the realtor, It basically stores Property name, type of the property, buyers, seller, dealer, Registry date, size, marla, state, city, address1, nearby, total amount, sai, rate, expenses, and payment condition.  

### Distinctiveness
The reason for it being distinct is that there is no website that I have seen which provides a way to store real estate properties for personal use, and most important one it's not just a Django application, it's desktop app made with Electron framework. If I go deep down to specific features which are distinct to CS50 web's other project, being able to select a date with a calendar for registry date, the templatetags folder provides a way to represent integer into comma-separated way according to Indian Numerical system, when the user tries to edit or delete the entry It asks for confirmation with the help of javscript, and when It comes distinctness in design the add container has a shadow, which makes it look raised, and it's same for the payment, address and payment condition. 


### Complexity
I used two Django models User and Property, the property model has all the fields about the property, specifically the "type" field in property field uses choices named PROPERTY_CHOICES, which are defined outside the property class. The property page allows to edit the listing, the edit page provides the same page as add, but the fields are already filled with the data of the listing, which it gets from the sqlite table, Now the user has the ability to chnage or add new information to the page and submit it, which will update the data in the sqlite table. Whenever the code searches for a possible row in a possible table, it makes sure the if the result doesn't exist, there is a error page explaining that, rather than the site just saying error. THe payment condition has a feature, so whenever the user clicks enter rather than saving the next line after a space, It saves it in the next line.


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
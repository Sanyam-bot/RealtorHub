# RealtorHub

### Description: 

It is a Django desktop application using Electron framework, It's general purpose is to store information about real estate deals, it is made keeping in mind that It can be used by the seller, buyer and the realtor, It basically stores Property name, type of the property, buyers, seller, dealer, Registry date, size, marla, state, city, address1, nearby, total amount, sai, rate, expenses, and payment condition.  

### Distinctiveness

The reason for it being distinct is that there is no website that I have seen which provides a way to store real estate properties for personal use. If I go deep down to specific features which are distinct to CS50 web's other project, being able to select a date with a calendar for registry date, the templatetags folder provides a way to represent integer into comma-separated way according to Indian Numerical system, when the user tries to edit or delete the entry It asks for confirmation with the help of javscript, and when It comes distinctness in design the add container has a shadow, which makes it look raised, and it's same for the payment, address and payment condition. 

It's not just a Django application, but also a Desktop application made with the help of Electron Framework, The reason for it also being a desktop app is that the fact I am planning to distribute this application one day after further development. It has both .bat, and .sh, that means It can work with both windows and linux, to make this possible I got to work with new technologies like node.js, npm, and electron. 

Within the templatetags, there is a folder which has a custom_filters.py file, it allows for the integers to be shown comma separated according to Indian decimal system.


### Complexity

#### Hardware Acceleration
Making a electron application for the first time served me with a lot errors, and also I made it for both Windows 11 and ubunutu, so the installion process is pretty different, which caused a trouble in managing dependencies. Nothing was more complex than understanding why I wasn't able to write in Django forms in the desktop app, when it was working fine as a website. The reason for this was my outdated GPU, which wasn't compatible withe Electron framework, so I disabled the hardware acceleration, which led to CPU taking over the graphics task, and solving this error.

#### Custom_filters.py
It shows the decimals comma-separated acc. to Indian decima system, firstly it converts the int into a string, then if the length of the string is less than or equal to 3, there will be no commas, but if it is more than 3, what it will do is separate the last three from the reamaining, and now it will iterate over the remaining and adding a comma after every two characters, and at last it will join the reamining and last three character with a comma in between.

#### add_property in views.py
When the user submits the add form to save the property listing, before simply adding the data into the SQLite database, it escapes the paytment condition field's '\n' to '<br>', so when the users clicks enter, the text afterwards starts from next line. Also, after that the form is saved without commiting because the user field is yet to be filed, the user would be the user who requested this to happen, and then finaaly the form is saved.

#### edit 
This feature allows to edit the property listing. The edit function first gets the property instance, then if the request was GET request,  it fills all the fields of the PropertyForm with the saved data. Now the user have form fields with pre filled data and a option to change anything, once it's submittted, the form is checked if it's valid or not, if it is saved to the database, otherwise the data will remain the same. ALso, when the user clicks on the edit button, it asks for the confirmation with the help of javascript. 

#### Search
This feature allows to search for the property listings, by searching for their property name. The search function iterates over Property instances, and then it iterates over the query searched by the user, then it checks if the characters of the query aren't equal to property_name's equivalent index, the loop will break, which would mean there aren't similar results to the query, but If the loop finishes without breaking, it will save the that property instance to a empty list.


### Models.py
It includes two model classes, User class which extends the default 'AbstractUser', without adding any additional fields and Property class which has several fields to store information about the property, user, property_name, buyer_1, buyer_2, buyer_3, buyer_4, buyer_5, seller, dealer_1, dealer_2, state, city, address1, nearby, total_amount, rate, expenses, registry_date, sai, size, marla, and payment_condition, basically it stored all the information, the reason I choose the a single class is that a single user is going to use it, so I didn't matter to store the data efficiently, also having just one class made it easier to use


### Views.py
It consists of a basic authentication process, other then that it has function which generates a Django form for the User to fill, which is further stored in the database. The index function genreates a page which showcases all the real estate lisitngs in a table which the user stored, and it provides a link to every listing, which the user can further go into to see the all information about the lisiting, actually that link takes to another url, whose function is defined in the views.py. When on the property page the useer gets option to either edit the lisitng or delete it, both of which are handled by different functions in the views.py, which are edit(request, property_id) and property(request, property_id) respectively. The edit and delete both ask for confirmation using javascript.

### Forms.py
I made a PropertyForm which extends the forms.ModelForm, and in the class meta all the fields are defined, and in widgets format of the registry-date is kept default

### Index.js
I basically launches the Django application as a desktop app using Electron on the localhost

### Realtor.bat, Realtor.sh
These are the launchers for both windows and linux respectively

### Design 
I used bootstrap for the navbar, whose files are stored locally, so It's accesible offline. The Add Page is divided into four sections, the sections are in a container which is given a shadow so it looks raised, also the color is off white, every section has a dashed border, and the text is aligned to the left. The property page has a basic design it just shows the the data stored in the database about that particular property listing.

### How to run the application
In order to run the application the user needs to have python, node, Django, and electron installed. After everything is installed the user should run python manage.py migrate, after that it's all set, by launching either of realtor.bat or realtor.sh based on the OS, it will run the application as a desktop app, If the user wants to just use it as a web application, there is no need to install node and electron, and the application will be able to start by runing python manage.py migrate and then python manage.py runserver.
# Project Description:

The Car Collector App is a comprehensive platform designed for automobile enthusiasts to manage their car collections efficiently. Built using Django Template Language, Django, Python, and PostgreSQL, this application allows users to catalog their vehicles, track fuel fillings, and manage modifications in a user-friendly interface.

===
# Key Features:
1. Car Management: 
Users can add details about their cars, including model, brand, and year of manufacture. Each car entry is stored in a dedicated database, allowing for easy retrieval and management.
2. Fuel Filling Log: 
Users can register their fuel filling dates along with the type of gas used. This feature helps track fuel consumption and maintain records for each vehicle.
3. Modifications Tracker: 
The app supports a many-to-many relationship for car modifications. Users can create a list of available modifications and assign them to specific cars in their collection, ensuring a detailed history of enhancements made.
4. User Authentication: 
Secure user authentication allows individuals to create accounts, log in, and manage their car collections safely.

===
# User Story
## Title: Car Collection
As a car enthusiast,
I want to be able to add my cars, track fuel fillings, and manage modifications,
so that I can keep detailed records of my collection and its maintenance.

===
## Acceptance Criteria:
1. Adding Cars:
- I can input the car's brand, model, and year of manufacture.
- I receive confirmation when a car is successfully added.
2. Tracking Fuel Fillings:
- I can log the date of each fuel filling and specify the type of gas used (e.g., regular, premium, diesel).
- I can view a history of my fuel fillings for each car.
3. Managing Modifications:
- I can create a list of modifications (e.g., new tires, paint job, engine upgrade).
- I can assign multiple modifications to each car and view which modifications have been applied.
4. User Authentication:
- I can create an account and log in securely.
My data is saved and accessible only to me.


===
# PseudoCode:
## Signing Up 
1. User provides username, email, and password.
2. Validate username and email format, and check password strength.
3. Create a new user account in the database.
4. Confirm account creation.

## Signing In
1. User provides username and password.
2. Check credentials against the database.
3. Create a session for the user.
4. Confirm login success.

## Adding a Vehicle
1. Check if the user is logged in.
2. Accept vehicle details: make, model, year, and VIN.
3. Save the vehicle to the database, linked to the user ID.
4. Confirm successful addition.

## Viewing Vehicles
1. Check if the user is logged in.
2. Retrieve all vehicles linked to the user ID from the database.
3. Display the list of vehicles.

## Recording a Fuel Fill
1. Check if the user is logged in.
2. Accept details: vehicle ID, date, amount, and price per gallon.
3. Calculate total cost and save the fuel fill record to the database.
4. Confirm successful recording.

## Viewing Fuel History
1. Check if the user is logged in.
2. Retrieve all fuel fill records linked to the specified vehicle ID.
3. Display the fuel fill history.

## Adding a Modification
1. Check if the user is logged in.
2. Accept modification details: vehicle ID, type, description, and date.
3. Save the modification to the database.
4. Confirm successful addition.

## Viewing Modifications
1. Check if the user is logged in.
2. Retrieve all modifications linked to the specified vehicle ID.
3. Display the modification history.

## Deleting a Vehicle
1. Check if the user is logged in.
2. Verify user ownership of the vehicle.
3. Remove the vehicle from the database.
4. Confirm deletion or return an error if unauthorized.

## Logging Out
1. Check if the user is logged in.
2. Clear the user session.
3. Confirm logout success.

===
# MocUp
1. <img src="/Public/Plan/imgs/MocUp/index.png" >
2. <img src="/Public/Plan/imgs/MocUp/SignUp.png" >
3. <img src="/Public/Plan/imgs/MocUp/SignIn.png" >
4. <img src="/Public/Plan/imgs/MocUp/Home.png" >
5. <img src="/Public/Plan/imgs/MocUp/AddCar.png" >
6. <img src="/Public/Plan/imgs/MocUp/Show.png" >
7. <img src="/Public/Plan/imgs/MocUp/Update.png" >
8. <img src="/Public/Plan/imgs/MocUp/Delete.png" >
9. <img src="/Public/Plan/imgs/MocUp/AddMod.png" >

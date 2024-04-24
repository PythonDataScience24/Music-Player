# Project for Programming for Data Science Course
---
# S-Wave

## About

Our program is called S-Wave and it aims to provide music playing platform that is fully under the control of the user. The user is able to upload their own *.mov* files and, therefore, create an own music library.  
The music library consists of not only the *.mov* file, but also the user will be able to add the name of the artist, the genre, year it was released and other classifications. Thus, the user will be able to then search their library by filtering it using the information they have provided during their creation of the library (i.e filter by genre, artist, etc.).  
Furthermore, our application does not only serve as a storage place, but also provides different actions that can be used through an intuitive and user friendly GUI. The user will be able to not only play the music, but also give their listening experience a personalized twist by being able to perform actions like amplifying the track and other features. Furthermore, the user will be able to visualize the soundwaves through a plot and thus, see their self-applied changes regarding their favorite music title.

## Roadmap

Some milestones that our project aims to reach are: 
* the creation of a user-friendly GUI
* the creation of an appropriate database
* create an appropriate data manipulation environment
* a visualisation environment for the song plots need to be established. 

To enable the user to have a pleasent experience with our application the GUI needs to be easily interpretable, thus, one task that our project needs to fulfill is the implementation of exactly this by using an appropriate library that is fitting for our goals. Saving the uploaded *.mov* files and organizing them needs a fitting database. This can be achieved by creating a pandas dataframe with all the information saved, which then needs to be connected to the according *.mov* file. Thus, the creation of this database is a key task that our project aims at. In return, an appropriate data manipulation environment that docks onto this database and works closely with it is elementary to the project. This can be achieved through using the libraries numpy, pandas, and others. Building on top of all these elements, the plotting environment of the songs needs to be sufficient for our goals previously described. This task can be solved through the usage of the matpltlib library and Seaborn, which supply the appropriate tools to generate the plots.

We aim to set up the database and data manipulation environment before the other implementations, as the others cannot be used without this core of the project. We aim to fulfill this task until the 02.05.2024.  
Then, we aim to create establish the plotting environment until the 09.05.2024.  
And lastly, we aim to implement an appropraite GUI until the 16.05.2024.

---

Group Project for University Bern by Christian Gafner[21-917-075], Julien Chopin[21-916-846], Alexander Mlekus [17-118-753], Massimiliano Vella [20-117-594]

# 🎼🎼🎼 Lyrics-App  🎼🎼🎼

A tool that allows analysis of the frequency of the appearance of words and the mention of places in the world on song lyrics
This project is part of Topics in Digital Humanities course in BGU.

**To run this projects follow the steps:**

1. clone the project- ```git clone https://github.com/shirmarko/Lyrics-App.git```.
2. install flask - ```pip install flask```
3. go into Lyrics-App/backend directory.
4. run the command :

   for mac - ```export FLASK_APP=backend.py```.
   
   for Windows CMD - ```set FLASK_APP=backend```.
   
   for Windows PowerShell: ```$env:FLASK_APP = "backend"```.

5. run the command - ```flask run```.
6. it may ask you to install some libraries (nltk, lyricsgenius, matplotlib...), install them.
   than run the command again.

now the server should run on:  http://127.0.0.1:5000/

7. go back to the main directory.
8. open Lyrics-App/frontend directory.
9. open *home.html* file

**That's it! Now you can analyze the best song of your best artist! Enjoy!**

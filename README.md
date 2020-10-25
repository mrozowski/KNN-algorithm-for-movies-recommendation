# KNN-algorithm-for-movies-recommendation
It's my another small project in Python and my next step on the path to become a machine learning engineer. It uses the K-nearest neighbors algorithm to find 5 similar movies and recommend it to the user. I added a simple GUI in the **PyQT** framework 


The program uses CSV file with 30 popular movies. This is how the data looks. 
![pic](/Screenshots/data.JPG?raw=true "Title")



On the list are shown all available movies. After choosing one title and clicking the "Show" button the **KNN algorithm** starts running.
![pic](/Screenshots/main.JPG?raw=true "Title")



It's a simple yet perfect algorithm for that purpose and small data sets. It checks the correlation (distance) between the chosen movie and other rows in the dataset. Then it sorts the list ascendingly and chooses 5 first elements. After that results are shown on the interface.
![pic](/Screenshots/main2.JPG?raw=true "Title")


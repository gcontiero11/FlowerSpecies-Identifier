# KNN Algorithm

<img src="https://media.licdn.com/dms/image/C5112AQFY4bX3Y7jcHA/article-cover_image-shrink_423_752/0/1565431496518?e=1693440000&v=beta&t=XTs5fa0JRRCUBbuQoC3Js0pyAu8yM0lrLzAQXdg543U">

- Using a database named iris.data.csv with the infos: sepal_length , sepal_width , petal_length , petal_width and specie name.
- When placing a new flower with unknown species in iris.data_2.csv, using the KNN Algorithm, the program calculates the "k" flower species closest to the unkown flower and deduces a specie for it.
- The distance is calculated with the euclidian distance: d = ((a1-a2)**2 + (b1-b2)**2 + (c1-c2)**2 + (d1 - d2) ** 2 ) ** (1/2)

# Summary
- **Class Species :**

  Here a class called "Species" is defined with attributes for the species name, sepal length, sepal width, petal length, and petal width.

- **def Open_file(file_name) :** 

  This function opens a file provided as a parameter, reads each line, and separates the data into a list of flowers. Each flower is represented by an instance of the Species class, filling its attributes with the corresponding values. In the end, the complete list of flowers is returned.

- **def position_biggest_number(arr) :** 

  This function receives a list of numbers as a parameter and returns the position of the largest number in the list.

- **def calculating_distance(flower, list, k) :** 

  This function receives an unknown flower, a list of known flowers, and a value k as parameters. It calculates the Euclidean distance between the unknown flower and each known flower in the list. The k closest species are stored in a list. If the species list is not full yet (less than k), the current species is added to the list. Otherwise, if the current distance is smaller than the largest distance in the list, the corresponding species is replaced by the current value, keeping the list updated.

- **def highest_frequency(arr) :** 

  This function receives a list of species as a parameter and counts the frequency of each species in the list. Then it determines which species has the highest frequency and returns its name.

- **def main() :** 

  This is the main function of the program. It initializes variables, opens the "iris.data.csv" file to obtain the known flowers, prompts the user for the value of k and the name of a file for the unknown flowers. Then, for each unknown flower, it calculates the closest species using the "calculating_distance" function, determines the species based on the frequency of the closest species using the "bigger_frequency" function, and prints the result on the screen.


class Species:
    name = ""
    sepal_length = 0
    sepal_width = 0
    petal_length = 0
    petal_width = 0


def Open_file(file_name):
    # Open the file and return a list of flowers with the data separated into classes
    flowers = []
    arq = open(f"{file_name}" , "r")
    for line in arq:
        data = line.strip().split(",")
        species = Species()
        species.sepal_length = float(data[0])
        species.sepal_width = float(data[1])
        species.petal_length = float(data[2])
        species.petal_width = float(data[3])
        species.name = data[4]
        flowers.append(species)
    arq.close()
    return flowers


def position_biggest_number(arr):
    # Returns the position of the largest number in a list
    biggest_number = arr[0]
    position = 0
    for i in range(len(arr)):
        if arr[i] > biggest_number:
            biggest_number = arr[i]
            position = i
    return position


def calculating_distance(Unkown_flower,list,k):
    # Calculate the closest species for a given unknown flower
    closest_species = []
    species = []
    sepal_l1 = Unkown_flower.sepal_length
    sepal_w1 = Unkown_flower.sepal_width
    petal_l1 = Unkown_flower.petal_length
    petal_w1 = Unkown_flower.petal_width
    distance = 0
    for elem in list:
        sepal_l2 = elem.sepal_length
        sepal_w2 = elem.sepal_width
        petal_l2 = elem.petal_length
        petal_w2 = elem.petal_width
        distance = ((sepal_l1 - sepal_l2)**2 + (sepal_w1 - sepal_w2)**2 + (petal_l1 - petal_l2)**2 + (petal_w1 - petal_w2)**2) ** (1/2)
        if len(species) < k:
            species.append(elem.name)
            closest_species.append(distance)
        elif len(species) == k:
            position = position_biggest_number(closest_species)
            biggest_value = closest_species[position]
            if distance < biggest_value:
                closest_species[position] = distance
                species[position] = elem.name
    return species  


def highest_frequency(arr):
    # Determine the most frequent species in a list of species
    setosa_count = 0
    versicolor_count = 0
    virginica_count = 0
    for elem in arr:
        if elem == 'setosa':
            setosa_count += 1
        elif elem == 'versicolor':
            versicolor_count += 1
        elif elem == 'virginica':
            virginica_count += 1
    if setosa_count > versicolor_count and setosa_count > virginica_count:
        return "setosa"
    elif versicolor_count > setosa_count and versicolor_count > virginica_count:
        return "versicolor"
    else:
        return "virginica"


def main():
    # Main function of the program
    species = []
    flowers = Open_file("iris.data.csv")
    k = int(input("K value: "))
    file_name = input("Type the document name:")
    Unknown_species = Open_file(file_name)
    i = 0
    for Unkown_flower in Unknown_species:
        i += 1
        species = calculating_distance(Unkown_flower,flowers,k)
        Unkown_flower.name = highest_frequency(species)
        print(f"flower {i} : {Unkown_flower.name}")

main()

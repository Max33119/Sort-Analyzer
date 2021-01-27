# Sort Analyzer by Mr. V

# import time
import time

def main():
    # Load data files into variables
    randomData = loadDataArray("data-files/random-values.txt")
    reversedData = loadDataArray("data-files/reversed-values.txt")
    fewUniqueData = loadDataArray("data-files/few-unique-values.txt")
    nearlySortedData = loadDataArray("data-files/nearly-sorted-values.txt")


    # Test file load
    print(randomData[0:15])
    print(reversedData[0:15])
    print(fewUniqueData[0:15])
    print(nearlySortedData[0:15])

    # Main Menu
    loop = True
    while loop:
        # Print main menu and get user selection
        selection = mainMenu()

        # Process selection
        if (selection == "1"):
            
            # bubble random
            print("\nBubble Sort Random Data")
            randomData = loadDataArray("data-files/random-values.txt")

            startTime = time.time()
            bubbleSort(randomData)
            endTime = time.time()
            
            print("it took " + str(endTime - startTime) + " seconds to sort")

           

        elif (selection == "2"):

            #bubble reversed
            print("\nBubble Sort Reversed Data")
            reversedData = loadDataArray("data-files/reversed-values.txt")

            startTime = time.time()
            bubbleSort(reversedData)
            endTime = time.time()
            
            print("it took " + str(endTime - startTime) + " seconds to sort")

            
        elif (selection == "3"):

            #bubble few unique
            print("\nBubble Sort Few Unique Data")
            fewUniqueData = loadDataArray("data-files/few-unique-values.txt")

            startTime = time.time()
            bubbleSort(fewUniqueData)
            endTime = time.time()
            
            print("it took " + str(endTime - startTime) + " seconds to sort")

            

        elif (selection == "4"):

            #bubble nearly
            print("\nBubble Sort Nearly Sorted Data")
            nearlySortedData = loadDataArray("data-files/nearly-sorted-values.txt")
            
            startTime = time.time()
            bubbleSort(nearlySortedData)
            endTime = time.time()
            
            print("it took " + str(endTime - startTime) + " seconds to sort")

            

        elif (selection == "5"):

            #selection random
            print("\nSelection Sort Random Data")
            randomData = loadDataArray("data-files/random-values.txt")

            startTime = time.time()
            selectSort(randomData)
            endTime = time.time()
            
            print("it took " + str(endTime - startTime) + " seconds to sort")

            

        elif (selection == "6"):

            #selection reversed
            print("\nSelection Sort Reversed Data")
            reversedData = loadDataArray("data-files/reversed-values.txt")

            startTime = time.time()
            selectSort(reversedData)
            endTime = time.time()
            
            print("it took " + str(endTime - startTime) + " seconds to sort")

            
        elif (selection == "7"):

            #selection few unqiue
            print("\nSelection Sort Few Unique Data")
            fewUniqueData = loadDataArray("data-files/few-unique-values.txt")

            startTime = time.time()
            selectSort(fewUniqueData)
            endTime = time.time()
            
            print("it took " + str(endTime - startTime) + " seconds to sort")

            
        elif (selection == "8"):

            #selection nearly
            print("\nSelection Sort Nearly Sorted Data")
            nearlySortedData = loadDataArray("data-files/nearly-sorted-values.txt")

            startTime = time.time()
            selectSort(nearlySortedData)
            endTime = time.time()
            
            print("it took " + str(endTime - startTime) + " seconds to sort")

            
        elif (selection == "9"):

            #insetion random
            print("\nInsertion Sort Random Data")
            randomData = loadDataArray("data-files/random-values.txt")

            startTime = time.time()
            insertionSort(randomData)
            endTime = time.time()
            
            print("it took " + str(endTime - startTime) + " seconds to sort")

           
        elif (selection == "10"):

            #insertion reversed
            print("\nInsertion Sort Reversed Data")
            reversedData = loadDataArray("data-files/reversed-values.txt")

            startTime = time.time()
            insertionSort(reversedData)
            endTime = time.time()
            
            print("it took " + str(endTime - startTime) + " seconds to sort")

            
        elif (selection == "11"):

            #insertion few unqiue
            print("\nInsertion Sort Few Unique Data")
            fewUniqueData = loadDataArray("data-files/few-unique-values.txt")

            startTime = time.time()
            insertionSort(fewUniqueData)
            endTime = time.time()
            
            print("it took " + str(endTime - startTime) + " seconds to sort")

            
        elif (selection == "12"):

            #insertion nearly sorted
            print("\nInsertion Sort Nearly Sorted Data")
            nearlySortedData = loadDataArray("data-files/nearly-sorted-values.txt")

            startTime = time.time()
            insertionSort(nearlySortedData)
            endTime = time.time()
            
            print("it took " + str(endTime - startTime) + " seconds to sort")

            
        elif (selection == "13"):
            loop = False
    # end while loop
    print("goodbye")
# end main()


def loadDataArray(fileName):
    # Return data from file as an array of integers.
    temp = []

    # Read file line by line
    fileref = open(fileName, "r")
    for line in fileref:
        line = line.strip()  # Clean up line
        temp.append(int(line))  # Add integer to temp list

    fileref.close()

    return temp
# end loadDataArray()


def mainMenu():
    # Print Main Menu
    print("\nMain Menu")
    print("1: Bubble Sort Random Data")
    print("2: Bubble Sort Reversed Data")
    print("3: Bubble Sort Few Unique Data")
    print("4: Bubble Sort Nearly Sorted Data")
    print("5: Selection Sort Random Data")
    print("6: Selection Sort Reversed Data")
    print("7: Selection Sort Few Unique Data")
    print("8: Selection Sort Nearly Sorted Data")
    print("9: Insertion Sort Random Data")
    print("10: Insertion Sort Reversed Data")
    print("11: Insertion Sort Few Unique Data")
    print("12: Insertion Sort Nearly Sorted Data")
    print("13: Exit")
    return input("Enter menu selection (1-13): ")
# end mainMenu()



#bubble sort--------------------------------------------------------------------------------------------------------

def bubbleSort(aList):
    
    for num_compare in range(len(aList) - 1, 0, -1):
        for i in range(num_compare):
            if aList[i] > aList[i+1]:
                placeholder = aList[i]
                aList[i] = aList[i+1]
                aList[i+1] = placeholder

#select sort----------------------------------------------------------------------------------------------------------

def selectSort(aList):
    for position in range(len(aList)):
        min_position = position
        for i in range(position + 1, len(aList)):
            if aList[i] < aList[min_position]:
                min_position = i


        min_value = aList[min_position]
        aList[min_position] = aList[position]  
        aList[position] = min_value


#insertion sort--------------------------------------------------------------------------------------------------------------------------

def insertionSort(aList):
    for i in range(1, len(aList)):
        insert_value = aList[i]
        insert_position = i

        while insert_position > 0 and aList[insert_position - 1] > insert_value:
            aList[insert_position] = aList[insert_position - 1]
            insert_position += - 1

        aList[insert_position] = insert_value



# Call main() to begin program
main()
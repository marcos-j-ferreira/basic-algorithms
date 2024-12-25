import time

def array():

    text = "-- Chose a option --\n 1 - add an element to the array\n 2 - Remove an element from the array\n 3 - to go out\n"

    arr = []

    try:
        option = 1
        while option < 3:
            option = int(input(text))

            if option == 1:

                values = int(input("Enter a elemets for add in array: --  "))
                arr.append(values)

                print(f"\nitem  add: {arr}\n")

            elif option == 2:
                arr.pop()
                print(f"last element successfully removed: {arr}")
            else:
                print("enter a valid value")

    except Exception as e:
        print(f"Error loading: {e}")
    finally:

        for i in range(10):
            print(f"Closing in {i}/10", end="\r")
            time.sleep(1)
array()

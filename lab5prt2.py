try:
    my_list = [1, 2, 3]
    index = int(input("Enter an index: "))
    value = my_list[index]
except IndexError:
    print("Error: Index out of range.")
except ValueError:
    print("Error: Please enter a valid index.")
finally:
    print("Execution completed.")

# You can raise a custom exception if needed
if index >= len(my_list) or index < 0:
    raise Exception("Invalid index.")

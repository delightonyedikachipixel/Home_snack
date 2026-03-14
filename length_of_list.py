
import random
def Random_numbers():

    numbers = [random.randint(1, 50) for numbers in range(10)] 

    return numbers


def length_of_list(numbers):

    count = 0
    for number in numbers:
        count += 1

    return count




def even_sum(numbers):

    sum_of_even = 0
    counter = 1

    for value in numbers:
        if (counter % 2 == 0):
            sum_of_even += value
        counter += 1

    return sum_of_even

def odd_sum(numbers):

    sum_of_odd = 0
    counter = 1

    for value in numbers:
        if (counter % 2 != 0):
            sum_of_odd += value
        counter += 1

    return sum_of_odd




def multiply_elements_at_third_position(numbers):

    product = 1
    counter = 1

    for value in numbers:
        if counter % 3 == 0:
            product *= value
        counter +=1

    return product



def average_of_numbers(numbers):

    total = 0

    for value in numbers:
        total += value
    average = total / length_of_list(numbers)

    return average



def get_largest_number(numbers):

    largest_number = numbers[0]
    for number in numbers:

        if number > largest_number:
            largest_number = number
    return largest_number


def get_smallest_number(numbers):

    smallest_number = numbers[0]
    for number in numbers:

        if number < smallest_number:
            smallest_number = number
    return smallest_number



def get_length_of_word(words):

    new_list = []
    for word in words:
        if len(word)>=2 and word.lower()[0] == word.lower()[len(word)-1]:
            new_list.append(word)
    return len(words), new_list
    





def get_range_of_numbers():

    numbers = list(range(1,16))
    print(numbers)

    return numbers
get_range_of_numbers()

def get_sum_of_third_place_numbers():

    numbers = [1,2,3,4,5,6,7,8,9,10]

    sum_of_third_place = 0
    counter = 1

    for value in numbers:
        if counter % 3 == 0:
            sum_of_third_place += value
        counter +=1
    

    return sum_of_third_place



def get_sum_of_first_middle_last_place_numbers():

    numbers = [1,2,3,4,5,6,7,8,9,10]

    first_number = numbers[0]
    last_number = numbers[len(numbers)-1]

    counter = len(numbers)
    sum_of_third_place_numbers = 0

    if counter % 2 == 1:
        middle_number = numbers[counter//2]
        sum_of_third_place_numbers += middle_number
    else:            
        middle_number = (numbers[counter//2 - 1] + numbers[counter//2]) / 2
        sum_of_third_place_numbers += middle_number

    

    return first_number + sum_of_third_place_numbers + last_number

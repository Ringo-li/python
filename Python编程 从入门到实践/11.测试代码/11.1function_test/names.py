from my_function import get_formatted_name

print("Enter 'q' at any time to quit")

while True:
    first = input("Please give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break
    middle = input("Please give me a fdsmiddle name if you have: ")
    if middle == 'q':
        break
    formatted_name = get_formatted_name(first ,last, middle)
    print("Neatly formatted name: " + formatted_name + '.') 
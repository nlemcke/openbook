def whats_your_name():
    name = input("What's your name? ")
    new_name = ''
    count = 0
    for letter in name:
        count += 1
        new_name += count * letter
    print("Hi", new_name)

if __name__ == '__main__':
    whats_your_name()

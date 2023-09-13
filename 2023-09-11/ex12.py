from vin_utils import reverse, reverse_by_words


def main():
    text = input('Enter some text: ')

    print(reverse(text))
    print(reverse_by_words(text))
    

if __name__ == '__main__': main()

import json
import time


def main():
    filename = input('Enter the CSV filename: ')
    if not filename.endswith('.csv'):
        print('The filename must have a `.csv` extension')
        return

    try:
        with open(filename, encoding='utf-8') as file:
            keys = file.readline().strip().split(',')

            # data = []
            # for line in file.readlines():
            #     values = line.strip().split(',')
            #     d = dict(zip(keys, values))
            #     data.append(d)

            data = [
                dict(zip(keys, line.strip().split(',')))
                for line in file.readlines()
            ]

        out_filename = f'{filename[:-4]}.{time.time()}.json'
        with open(out_filename, mode='wt', encoding='utf-8') as file:
            json.dump(data, file, indent=3)
            print(f'JSON data saved to file `{out_filename}`')

    except FileNotFoundError:
        print(f'The file "{filename}" does not exist')


if __name__ == '__main__':
    main()

# TODO импортировать необходимые молули
import csv, json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task(input_filename_path, output_filename_path,
         delimiter=',', new_line='\n') -> None:
    # TODO считать содержимое csv файла
    with open(input_filename_path, 'r', newline=new_line) as file:
        d = list(csv.DictReader(file, delimiter=delimiter))

    # TODO Сериализовать в файл с отступами равными 4
    with open(output_filename_path, 'w') as f:
        json.dump(d, f, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task(INPUT_FILENAME, OUTPUT_FILENAME)
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")

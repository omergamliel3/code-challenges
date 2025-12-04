'''
Camel to Snake
Given a string in camel case, return the snake case version of the string using the following rules:

The input string will contain only letters (A-Z and a-z) and will always start with a lowercase letter.
Every uppercase letter in the camel case string starts a new word.
Convert all letters to lowercase.
Separate words with an underscore (_).
'''


def to_snake_case(camel_str: str) -> str:
    snake_case_str = ''

    for char in camel_str:
        if char.isupper():
            snake_case_str += '_'

        snake_case_str += char.lower()

    return snake_case_str


def main():
    print(to_snake_case('helloWorld'))
    print(to_snake_case('longFunctionName'))
    print(to_snake_case('myNameIsOmerGamliel'))
    print(to_snake_case('omer'))


if __name__ == "__main__":
    main()

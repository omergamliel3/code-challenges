"""
Markdown Ordered List Item Converter

Given a string representing an ordered list item in Markdown, return the equivalent HTML string.

A valid ordered list item in Markdown must:

Start with zero or more spaces, followed by
A number (1 or greater) and a period (.), followed by
At least one space, and then
The list item text.
If the string doesn't have the exact format above, return "Invalid format". Otherwise, wrap the list item text in li tags and return the string.

For example, given "1. My item", return "<li>My item</li>"
"""""


def convert_list_item(markdown_string: str) -> str:
    INVALID_FORMAT_MSG = "Invalid format"

    if not isinstance(markdown_string, str):
        return INVALID_FORMAT_MSG

    line = markdown_string.strip()
    if "." not in line:
        return INVALID_FORMAT_MSG

    number_part, _, text_part = line.partition(".")

    if not (number_part.isdigit() and int(number_part) > 0):
        return INVALID_FORMAT_MSG

    if not text_part.startswith(" "):
        return INVALID_FORMAT_MSG

    list_item_text = text_part.strip()
    if not list_item_text:
        return INVALID_FORMAT_MSG

    return f"<li>{list_item_text}</li>"


def main():
    inputs = ["1. My item", " 1.  Another item", "1 . invalid item",
              "2. list item text", ". invalid again", "A. last invalid", 123, "3", "", " ", "1.invalid item"]
    for input in inputs:
        print(convert_list_item(input))


if __name__ == "__main__":
    main()

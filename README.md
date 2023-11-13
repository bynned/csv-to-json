# CSV to JSON Converter for Book Data

This Python script provides a simple and efficient way to convert a CSV file containing book data into a JSON format.

## Script Overview

The script reads a CSV file where each row represents a book. The book's name and author are separated by a semicolon (`;`). It then converts this data into a JSON structure, assigning each book an incremental ID starting from 1.

## Usage

1. **Input CSV File**: The input CSV file should be named `kirjat.csv` (or you can modify the `csvfile` variable in the script to match your file's name). Each line in this file should follow the format: `BookName;Author`.

2. **Output JSON File**: The output will be saved in a file named `kirjat.json`. This file will contain the book data in a JSON format, encoded in UTF-8 to support special characters.

## Functionality

- **`csv_to_json(csvfile)` Function**:
  - **Parameters**: Accepts a single parameter `csvfile` which is the path to the CSV file.
  - **Return Value**: Returns a dictionary where the key is `'books'` and the value is a list of book records. Each record is a dictionary containing `id`, `name`, and `author`.

- **Reading CSV File**:
  - Opens the CSV file in read mode with UTF-8 encoding.
  - Reads each line, splits the line into book name and author using `;` as the delimiter.

- **JSON Conversion**:
  - Converts the list of books into JSON format.
  - Uses `ensure_ascii=False` to correctly handle special characters like 'ä'.

- **Saving to JSON File**:
  - The JSON data is written to `kirjat.json` with an indentation of 4 for readability.
  - Ensures UTF-8 encoding for the output file to support special characters.

## Example

Given a CSV file with the following content:

```
Twilight;Stephenie Meyer
Harry Potter and the Philosopher's Stone;J.K. Rowling
```

The output JSON file will be:

```
{
    "books": [
        {
            "id": 1,
            "name": "Twilight",
            "author": "Stephenie Meyer"
        },
        {
            "id": 2,
            "name": "Harry Potter and the Philosopher's Stone",
            "author": "J.K. Rowling"
        }
    ]
}
```

## Notes

- Ensure the CSV file follows the expected format for correct processing.
- The script can be modified to accommodate different CSV formats or JSON structures.
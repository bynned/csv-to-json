import json

csvfile = 'kirjat.csv' 

def csv_to_json(csvfile):
    books = [] # Why books? because i have a huge list of my books in csv i need to convert to json
    with open(csvfile, 'r', encoding='utf-8') as file:
        for idx, line in enumerate(file, start=1):
            # In my csv, what seperates the book name and author is ';'
            name, author = line.strip().split(';')
            books.append({'id': idx, 'name': name, 'author': author})

    return {'books': books}

json_data = csv_to_json(csvfile)

# Save json data to file
with open ('kirjat.json', 'w', encoding='utf-8') as json_file:
    json.dump(json_data, json_file, indent=4, ensure_ascii=False)
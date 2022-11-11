import csv


def create_txt(name="data"):
    with open("database.csv", newline="", encoding="utf-8") as csvfile:
        txt = ""
        reader = csv.DictReader(csvfile)
        page = open(f"export/{name}.txt", "w", encoding="utf-8")
        for row in reader:
            txt += f'Фамилия: {row["Фамилия"]}\n'
            txt += f'Имя: {row["Имя"]}\n'
            txt += f'Телефон: {row["Телефон"]}\n'
            txt += f'Описание: {row["Описание"]}\n\n'
        page.write(txt)

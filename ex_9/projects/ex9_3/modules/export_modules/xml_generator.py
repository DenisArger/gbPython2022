import csv


def create_xml(name="data"):
    xml = "<xml>\n"
    with open("database.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            xml += f'<Фамилия>{row["Фамилия"]}</Фамилия>\n'
            xml += f'<Имя>{row["Имя"]}</Имя>\n'
            xml += f'<Телефон>{row["Телефон"]}</Телефон>\n'
            xml += f'<Описание>{row["Описание"]}</Описание>\n'
    xml += "</xml>"
    with open(f"export/{name}.xml", "w", encoding="utf-8") as page:
        page.write(xml)

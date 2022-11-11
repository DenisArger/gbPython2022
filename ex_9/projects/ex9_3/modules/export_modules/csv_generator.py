def create_csv(filename="data"):
    with open("database.csv", "rb", encoding="utf-8") as data:
        with open(f"export/{filename}.csv", "wb", encoding="utf-8") as new_file:
            new_file.writelines(data.readlines())

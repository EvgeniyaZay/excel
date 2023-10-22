import csv
import requests
import re
import os



regex = r"([^\.]*)\.?\s*обл\..*(г|п|пгт)\.([^\s\.,]{4,})"
with open('work1.csv', mode='r') as infile:
    reader = csv.reader(infile, delimiter=',')
    if os.path.exists("work_new.csv"):
        os.remove("work_new.csv")
    with open('work_new.csv', mode='x') as outfile:
        writer = csv.writer(outfile)
        mydata = [{"index": rows[0], "city": rows[1], "street": rows[2], "home": rows[3]} for rows in reader]
        # здесь у нас ограничено первой сотней
        for number, row in enumerate(mydata[:2731]):
            matches = re.finditer(regex, row["city"], re.MULTILINE)
            city = ''
            for matchNum, match in enumerate(matches, start=1):
                city = match.group(3)
            json_data = {"query": f'{city}, {row["street"].split(".")[-1]}, {row["home"].split(".")[-1]}',"limit":5,"fromBound":"CITY"}
            resp = requests.post('https://www.pochta.ru/suggestions/v2/suggestion.find-addresses', json=json_data)
            data = resp.json()
            index = ''
            if data:
                if 'postalCode' in data[0]:
                    index = data[0]['postalCode']
                else:
                    print(json_data)
                    # print(data[0])
            row["index"] = index
            print(number)
            writer.writerow(list(row.values()))
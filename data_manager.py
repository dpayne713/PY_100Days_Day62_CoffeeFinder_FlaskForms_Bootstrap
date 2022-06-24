import csv

class CSVData():
    def __init__(self):
        self.data = None

    def get_data(self):
        try:
            with open("cafe-data.csv", 'r') as csv_data:
                return list(csv.DictReader(csv_data))
        except Exception as x:
            print(x.args)
            return []


    def add_data(self, form):

        form_data = {
            "Cafe Name": form.cafe_name.data,
            "Location": form.location_url.data,
            "Open": form.open.data,
            "Close": form.close.data,
            "Coffee": form.coffee.data,
            "Wifi": form.wifi.data,
            "Power": form.power.data,
        }
        with open('cafe-data.csv', 'a') as csv_data:
            writer = csv.DictWriter(csv_data, fieldnames=list(form_data.keys()))
            writer.writerow(form_data)




import json


class JSON:
    def __init__(self, filepath):
        self.filepath = filepath
        self.jdict = {}

        try:
            with open(self.filepath, "r") as file:
                string = file.read()
                self.jdict = json.loads(string)

        except FileNotFoundError:
            raise FileNotFoundError(f"The file '{filepath}' could not be found.")

    def update_json(self):
        with open(self.filepath, 'w') as f:
            json.dump(self.jdict, f, indent=4)

    def add_field(self, key):
        self.jdict[key] = None
        self.update_json()

    def add_value(self, key, value):
        self.jdict[key] = value
        self.update_json()

    def remove_field(self, key):
        if key in self.jdict:
            del self.jdict[key]
            self.update_json()


filepath = "C:\\Users\\matthew.kuilan\\Downloads\\student.json"
instance = JSON(filepath)
instance.add_field('age')
print(instance.jdict)

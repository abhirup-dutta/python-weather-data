import json

class FileReaderWriter:

    def readFile(self, fileName):
        with open(fileName, 'r') as file:
            return json.load(file)

    def writeToFile(self, fileName, string_data):
        with open(fileName, 'w') as file:
            file.write(string_data)




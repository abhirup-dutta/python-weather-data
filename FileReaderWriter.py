import json


class FileReaderWriter:

    def readObjectFromFile(self, file_name):
        with open(file_name, 'r') as file_pointer:
            return json.load(file_pointer)

    def readStringFromFile(self, file_name):
        with open(file_name, 'r') as file_pointer:
            return file_pointer.read()

    def writeObjectToFile(self, file_name, object_data, indent):
        with open(file_name, 'w') as file_pointer:
            json.dump(object_data, file_pointer, indent=indent)


    def writeStringToFile(self, file_name, string_data):
        with open(file_name, 'w') as file_pointer:
            file_pointer.write(string_data)




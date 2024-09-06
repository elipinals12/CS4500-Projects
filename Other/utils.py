import json

class Utils(object):
    @classmethod
    def extract_json_objects(self,data):
        """Extract JSON objects from a concatenated string."""
        objects = []
        pos = 0
        while pos < len(data):
            try:
                obj, pos = json.JSONDecoder().raw_decode(data, pos)
                objects.append(obj)
                # Skip any whitespace or extra characters between objects
                while pos < len(data) and data[pos].isspace():
                    pos += 1
            except json.JSONDecodeError:
                print("error")
                break
        return objects
import json
import xml.etree.ElementTree as e_tree


class JSONDATAExtractor:
    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode="r", encoding="utf-8") as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        """
        This function extracts data from json file
        :return: data
        """
        return self.data


class XMLDATAExtractor:
    def __init__(self, filepath):
        self.tree = e_tree.parse(filepath)

    @property
    def parsed_data(self):
        """
        This function extracts data from xml file
        :return: data
        """
        return self.tree


def dataextraction_factory(filepath):
    """
    This function extracts data from json and xml files
    :param filepath: path to file
    :return: data
    """
    if filepath.endswith("json"):
        extractor = JSONDATAExtractor
    elif filepath.endswith("xml"):
        extractor = XMLDATAExtractor
    else:
        raise ValueError(f"Cannot extract data from {filepath}")
    return extractor(filepath)


def extract_data_from(filepath):
    """
    This function is wrapper of dataextraction_factory. It adds exception handling.
    :param filepath: path to file
    :return: data
    """
    factory_obj = None
    try:
        factory_obj = dataextraction_factory(filepath)
    except ValueError as e:
        print(e)
    return factory_obj


def main():
    sqlite_factory = extract_data_from("data/person.sq3")
    print()
    json_factory = extract_data_from("data/movies.json")
    json_data = json_factory.parsed_data
    print(f"Found: {len(json_data)} movies")

    for movie in json_data:
        print(f"Title: {movie.get('title', '')}")
        year = movie.get('year', '')
        if year:
            print(f"Year: {year}")
        director = movie.get('director', '')
        if director:
            print(f"Director: {director}")
        genre = movie.get('genre', '')
        if genre:
            print(f"Genre: {genre}")
        print()

    xml_factory = extract_data_from("data/person.xml")
    xml_data = xml_factory.parsed_data
    liars = xml_data.findall(f".//person[lastName='Liar']")
    print(f"found: {len(liars)} persons")
    for liar in liars:
        firstname = liar.find('firstName').text
        print(f"first name: {firstname}")
        lastname = liar.find('lastName').text
        print(f"last name: {lastname}")
        [print(f"phone number ({p.attrib['type']}):", p.text) for p in liar.find('phoneNumbers')]
        print()


if __name__ == "__main__":
    main()


import json
import xml.etree.ElementTree as e_tree

"""
The Factory Pattern
    Use cases:
    If you realize that you cannot track the objects created by your application because the code
    that creates them is in many different places instead of in a single function/method, you
    should consider using the factory method pattern. The factory method centralizes object
    creation and tracking your objects becomes much easier. Note that it is absolutely fine to
    create more than one factory method, and this is how it is typically done in practice. Each
    factory method logically groups the creation of objects that have similarities. For example,
    one factory method might be responsible for connecting you to different databases
    (MySQL, SQLite), another factory method might be responsible for creating the geometrical
    object that you request (circle, triangle), and so on.

    The factory method is also useful when you want to decouple object creation from object
    usage. We are not coupled/bound to a specific class when creating an object; we just
    provide partial information about what we want by calling a function. This means that
    introducing changes to the function is easy and does not require any changes to the code
    that uses it.
"""


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

#!/usr/bin/env python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    try:
        root = ET.Element("data")

        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=False)
    except (TypeError, OSError):
        return None


def deserialize_from_xml(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        result = {}

        for child in root:
            result[child.tag] = child.text

        return result
    except (ET.ParseError, FileNotFoundError, OSError):
        return None

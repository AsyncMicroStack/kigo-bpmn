import xmltodict
import codecs
import json

def load_xml2dict(pathtoxmlfile: str, decode='utf-8'):
    with open(pathtoxmlfile, mode='rb') as f:
        body = f.read()
        body = codecs.decode(body, decode)
        xml = xmltodict.parse(body)
    return xml


def load_xml2json(pathtoxmlfile: str, decode='utf-8', escape_namespace=False, error='ignore'):
    """
    error = ignore | strict
    :param pathtoxmlfile:
    :param decode:
    :param escape_namespace:
    :param error:
    :return:
    """
    with open(pathtoxmlfile, mode='rb') as f:
        body = f.read()
        body = codecs.decode(body, decode, error)
        if escape_namespace:
            xml = xmltodict.parse(body, postprocessor=escape_ns)
        else:
            xml = xmltodict.parse(body)
    return json.dumps(xml)


def escape_ns(path, key, value):
    if key.startswith('@'):
        new_key = key
    elif ':' in key:
        new_key = key.split(':')[1]
    else:
        new_key = key
    return new_key, value
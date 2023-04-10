import xml.dom.minidom as xml


def get_objects_by_xml(filename):
    try:
        objects = xml.parse(filename).documentElement.getElementsByTagName('real_estate')
    except:
        return []

    result = []

    for object in objects:
        object_to_add = RealEstate()

        try:
            object_to_add.county = object.getElementsByTagName('county')[0].childNodes[0].nodeValue
        except:
            pass
        try:
            object_to_add.district = object.getElementsByTagName('district')[0].childNodes[0].nodeValue
        except:
            pass
        try:
            object_to_add.address = object.getElementsByTagName('address')[0].childNodes[0].nodeValue
        except:
            pass
        try:
            object_to_add.type = object.getElementsByTagName('type')[0].childNodes[0].nodeValue
        except:
            pass
        try:
            object_to_add.description = object.getElementsByTagName('description')[0].childNodes[0].nodeValue
        except:
            pass
        try:
            object_to_add.state = object.getElementsByTagName('state')[0].childNodes[0].nodeValue
        except:
            pass
        try:
            object_to_add.owner_first_name = object.getElementsByTagName('owner_first_name')[0].childNodes[0].nodeValue
        except:
            pass
        try:
            object_to_add.owner_last_name = object.getElementsByTagName('owner_last_name')[0].childNodes[0].nodeValue
        except:
            pass
        try:
            object_to_add.owner_surname = object.getElementsByTagName('owner_surname')[0].childNodes[0].nodeValue
        except:
            pass
        try:
            object_to_add.actual_user_first_name = object.getElementsByTagName('actual_user_first_name')[0].childNodes[
                0].nodeValue
        except:
            pass
        try:
            object_to_add.actual_user_last_name = object.getElementsByTagName('actual_user_last_name')[0].childNodes[
                0].nodeValue
        except:
            pass
        try:
            object_to_add.actual_user_surname = object.getElementsByTagName('actual_user_surname')[0].childNodes[
                0].nodeValue
        except:
            pass
        try:
            object_to_add.square = float(
                object.getElementsByTagName('square')[0].childNodes[0].nodeValue.replace(',', '.'))
        except:
            return []

        result.append(object_to_add)

    return result


res = get_objects_by_xml('1.xml')

for o in res:
    print(o)

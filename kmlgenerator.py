import simplekml


def generate():
    kml = simplekml.Kml()
    data = fetch_data()
    for item in data:
        # Modify this
        pnt = kml.newpoint(name=item["text"], coords=[(item["lat"], item["lng"])])
        # Example if condition
        if item["text"].startswith("B"):
            pnt.labelstyle.color = 'ff0000ff'
        else:
            pnt.labelstyle.color = 'ffffff00'
        pnt.labelstyle.scale = 2  # Text twice as big
        pnt.iconstyle.color = 'ffff0000'  # Blue
        pnt.iconstyle.scale = 3  # Icon thrice as big
        pnt.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/info-i.png'  # Culry 'information i
    return kml.kml()


def fetch_data():
    # Modify this
    data = [{"lat": 12.34, "lng": 45.56, "text": "Bonjour"}, {"lat": 12.44, "lng": 46.56, "text": "Goodbye"}]
    return data

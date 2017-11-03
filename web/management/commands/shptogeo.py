from django.core.management.base import BaseCommand
import shapefile

class Command(BaseCommand):
    help = "Converts a shapefile into a GEOjson dump."

    def add_arguments(self, parser):
        parser.add_argument('shapefile')

    def handle(self, *args, **options):
        # read the shapefile
        shape_file = options['shapefile']
        reader = shapefile.Reader(shape_file)
        fields = reader.fields[1:]
        field_names = [field[0] for field in fields]
        buffer = []
        for sr in reader.shapeRecords():
           atr = dict(zip(field_names, sr.record))
           geom = sr.shape.__geo_interface__
           buffer.append(dict(type="Feature", \
            geometry=geom, properties=atr))

        # write the GeoJSON file
        from json import dumps
        geojson = open("pyshp-demo.json", "w")
        geojson.write(dumps({"type": "FeatureCollection",\
        "features": buffer}, indent=2) + "\n")
        geojson.close()

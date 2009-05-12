import os, sys

from django.core import serializers

def install_apex_vertex(json_file=None):
    """ Load handset JSON dump to Django SQL database.
    
    Simulate command line django-admin.py loaddata command to load the initial handset database
    
    @param json_file: JSON entries to load or None to use built in public JSON sample
    """

    if json_file == None:
        # Use publich sample file
        path = os.path.dirname(sys.modules["mobile.sniffer.apexvertex"].__file__)
        json_file = os.path.join(path, "public_handsets.json")
    
    
    f = open(json_file, "rt")
    data = f.read()
    f.close()
    
    # Deserialize JSON to the (memory) database
    objects = serializers.deserialize("json", data)
    for o in objects:
        o.save()
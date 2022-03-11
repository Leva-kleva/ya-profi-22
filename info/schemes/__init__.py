from jsonschema import validate
import schemes.search


def check(request, schema):
    try:
        validate(instance=request.json, schema=schema)
        return True
    except:
        return False

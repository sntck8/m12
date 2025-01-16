from pprint import pprint

def introspection(obj):
    type_obj = (type(obj))
    attr_obj = (dir(obj))
    hasattr_obj = (hasattr(obj, 'imag'))
    getattr_obj = (getattr(obj, 'type_obj', "Hi"))
    call_obj = (callable(obj))
    iis_obj = (isinstance(obj, int))
    return [type_obj, attr_obj, hasattr_obj,
            getattr_obj, call_obj, iis_obj]

number_info = introspection(42)
pprint(number_info)

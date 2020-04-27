import json

_KEYS = ['__dict__', '__doc__', '__module__', '__weakref__']


class JsonEncoder(object):
    def __init__(self, skipkeys=False, ensure_ascii=True,
                 check_circular=True, allow_nan=True, sort_keys=False,
                 indent=None, separators=None, default=None):
        self.skipkeys = skipkeys
        self.ensure_ascii = ensure_ascii
        self.check_circular = check_circular
        self.allow_nan = allow_nan
        self.sort_keys = sort_keys
        self.indent = indent
        self.item_separator = separators
        self.default = default

    def encode(self, obj):
        if list == type(obj):
            r = [self.modelToDict(o) for o in obj]
        else:
            r = self.modelToDict(obj)
        return json.dumps(r, skipkeys=self.skipkeys, ensure_ascii=self.ensure_ascii,
             check_circular=self.check_circular, allow_nan=self.allow_nan, sort_keys=self.sort_keys,
             indent=self.indent, separators=self.item_separator, default=self.default)

    def modelToDict(self, obj):
        result = dict()
        for key in self.keys(obj.__class__):
            result[key] = getattr(obj, key)
        return result

    def keys(self, modelClass):
        for key in dir(modelClass):
            if not callable(getattr(modelClass, key)) and key not in _KEYS:
                yield key











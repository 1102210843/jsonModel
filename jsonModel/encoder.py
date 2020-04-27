import json

_KEYS = ['__dict__', '__doc__', '__module__', '__weakref__']
_CALSS = [int, float, bool, complex, str, dict]


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
        r = self.__transform__(obj)
        return json.dumps(r, skipkeys=self.skipkeys, ensure_ascii=self.ensure_ascii,
             check_circular=self.check_circular, allow_nan=self.allow_nan, sort_keys=self.sort_keys,
             indent=self.indent, separators=self.item_separator, default=self.default)

    def __transform__(self, obj):
        if list == obj.__class__:
            result = [self.__modelToDict__(o) for o in obj]
        elif obj.__class__ not in _CALSS:
            result = self.__modelToDict__(obj)
        else:
            result = self.__modelToDict__(obj)
        return result

    def __modelToDict__(self, obj):
        if obj.__class__ in _CALSS:
            return obj
        result = dict()
        for key in self.__keys__(obj.__class__):
            v = getattr(obj, key)
            if v.__class__ not in _CALSS:
                result[key] = self.__transform__(v)
            else:
                result[key] = v
        return result

    def __keys__(self, modelClass):
        for key in dir(modelClass):
            if not callable(getattr(modelClass, key)) and key not in _KEYS:
                yield key











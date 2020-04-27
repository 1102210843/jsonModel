
__version__ = '1.0.0'
__all__ = [
    'dumps', 'loads',
    'JsonDecoder', 'JsonEncoder',
]

__author__ = 'Sun Yu <18610863095@163.com>'

from .encoder import JsonEncoder
from .decoder import JsonDecoder


_default_encoder = JsonEncoder(
    skipkeys=False,
    ensure_ascii=True,
    check_circular=True,
    allow_nan=True,
    indent=None,
    separators=None,
    default=None,
)


def dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True,
        allow_nan=True, cls=None, indent=None, separators=None,
        default=None, sort_keys=False):
    # cached encoder
    if (not skipkeys and ensure_ascii and
            check_circular and allow_nan and
            cls is None and indent is None and separators is None and
            default is None and not sort_keys):
        return _default_encoder.encode(obj)
    if cls is None:
        cls = JsonEncoder
    return cls(
        skipkeys=skipkeys, ensure_ascii=ensure_ascii,
        check_circular=check_circular, allow_nan=allow_nan, indent=indent,
        separators=separators, default=default, sort_keys=sort_keys).encode(obj)


_default_decoder = JsonDecoder(object_hook=None, object_pairs_hook=None)


def loads(s, mClass, *, encoding=None, cls=None, object_hook=None, parse_float=None,
        parse_int=None, parse_constant=None, object_pairs_hook=None, **kw):
    if (cls is None and object_hook is None and
            parse_int is None and parse_float is None and
            parse_constant is None and object_pairs_hook is None and not kw):
        return _default_decoder.decode(s, mClass)
    if cls is None:
        cls = JsonDecoder
    if encoding is not None:
        kw['encoding'] = encoding
    if object_hook is not None:
        kw['object_hook'] = object_hook
    if object_pairs_hook is not None:
        kw['object_pairs_hook'] = object_pairs_hook
    if parse_float is not None:
        kw['parse_float'] = parse_float
    if parse_int is not None:
        kw['parse_int'] = parse_int
    if parse_constant is not None:
        kw['parse_constant'] = parse_constant
    return cls(**kw).decode(s, mClass)






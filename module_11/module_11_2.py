import inspect


def introspection_info(obj):
    info = {
        'type': str(type(obj)),
        'attributes': None,
        'methods': None,
        'module': None
    }

    if hasattr(obj, '__module__'):
        info['module'] = obj.__module__
    else:
        if isinstance(obj, (int, float, str, list, dict, set, tuple)):
            info['module'] = 'builtins'
        else:
            info['module'] = 'Нет модуля'
    all_attributes = dir(obj)
    methods = []
    attributes = []
    for attr in all_attributes:
        if callable(getattr(obj, attr)) and (inspect.ismethod(getattr(obj, attr)) or inspect.isfunction(getattr(obj, attr))):
            methods.append(attr)
        else:
            attributes.append(attr)
    info['methods'] = methods
    info['attributes'] = attributes
    return info


class MyClass:
    def method1(self):
        pass

    def method2(self):
        pass


obj = MyClass()
info = introspection_info(obj)
print(info)

number_info = introspection_info(42)
print(number_info)

string_info = introspection_info("Hello")
print(string_info)
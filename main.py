import importlib
from human import Human
import glob
from os import path


def main():
    for f in glob.glob('dynamic/*.py'):
        module_name = path.splitext(path.basename(f))[0]
        if module_name == '__init__':
            continue
        module = importlib.import_module('dynamic.' + module_name)
        for obj_name in dir(module):
            obj = getattr(module, obj_name)
            try:
                is_human = isinstance(obj(), Human)
            except TypeError:
                continue
            if is_human:
                instance = obj(19)
                instance.execute()

if __name__ == '__main__':
    main()

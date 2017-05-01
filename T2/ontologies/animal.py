# TODO: find a better filename

import sys
from io import StringIO
from os.path import realpath

sys.stderr = StringIO()

import owlready

if __name__ == '__main__':
    owlready.onto_path.append(realpath('.'))

    onto = owlready.Ontology('onto.owl')

    onto.save()

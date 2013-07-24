#!/bin/bash

pep8 pythontest.py > pep8.log
pylint pythontest.py --output-format=parseable --report=yes > pylint.log
nosetests pythontest.py --with-xunit --with-coverage --cover-branches
coverage xml --omit='/usr/*' -o coverage.xml

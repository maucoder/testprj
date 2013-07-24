#!/bin/bash

nosetests pythontest.py --with-xunit --with-coverage --cover-branches
coverage xml --omit='/usr/*' -o coverage.xml

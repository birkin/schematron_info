# -*- coding: utf-8 -*-

"""
Demo of how to use schematron with lxml.
    - example from <http://lxml.de/validation.html>
"""

import sys
import lxml
from lxml import etree, isoschematron


assert sys.version_info >= ( 3,0 )  # just to show this works with v3x


## make docs
with open( './schematron.xml', 'r' ) as fh:
    schematron_doc = etree.parse( fh )
with open( './source_bad.xml', 'r' ) as fh:
    bad_doc = etree.parse( fh )
with open( './source_good.xml', 'r' ) as fh:
    good_doc = etree.parse( fh )

## make the schematron test-object
schematron = isoschematron.Schematron( schematron_doc )  # type(schematron) == lxml.isoschematron.Schematron

## apply test
result = schematron.validate( bad_doc )  # type(result) == bool
assert result == False
result = schematron.validate( good_doc )
assert result == True


"""
that's it -- but you can examine the output, too
fyi:
    - type(schematron_2.validation_report) == lxml.etree._XSLTResultTree
    - type(report) == bytes
"""

schematron_2 = isoschematron.Schematron( schematron_doc, store_report=True )

result = schematron_2.validate( bad_doc )
assert result == False
report = etree.tostring( schematron_2.validation_report, pretty_print=True )
print( '--------------------' )
print( 'bad doc report, ```\n%s```' % report.decode('utf-8') )

result = schematron_2.validate( good_doc )
assert result == True
report = etree.tostring( schematron_2.validation_report, pretty_print=True )
print( '--------------------' )
print( 'good doc report, ```\n%s```' % report.decode('utf-8') )

print( '--------------------' )

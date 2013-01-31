# -*- coding: utf-8 -*-

import lxml
from lxml import etree, isoschematron

## make docs
schematron_doc = etree.parse( open(u'./schematron.xml') )  # type(schematron_doc) == lxml.etree._ElementTree
bad_doc = etree.parse( open(u'./source_bad.xml') )
good_doc = etree.parse( open(u'./source_good.xml') )

## make the schematron test-object
schematron = isoschematron.Schematron( schematron_doc )  # type(schematron) == lxml.isoschematron.Schematron

## apply test
result = schematron.validate( bad_doc )  # type(result) == bool
assert result == False
result = schematron.validate( good_doc )
assert result == True

## examine output
schematron_2 = isoschematron.Schematron( schematron_doc, store_report=True )
#
result_2 = schematron_2.validate( bad_doc )  # type(schematron_2.validation_report) == lxml.etree._XSLTResultTree
assert result_2 == False
report = etree.tostring( schematron_2.validation_report, pretty_print=True )  # type(report) == str
print u'REPORT:\n%s\n\n' % report.decode(u'utf8', u'replace')
#
result_2 = schematron_2.validate( good_doc )
assert result_2 == True
report = etree.tostring( schematron_2.validation_report, pretty_print=True )
print u'REPORT:\n%s\n\n' % report.decode(u'utf8', u'replace')

Overview
========

- a way of validating xml; assertion-based; familiar to [TDD-ers] [TDD].

- from [wikipedia][WIK]: _"...Schematron is a rule-based validation language for making assertions about the presence or absence of patterns in XML trees. It is a structural schema language expressed in XML using a small number of elements and XPath."_

[TDD]: http://en.wikipedia.org/wiki/Test-driven_development
[WIK]: http://en.wikipedia.org/wiki/Schematron


Resources
=========

- wonderful [introduction][INT] (**especially** the section 'Schematron hierarchy'), and the full article includes information about how schematron complements other xml schemas
  - 'assertions' define conditions to test
  - 'rules' define the context, or where in the document to apply the conditions

- hands on tutorial, [ibm developerworks][IBM]

- concise [schematron test examples][EXA], showing, for each example, the schematron test xml, minimalist source xml that passes and fails and expected test output.

- [schematron validation with lxml][LXM], a popular python xml library

[INT]: http://www.topologi.com/public/Schtrn_XSD/Paper.html
[IBM]: https://web.archive.org/web/20131007161526/http://www.ibm.com/developerworks/xml/tutorials/x-schematron/
[EXA]: http://www.zvon.org/xxl/SchematronTutorial/General/toc.html
[LXM]: http://lxml.de/validation.html


Code
====

- simple [validation example][VAL] using lxml; shows how to view validation output.

[VAL]: https://github.com/birkin/schematron_info/blob/master/code.py

---


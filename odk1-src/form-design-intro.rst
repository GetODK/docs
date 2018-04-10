Intro to Forms in ODK
========================

Forms used in the ODK ecosystem are XML documents following the `ODK XForms specification <https://opendatakit.github.io/xforms-spec/>`_, a subset of the `W3C XForms specification <https://www.w3.org/TR/xforms/>`_. (`Example XForms are available for reference. <https://github.com/opendatakit/sample-forms>`_)

Most ODK tools use the `ODK JavaRosa <https://github.com/opendatakit/javarosa>`_ library to render forms. Form transfer between ODK components is governed by the :doc:`openrosa` API.

Because of the complexity of the XForms format, we do not recommend coding XForms directly in XML. The recommended process is:

1. Begin with one of the :ref:`compliant-build-tools`.
2. Edit the XML only if necessary.

   - Before editing an XForm directly, you need to be familiar with the `ODK XForm specification <https://github.com/opendatakit/xforms-spec>`_.

3. Use :doc:`validate` to check that the edited XForm is well-formed and fully compliant.


.. _excel-based-form-creation:

Excel-based form creation
---------------------------------

Most ODK users design their forms in Excel, following the `XLSForm <http://xlsform.org/>`_ specification. To convert XLSForms to XForms, you can use:

- `ODK's online XLSForm converter <http://opendatakit.org/xiframe/>`_
- `XLSForm Offline for Mac or Windows <https://gumroad.com/l/xlsform-offline>`_
- `XLSForm for Windows <https://opendatakit.org/downloads/download-info/xlsform-for-windows/>`_
- :doc:`pyxform`, a Python XLSForm converter with a command-line tool

.. tip::

  If you are comfortable with using the command-line, Pyxform is the most efficient XLSForm converter.

.. _drag-and-drop-form-creation:

Drag-and-drop form creation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  
For simple forms, :doc:`odk-build` is a drag-and-drop form designer that works both online and offline.

********************
Aggregate Usage
********************

ODK Aggregate can be used to collect data from ODK collect, filter the submiited data and export it to useful formats. It provides a mechanism for hosting the survey forms and gathering the survey results. 

When the URL to the ODK Aggregate server is first opened, you will be presented with the application page showing the :guilabel:`Submissions` and :guilabel:`Form Management` tabs. You will also see a :guilabel:`Log In` option and three help buttons.

.. image:: /img/aggregate-use/server-start.*
   :alt: Image showing tabs on Aggregate server.

.. _form-manage:

Form Management
----------------

You can add, download and delete forms, export data into useful formats, publish data into another service, manually upload submissions and view the published data. ODK Aggregate provides all these options under the :guilabel:`Form Management` tab.

.. _create-manage:

Managing forms
~~~~~~~~~~~~~~~~

You can view all your forms, add new forms, delete forms, download forms as well as restrict submissions for a form.

Click on :guilabel:`Forms list` tab to see a list of all your forms.  

.. image:: /img/aggregate-use/form-list.*
   :alt: Image showing list of all forms.

Under the :guilabel:`Form list` tab, you will see :guilabel:`Add New Form` button  to upload a new form definition to ODK Aggregate. 

.. image:: /img/aggregate-use/add-form.*
   :alt: Image showing add form button.

When you click on it a box will open asking for details of the form. `Form Definition` is required and `Media File(s)` is optional. Choose the .xml file that will be used. You can also choose the appropriate media files for the form.  

.. image:: /img/aggregate-use/add-form-options.*
   :alt: Image showing add form options.

You can manage all the forms present on your server in your form list. All options displayed in the form list are as follow:

- Click on :guilabel:`Title` to view the XML for a form. You can then download XML for that form by clicking on :guilabel:`Download XML` in the Form XML Viewer.

.. image:: /img/aggregate-use/xml-viewer.*
   :alt: Image showing xml viewer for form.

- :guilabel:`Form Id` is the unique name for the form.
- :guilabel:`Media Files` displays the count of media files you have uploaded for the form.
- :guilabel:`User` is the user who uploaded the form.
- Clicking on :guilabel:`Downloadable` checkbox enables/disables Aggregate from displaying the form to remote clients so that they can download the form.
- Clicking on :guilabel:`Accept Submissions` checkbox enables/disables Aggregate ability to accept submissions for the particular form. 

.. tip::

  Disable accepting submission by unchecking the :guilabel:`Accept Submissions` checkbox if you want to prevent users from submitting more data for a particular form.

- Click on :guilabel:`Delete` when you want to remove a form.     

.. _export-form:

Exporting form data
~~~~~~~~~~~~~~~~~~~~~~~

Click on :guilabel:`Export` option in the form list to export form into useful formats and choose the format in which you want to export data. You can also choose a filter which you have saved for the form to export only a certain substet of form. Details on :ref:`exporting data <export-data>` are given in the :ref:`data transfer <transfer-data>` section.   

.. _publish-form:

Publishing form data
~~~~~~~~~~~~~~~~~~~~~~
 
Click on :guilabel:`Publish` option in the form list to publish the form into another service. You can choose where you want to publish data and which data you want to publish. Details on :ref:`publishing data <publish-data>` are given in the :ref:`data transfer <transfer-data>` section.

.. _view-publish-data:

Viewing Published data
~~~~~~~~~~~~~~~~~~~~~~~

You can get a view of the published data you have created for a particular form by clicking on :guilabel:`Published Data`. 

.. image:: /img/aggregate-use/published-data.*
   :alt: Image showing published data.

- Select the form corresponding to the published data in the :guilabel:`Form` dropdown.
- Read the message that appears and click on :guilabel:`Purge Published Data`.
- :guilabel:`Created By` shows the email of the user who created the published file.
- :guilabel:`Status` can be `ACTIVE` (the file is ready to view) or `ESTABLISHED` (something went wrong in the process of exporting.)
- :guilabel:`Start Date` shows the time when you finished filling out the :guilabel:`Publish` form.
- :guilabel:`Action` is based on your selection of upload only, stream only, or both in the :guilabel:`Publish` form.
- :guilabel:`Type` shows the type you choose to publish your data to.
- :guilabel:`Owner` shows the owner of the published data.
- :guilabel:`Name` is the place where you published your data. If the type was a Google Fusion Table, click on the link to view the Fusion Table.
- Select delete box in the :guilabel:`Delete` column if you want to delete your published file.     


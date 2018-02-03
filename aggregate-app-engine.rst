Installing on App Engine
================================

.. note:: 

  Google App Engine is the recommended deployment platform for Aggregate. 
  
  There is no charge to set up an Aggregate server on App Engine, and lightly used instances will usually incur no charges.


.. admonition:: Before you begin...

  - Make sure `Java 8 <https://java.com/en/download/>`_ or higher is `installed on your system <https://www.java.com/en/download/help/download_options.xml>`_.
  
  - You will need a Gmail account to use App Engine; this Gmail account will be the owner of the Google Cloud Platform project under which your App Engine will execute.

  - Read the `Google Cloud Platform term of service <https://cloud.google.com/terms/>`_.

  .. _download-aggregate-installer: 
    
  - Download `ODK Aggregate <https://opendatakit.org/downloads/>`_. Select the latest release for your operating system.

    - You can :doc:`verify the download <verify-downloads>` using *SHA256 signatures*.
    - If you are running OSX, you must unzip the downloaded file before running the installer within it.
    - If you are on MacOSX Mountain Lion or onward, you will need to fiddle with `GateKeeper settings <http://osxdaily.com/2012/07/27/app-cant-be-opened-because-it-is-from-an-unidentified-developer/>`_ in order to run the installer.
    - If you are on Windows 10, you will need to approve running an unsigned installer.
    - If you are on Linux, you will need to change the downloaded file's permissions to enable running it as a program. Right click on the file and click on :guilabel:`Properties`. Click on :guilabel:`Permissions` tab. Now check the box labeled as :guilabel:`Allow executing file as program`.
  
    


1. Go to `Google Cloud Platform <https://cloud.google.com/>`_ and click on :guilabel:`Console` in the top right corner.

   .. image:: /img/aggregate-install/cloud-console.*
     :alt: An image showing the console option on the Google Cloud Platform.

2. Sign in with a Gmail account which you wish to use.

   .. image:: /img/aggregate-install/email-select.*
     :alt: Image showing the sign in window of Gmail.

3. If you have never configured a Google Cloud Platform project, click on :guilabel:`Create an Empty Project`.

   .. image:: /img/aggregate-install/empty-project.*
     :alt: Image showing Create an empty project option for first projects. 

4. If you have configured a Google Cloud Platform project before, this link will open onto either a page with a :guilabel:`Create Project` button and a table listing all of your projects, or it will open into one of your existing projects. In the later case, click on that project name at the top of the window. In the below image, the older project is `Project-edu`.

   .. image:: /img/aggregate-install/project.*
     :alt: Image showing previous project name `Project-edu`.

   - Upon clicking on the project name, a window appears with a :guilabel:`+` symbol. Click on it to create a new project.   

     .. image:: /img/aggregate-install/create-project.*
       :alt: Image showing the + sign which denotes creating a new project.

5. Name your project.

   On the project-creation popup dialog, type in a project name that makes sense to you. You can enter a project name and click on :guilabel:`Create` if you don't want to edit the project ID. You can choose :guilabel:`Edit` if you want to edit the project ID. The project ID will be the first part of the URL to your ODK Aggregate server.

   .. image:: /img/aggregate-install/project-name.png
     :alt: Image showing the window to enter a project name.

   - If you click on :guilabel:`Edit`, a window will appear where you can enter a project id. After changing the project id click on :guilabel:`Create` to create your project.

     .. image:: /img/aggregate-install/project-id.*
       :alt: Image showing the window which comes after clicking on edit option to change the project id.

   .. tip::

     You may want to use a project id that combines your organization name and the name of your data collection group or project. 
     
   .. note::
   
     You may need to accept Google's terms and conditions.

6. After few seconds, you will see a notification in the top right corner of the window. Click on the notification icon and select the notification message **Create Project:your project name**.
  
   .. image:: /img/aggregate-install/notification.*
     :alt: Image showing blue notification icon.

   .. image:: /img/aggregate-install/go-to-project.*
     :alt: Image showing the option to create your project.      

7. You will be directed to an empty project screen showing the details of your project. If you want to change any settings, click on :guilabel:`Go to project settings` otherwise click on the menu icon (:guilabel:`☰`) to the left of :guilabel:`Google Cloud Platform` in the upper left side of the screen, and select :guilabel:`App Engine` from the dropdown menu.

   .. image:: /img/aggregate-install/project-settings.*
     :alt: Image showing the project settings option and the menu option.

   .. image:: /img/aggregate-install/app-engine.*
     :alt: Image showing App Engine option.

8. Click on the :guilabel:`Select a language` menu and select :guilabel:`Java`.

   .. image:: /img/aggregate-install/language-select.*
     :alt: Image showing option to select a language.

   .. image:: /img/aggregate-install/select-java.*
     :alt: Image showing various language options to choose from.

9. Select your preferred datacenter location and click :guilabel:`Next`.

   .. image:: /img/aggregate-install/select-region.*
     :alt: Image showing options to choose a region where the server will operate.

10. Google will then begin configuring the server.

    .. image:: /img/aggregate-install/prepare-engine.*
      :alt: Image showing Google configuring the server.

11. When this completes, you will be directed to begin a tutorial to install a sample application. Choose :guilabel:`Cancel Tutorial` and confirm that you want to not perform that tutorial.

    .. image:: /img/aggregate-install/cancel-tutorial.*
      :alt: Image showing option to cancel the tutorial.

12. Launch the ODK Aggregate installer on you computer. (:ref:`See download info here. <download-aggregate-installer>`) 

    The installer will guide you through configuring ODK Aggregate for App Engine. Click on the :guilabel:`Forward` button each time you complete a step to move ahead.

    .. image:: /img/aggregate-install/setup.*
      :alt: Image showing the installer for ODK Aggregate.

13. Accept the license agreement.

    .. image:: /img/aggregate-install/agreement.*
      :alt: Image showing license agreement.

14. Select a parent directory under which an :file:`ODK Aggregate` directory will be created to contain the configured software. Click on the :guilabel:`folder` icon to choose a directory.

    .. image:: /img/aggregate-install/directory-setup.*
      :alt: Image showing window to choose a parent directory. 

15. Select :guilabel:`Google App Engine` as the platform for the Aggregate server.

    .. image:: /img/aggregate-install/choose-platform.*
      :alt: Image displaying options to choose a platform for Aggregate.

16. Enter a name for your ODK Aggregate instance.

    .. image:: /img/aggregate-install/set-name.*
      :alt: Image showing window to select a name for your Aggregate instance.

    .. note::    
   
      The ODK Aggregate instance name will be displayed to your users when they log into ODK Aggregate using their username and password.

    .. tip::
   
      Including the name of your organization in the instance name can help users confirm that they have contacted the correct website.

17. Enter a superuser name in the next window.

    .. image:: /img/aggregate-install/superuser.*
      :alt: Image showing window to enter a superuser name.

    .. note::
   
      - The user with the superuser account will have full permissions on the system.
      - The password for this user will be set to **aggregate** initially.
      - Only this user will be allowed to log onto the system when ODK Aggregate is run for the first time.
      - Upon first logging in, the superuser should change the password and complete the configuration of ODK Aggregate by specifying additional users and what permissions they will have on the system.

18. Enter the project ID of the project you created on the Google Cloud platform.

    .. image:: /img/aggregate-install/application-id.*
      :alt: Image showing project id of the project created earlier entered in the application id box.

19. The installer will configure Aggregate and launch a upload tool.  

    .. tip::

      Beginning with Java 7 Update 51, there are security level settings that may prevent the upload tool from running. A reported workaround is to add the *file: path* (e.g., :file:```file:///```) to the Exception Site list.

20. Enter the Gmail account that you specified when setting up the App Engine project. This will enable the :guilabel:`Get Token` button.

    .. image:: /img/aggregate-install/get-token.*
      :alt: Image showing the window for upload tool to enter the email id and get a token.

21. Click the :guilabel:`Get Token` button. 

    - Your default browser will open to a Google site (``accounts.google.com``) where you are asked to choose a Gmail account. Select the account you specified earlier when setting up App Engine, and then allow *Google App Engine appcfg* to view and manage your AppEngine instances and datastores. Click :guilabel:`Allow`. This will take you to a screen with instructions to copy a code.

      .. image:: /img/aggregate-install/allow.*
        :alt: Image showing window asking for App Engine Permissions.

    - At the same time, a popup dialog should be displayed by the install wizard. 

      .. tip::

        - If the pop-up dialog does not show, you will need to relaunch the upload tool. Close the upload tool and open a file browser or Finder window in the directory you specified earlier. Navigate to the ODK Aggregate directory.
	
          - If on Windows, double-click the :file:`ODKAggregateAppEngineUpdater.jar` file. 
          - If on Mac OSX, double-click the :file:`uploadAggregateToAppEngine.app` file. 
          - If on Linux, open a bash shell and run :file:`uploadAggregateToAppEngine.sh`.
	   
        - Re-enter the e-mail address, and once again click :guilabel:`Get Token`. The pop-up dialog should now appear.

22. Copy the code from the browser into the installer's popup dialog and click :guilabel:`OK`.

    .. image:: /img/aggregate-install/token.*
      :alt: Image showing pop-up dialog to enter a token.

    .. tip::
    
      The text box on Google's site is not as wide as the code; be sure to copy the entire code. 

23. If everything went well, you should see a status message letting you know the ``Action Succeeded``.
  
    .. image:: /img/aggregate-install/success-output.*
      :alt: Image showing output for a successful result.

    .. tip::
    
      - If the output does not look like that, you may have delayed too long between getting the code and pasting it into the tool. Click :guilabel:`Delete Token` and try again.
      - If you see a failure message in the output window, then it is likely that you have several different Gmail accounts and Google has gotten confused during the token-issuing process. In this case, when the browser window opens, before selecting an account, copy the URL, open a Private Browsing or Incognito Window in your browser, and paste the URL into that. Then proceed to get the token, etc. This should fix this issue.

24. Click :guilabel:`Upload ODK Aggregate`.

    .. image:: /img/aggregate-install/upload.*
      :alt: Image showing successful output and upload option.

    Clicking on :guilabel:`Upload ODK Aggregate` will generate a very long list of progress messages into the Output window. The `listBackends :` and `deleteBackendBackground :` sections may report "500 Internal Server Error" and Severe errors, and Warnings about the use of Backends, a deprecated feature. You will see a number of warnings and errors; this is expected. 
    
    For reference, here is a list of few of those errors:
   
    .. code-block:: none
      :class: details

        listBackends : Warning: This application uses Backends, a deprecated feature that has been replaced by Modules, which offers additional functionality. Please convert your backends to modules as described at: https://developers.google.com/appengine/docs/java/modules/converting.

        listBackends! : WARNING: Error posting to URL: https://appengine.google.com/api/backends/delete?backend=background&app_id=project-123-181306&   
        listBackends! : 500 Internal Server Error
   
        listBackends : Unable to list backends: Error posting to URL: https://appengine.google.com/api/backends/list?app_id=project-123-181306&
        listBackends : 500 Internal Server Error

        deleteBackendBackground : Warning: This application uses Backends, a deprecated feature that has been replaced by Modules, which offers additional functionality. Please convert your backends to modules as described at: https://developers.google.com/appengine/docs/java/modules/converting.

        deleteBackendBackground!: WARNING: Error posting to URL: https://appengine.google.com/api/backends/delete?backend=background&app_id=project-123-181306&
        deleteBackendBackground!: 400 Bad Request      

        deleteBackendBackground : Unable to delete backend: Error posting to URL: https://appengine.google.com/api/backends/delete?backend=background&app_id=project-123-181306& 
        deleteBackendBackground : 400 Bad Request     
           

25. Finally, you should see the message ``status : Action Succeeded!``. 

    - To get a more clear view, you can see an `example log <https://opendatakit.org/wp-content/uploads/Apr2016-GoogleCloud/exampleUploadScriptOutput.txt>`_. 
   
    
26. Once the installer has run and uploaded the ODK Aggregate configuration to App Engine, return to the Google Cloud Platform console. 

27. With the console displaying your project, click on the menu icon (☰) to the right of *Google Cloud Platform* in the upper left side of the screen and select :guilabel:`App Engine` from the menu.

28. Click on the project's URI in the top right corner of the window. This will open your Aggregate server page.

    .. image:: /img/aggregate-install/project-aggregate.*
      :alt: Image showing a window where server url is displayed on top right corner.

29. :guilabel:`Log In` with the superuser username that you specified in the installer (the initial password for this username will be ``aggregate``), and access the site administration screens for your server.  

    .. image:: /img/aggregate-install/server.*
      :alt: Image showing ODK Aggregate server and log in option.

30. You should immediately change your superuser password.

    Go to :menuselection:`Site Admin -> Permissions` to change your password. You can also add additional users.
      

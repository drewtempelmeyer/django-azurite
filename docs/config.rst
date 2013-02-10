Configuration Variables
***********************

Below are a list of settings for django-azurite. All of these belong within the ``AZURITE``
dict in your project's ``settings.py``.

``ACCOUNT_NAME``
----------------

Default is ``None``.

The storage account name for the Windows Azure Storage. To obtain the ``ACCOUNT_NAME``, refer
to `How to: View, copy, and regenerate storage access keys`_.

.. _`How to: View, copy, and regenerate storage access keys`: http://www.windowsazure.com/en-us/manage/services/storage/how-to-manage-a-storage-account/#regeneratestoragekeys


``ACCOUNT_KEY``
---------------

Default is ``None``.

The storage account key for the Windows Azure Storage. To obtain the ``ACCOUNT_KEY``, refer
to `How to: View, copy, and regenerate storage access keys`_.

.. _`How to: View, copy, and regenerate storage access keys`: http://www.windowsazure.com/en-us/manage/services/storage/how-to-manage-a-storage-account/#regeneratestoragekeys


``CONTAINER``
-------------

Default is ``None``.

The container to store any uploaded media files from your models. For more information on how
manage your containers, refer to `How to Add or Remove a Windows Azure Storage Container`_.


``STATIC_CONTAINER``
--------------------

Default is ``None``.

The container to store your static files when running ``python manage.py collectstatic``. For
more information on how manage your containers, refer to
`How to Add or Remove a Windows Azure Storage Container`_.

.. _How to Add or Remove a Windows Azure Storage Container: http://technet.microsoft.com/en-us/library/hh495450.aspx


``CDN_HOST``
------------

Default is ``None``.

The hostname for the CDN service. Activating the CDN service is a bit hidden, but Microsoft
has a tutorial on `Using CDN for Windows Azure`_. The hostname would be similar to::

    az123456.vo.msecnd.net

.. _Using CDN for Windows Azure: http://www.windowsazure.com/en-us/develop/net/common-tasks/cdn/


``USE_SSL``
-----------

Default is ``False``.

Set to ``True`` if you need to use https. ``False`` should be sufficient for most sites.

**Note:** If using the CDN service be sure to enable HTTPS.

.. toctree::
   :maxdepth: 2

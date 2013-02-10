django-azurite
==============

django-azurite provides custom Django storage classes to store files on a Windows Azure
storage service.

Installation
************

Install the latest version from PyPI::

    pip install django-azurite

Install the latest development version::

    pip install -e git://github.com/drewtempelmeyer/django-azurite.git#egg=django-azurite

Add ``azurite`` to your ``INSTALLED_APPS`` in your Django ``settings.py`` file::

    INSTALLED_APPS = (
      ...
      'azurite',
    )

Usage
*****

Add the following to your Django project's ``settings.py`` file::

    AZURITE = {
        'ACCOUNT_NAME': 'storageaccountname',
        'ACCOUNT_KEY': 'storagekey',
        'CONTAINER': 'media',
        'STATIC_CONTAINER': 'static',
        'CDN_HOST': None,
        'USE_SSL': False,
    }

More details about `django-azurite configuration variables`_.

.. _django-azurite configuration variables: config.html


Changing Your Media Storage
---------------------------

You'll need to change your ``DEFAULT_FILE_STORAGE`` in your Django project's ``settings.py``
to allow django-azurite to handle all media uploads from your models::

    DEFAULT_FILE_STORAGE = 'azurite.storage.AzureStorage'

Any time a file is uploaded it will be stored on the specified storage account.

Example::

    class Photo(models.Model):
        image = models.ImageField(upload_to='photos')

    photo = Photo.objects.get(pk=1)
    print photo.image.url
    "http://storageaccount.blob.core.windows.net/container/photos/image.jpg"


Using Static Files
------------------

django-azurite includes support for syncing your static files to Windows Azure Storage. This
takes load off of your server and allows you to take advantage of `Azure's CDN`_.

Add the following line to your project's ``settings.py`` file::

    STATICFILES_STORAGE = 'azurite.storage.AzureStaticStorage'

Now when running ``python manage.py collectstatic`` your static files will be uploaded to
Windows Azure Storage account into the specified ``STATIC_CONTAINER`` container.

.. _Azure's CDN: http://www.windowsazure.com/en-us/develop/net/common-tasks/cdn/


.. toctree::
   :maxdepth: 1

   Configuration <config>

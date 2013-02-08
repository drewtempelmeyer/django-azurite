from azurite.storage import AzureStorage
from django.db import models

azure_storage = AzureStorage()

class TestModel(models.Model):
    """
    Test all of the codes!
    """
    image = models.ImageField(storage=azure_storage, upload_to='azurite-tests')
    file_field = models.FileField(storage=azure_storage,
        upload_to='azurite-tests')

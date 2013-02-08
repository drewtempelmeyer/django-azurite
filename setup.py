from azurite import __version__
from setuptools import setup, find_packages

setup(
    name="django-azurite",
    version=__version__,
    description="Azure file storage for Django",
    long_description="Custom file storage for Django using Microsoft Azure's blob storage.",
    keywords="django, azure, microsoft, file, system, storage, blob",
    author="Drew Tempelmeyer",
    author_email="drewtemp@gmail.com",
    url="https://github.com/drewtempelmeyer/django-azurite",
    license="MIT",
    packages=find_packages(),
    zip_safe=False,
    install_requires=["azure>=0.6.1"],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)

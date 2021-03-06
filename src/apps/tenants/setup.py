from setuptools import setup, find_namespace_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
      name='purplship-server.tenants',
      version='2021.2',
      description='Multi-carrier shipping API muti-tenant module',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/PurplShip/purplship-server',
      author='Purplship Team',
      author_email='danielk.developer@gmail.com',
      license='AGPLv3',
      packages=find_namespace_packages("."),
      install_requires=[
            'purplship-server.core',
            'django-tenants',
      ],
      dependency_links=[
            'https://git.io/purplship',
      ],
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
      ],
      zip_safe=False
)

from setuptools import setup, find_packages

VERSION = '0.0.1'


setup(
    name="mkdocs-v1theme",
    version=VERSION,
    url='',
    license='BSD',
    description='Shane Test',
    author='ShaneV1',
    author_email='shane@test.ie',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'mkdocs.themes': [
            'v1theme = v1theme',
        ]
    },
    zip_safe=False
)
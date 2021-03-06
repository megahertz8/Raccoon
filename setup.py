from setuptools import setup, find_packages


with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name='raccoon-scanner',
    packages=find_packages(exclude="tests"),
    license="MIT",
    version='0.0.2',
    description='Offensive Security Tool for Reconnaissance and Information Gathering',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Evyatar Meged',
    author_email='evyatarmeged@gmail.com',
    url='https://github.com/evyatarmeged/Raccoon',
    install_requires=['beautifulsoup4', 'requests', 'dnspython', "lxml", "click", "fake-useragent"],
    package_data={
        "raccoon": [
            "wordlists/*",
            "requirements.txt",
            "README.md",
            "LICENSE"
        ]
    },
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'raccoon=raccoon.main:main'
        ]
    },
)

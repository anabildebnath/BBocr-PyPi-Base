from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.0.1'
DESCRIPTION = 'BBocr reconstruction package'
LONG_DESCRIPTION = 'A package that allows to reconstruct your recognizer output to create a html file'

# Setting up
setup(
    name="bbocr_reconstruction",
    version=VERSION,
    author="BBocr",
    author_email="<anabildebnath16@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['opencv-python', 'numpy', 'ApsisBNOCR','BeautifulSoup','HTMLFormatter','YOLO','Path'],
    keywords=['python', 'bbocr','reconstruction'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
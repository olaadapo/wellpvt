from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='wellpvt'
      , version='0.1' 
      , author="Ade Oyewole"
      , author_email="oyewoleadeoluwa@gmail.com"
      , description='Production well PVT calculations'
      , long_description=long_description
      , long_description_content_type="text/markdown"
      , url="https://github.com/olaadapo/wellpvt"
      , packages=['wellpvt'] 
      , classifiers=[
            "Programming Language :: Python :: 3"
          , "License :: OSI Approved :: MIT License"
          , "Operating System :: OS Independent"
        ]
      , python_requires='>=3.6
      , zip_safe=False)
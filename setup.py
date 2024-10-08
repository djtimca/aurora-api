import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="auroranoaa", 
    packages=["auroranoaa"],
    version="0.0.5",
    license='apache-2.0',
    author="Tim Empringham",
    author_email="tim.empringham@live.ca",
    description="NOAA Aurora Wrapper for Home Assistant Integration.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/djtimca/aurora-api",
    download_url = 'https://github.com/djtimca/aurora-api/archive/v_0.0.3.tar.gz',
    keywords = ['NOAA', 'Aurora'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    python_requires='>=3.6',
)
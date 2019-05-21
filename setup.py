import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="WebScraping",
    version="0.0.1",
    author="Harla",
    author_email="chweetharla@gmail.com",
    description="A small example package to get lyrics of songs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Harla/WebScrapingLyrics",
    packages=["Lyrics"],
    include_package_data=True,
    install_requires=["requests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

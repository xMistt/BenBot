import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="BenBot-async",
    version="0.0.1",
    author="xMistt",
    description="Asynchronous Python wrapper for BenBot API.",
    long_description_content_type="text/markdown",
    url="https://github.com/xMistt/BenBot",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'aiohttp',
      ],
)

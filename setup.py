import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="slack_notifier-imax2218", # Replace with your own username
    version="0.0.1",
    author="Imax 2218",
    author_email="imax2218@gmail.com",
    description="task notification package for slack",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RyotaFuwa/slack_notifier",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)
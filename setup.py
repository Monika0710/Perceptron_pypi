import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
PROJECT_NAME="Perceptron_pypi"
USER_NAME="monika0710"

setuptools.setup(
    name=f"{PROJECT_NAME}-{USER_NAME}",
    version="0.0.2",
    author=USER_NAME,
    author_email="monikabhargav11@gmail.com",
    description="It's an implementation of Perceptron",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{USER_NAME}/{PROJECT_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{USER_NAME}/{PROJECT_NAME}/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    install_requires=[
        "numpy",
        "tqdm",
        "logging"
    ]
)
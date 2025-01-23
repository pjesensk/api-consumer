from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='api-consumer',
    version='0.1.0', 
    description='Multiple API consumer library, primarily used in DevOps automation',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Pavol Jesensky',
    author_email='pjesensky@gmail.com,
    url='https://github.com/pjesensk/api-consumer.git', 
    packages=find_packages(), 
    install_requires=[ 
        'requests',
        'python-dotenv',
        'pandas',
        'numpy',
        'hvac',
        'jinja2',
        'cryptography'
    ],
    classifiers=[ 
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7', 
)
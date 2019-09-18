import io
import re

from setuptools import find_packages, setup

dev_requirements = [
    'bandit',
    'flake8',
    'isort',
    'pytest',
]
unit_test_requirements = [
    'pytest',
]
integration_test_requirements = [
    'pytest',
]
run_requirements = [
    'setuptools==39.0.1',
    'flasgger==0.9.2',
    'Flask==1.0.3',
    'Flask_RESTful==0.3.7',
    'loguru==0.3.2',
    'scikit-learn==0.21.3'
]

with io.open('./depression_classifier/__init__.py', encoding='utf8') as version_f:
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_f.read(), re.M)
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")

with io.open('README.md', encoding='utf8') as readme:
    long_description = readme.read()

setup(
    name="depression_classifier",
    version=version,
    author="Gabriel Nogueira",
    author_email="gabrielmvnogueira@gmail.com.br",
    include_package_data=True,
    license="COPYRIGHT",
    description="Classificador de depressão",
    long_description=long_description,
    zip_safe=False,
    install_requires=run_requirements,
    extras_require={
         'dev': dev_requirements,
         'unit': unit_test_requirements,
         'integration': integration_test_requirements,
    },
    python_requires='>=3.6',
    classifiers=[
        'Intended Audience :: Information Technology',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.6'
    ],
    keywords=(),
    entry_points={
        'console_scripts': [
            'depression_classifier = depression_classifier.__main__:start'
        ],
    },
)
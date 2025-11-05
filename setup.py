"""
Setup script for TextCopy
"""
from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
readme_file = Path(__file__).parent / 'README.md'
long_description = readme_file.read_text(encoding='utf-8') if readme_file.exists() else ''

# Read requirements
requirements_file = Path(__file__).parent / 'requirements.txt'
requirements = []
if requirements_file.exists():
    requirements = [
        line.strip()
        for line in requirements_file.read_text().splitlines()
        if line.strip() and not line.startswith('#')
    ]

setup(
    name='textcopy',
    version='1.0.0',
    description='System-wide text capture tool with hotkey support',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='TextCopy Contributors',
    url='https://github.com/Poorthing998/TextCopy',
    packages=find_packages(),
    package_dir={'': 'src'},
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'textcopy=textcopy:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
        'Environment :: Console',
    ],
    python_requires='>=3.7',
    keywords='clipboard text capture hotkey productivity notes',
    project_urls={
        'Bug Reports': 'https://github.com/Poorthing998/TextCopy/issues',
        'Source': 'https://github.com/Poorthing998/TextCopy',
    },
)

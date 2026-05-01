from setuptools import setup, find_packages

setup(
    name='api-security-dast',
    version='0.1',
    description='A project for security testing of APIs.',
    author='PBSO Pankar',
    author_email='your_email@example.com',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pyyaml',
        'pytest',
        'urllib3',
        'colorama',
        'tabulate',
    ],
    entry_points={
        'console_scripts': [
            'api-security-dast=your_module:main',  # Adjust your_module and main
        ],
    },
)
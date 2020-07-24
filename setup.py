    from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='shardbackup',
    version='0.0.2',
    author='Brian A Barnes-Cocke',
    author_email='bacocke08@gmail.com',
    description='shardbackup copies x (B - EiB) from a source directory to a target directory',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/babarnescocke/shardBackup',
    packages=find_packages('src'),
    package_dir={'': 'src'},
)

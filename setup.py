    from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='shardbackup',
    version='0.0.2',
    author='Brian A Barnes-Cocke',
    author_email='bacocke08@gmail.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/babarnescocke/shardBackup',
    packages=find_packages('src'),
    package_dir={'': 'src'},
)

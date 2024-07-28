from setuptools import setup, find_packages

setup(
    name="my_local_package",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
        # e.g., 'numpy', 'requests'
    ],
    author="Your Name",
    author_email="your_email@example.com",
    description="A brief description of your project",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    python_requires='>=3.9'
)

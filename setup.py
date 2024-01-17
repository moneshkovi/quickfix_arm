from setuptools import setup, find_packages

# Read the contents of your README file
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='quickfix_arm',
    version='0.1.0',
    author='Monesh Kovi',
    author_email='monesh.naidu1@gmail.com',
    description='A pip version of quickfix for ARM Machines',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/moneshkovi/Leetcode',
    packages=find_packages(),
    install_requires=[
        # Here, I'm assuming you meant 'numpy' as a Python package, not 'ruby'.
        # 'ruby' is not a Python package, so it cannot be included as a dependency in a Python project.
        'numpy',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    scripts=[
        'quickfix1/install_quickfix.py',  # Update this path if your script is located elsewhere
    ],
    entry_points={
        # If you have any console scripts, add them here
    },
    include_package_data=True,
    zip_safe=False,
)

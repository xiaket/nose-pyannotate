from setuptools import setup


VERSION = "0.2.0"

install_requires = [
    "nose",
    "pyannotate",
]


if __name__ == "__main__":
    setup(
        name="nose-pyannotate",
        version=VERSION,
        author="Kai Xia",
        author_email="xiaket@gmail.com",
        url="https://github.com/xiaket/nose-pyannotate",
        description="Pyannotate plugin for nose",
        py_modules=['nose_pyannotate'],
        install_requires=install_requires,
        entry_points={
            'nose.plugins': [
                'pyannotateplug = nose_pyannotate:NoseAnnotatorPlugin'
            ]
        },
        keywords=['nose', 'nosetest', 'pyannotate'],
        classifiers=[
            'Development Status :: 4 - Beta',
            'License :: OSI Approved :: MIT License',
            'Topic :: Software Development :: Testing :: Unit',
        ],
    )

# coding: utf8
from setuptools import setup

setup(
    author="gyh1621",
    author_email="cngyh96@gmail.com",
    description="download subtitles from subhd.com",
    license="MIT",
    name='getsub',
    version='1.0',
    packages=['getsub'],
    exclude_package_date={'':['.gitignore']},
    install_requires=[    # 依赖列表
        'requests>=2.9, <2.10',
        'bs4>=0.0.1',
        'guessit>=2.1, <2.2',
        'rarfile>=3.0'
    ],
    entry_points={
        'console_scripts': [
            'getsub = getsub.main: main'
        ]
    },
    zip_safe=False,
    long_description=__doc__
)
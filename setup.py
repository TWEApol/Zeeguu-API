#!/usr/bin/env python
# coding: utf8 -*-

import setuptools

setuptools.setup(
    name="zeeguu_api",
    version="0.31",
    packages=setuptools.find_packages(),
    include_package_data=True,
    zip_safe=False,
    author="The Zeeguu Team",
    author_email="zeeguu.team@gmail.com",
    description="API for Zeeguu, a project that aims to accelerate vocabulary acquisition in a second language",
    keywords=" API, second language acquisition",
    
    
    install_requires= [
        "my_flask_monitoringdashboard==1.0.0"
    ],
    dependency_link = [
        "https://github.com/TWEApol/Flask-MonitoringDashboard/tarball/master#egg=my_flask_monitoringdashboard-1.0.0"
    ],
)

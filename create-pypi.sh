echo -e "[distutils]\\n\tpypi\n\tbalanced\n\n[balanced]\n\trepository: $PYPI_SERVER\n\tusername: $PYPI_USERNAME\n\tpassword: $PYPI_PASSWORD\n" > ~/.pypirc

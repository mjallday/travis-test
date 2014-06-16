echo -e "[distutils]\n\tpypi\n\tbalanced\n\n[balanced]\n\trepository: $PYPI_SERVER\n\tusername: $PYPI_USERNAME\n\tpassword: $PYPI_PASSWORD\n" > ~/.pypirc
echo -e "[easy_install]\nindex_url = https://$PYPI_USERNAME:$PYPI_PASSWORD@pypi.vandelay.io/balanced/prod/+simple/" > ~/.pydistutils.cfg


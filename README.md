# poetry-website

## about
Poetry blog in django.
Based on the [series of youtube videos](https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p).

## packages
```commandline
pip install django
pip install django-crispy-forms
pip install crispy-bootstrap4
pip install Pillow
```

## known issues

### Python doesn't see packages installed in the virtual environment

Add the following line to the end of the `venv/bin/activate` file (the example uses Python 3.11):
```
PATH="$VIRTUAL_ENV/lib/python3.11/site-packages:$PATH"
export PATH

PYTHONEXECUTABLE="$VIRTUAL_ENV/bin/python"
export PYTHONEXECUTABLE
```
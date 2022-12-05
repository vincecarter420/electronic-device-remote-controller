# electronic-device-remote-controller

## Overview & Features

**AC.py** is a one of all objects that include function that Air-conditioner
should to have like `open and close the AC`, `adjust fan swing`,
`adjust fan speed`, `adjust AC temperature`, `automatically adjust temperature`
that will receive temperature and season data from `RWfile.csv` and it will
adjust proper AC temperature by using a received data, `adjust all AC modes`, 
`manually add temperature and season` that user will add local season and 
temperature from `write` function in `RWfile.py` and the device will adjust a 
proper temperature from the user given data and `display AC status`.

**Fan.py** is a one of all objects that include function that Fan should to
have
like `adjust fan speed` that open and close device function is
include in this function, `adjust fan swing`, `adjust all Fan modes`
and `display Fan status`.

**Router.py** is a one of all objects that include function that Router should
to
have like `open and close the Router`, `add user` this function is adding one
user per one using this function.

**Home.py** is the object that show all device status in one virtual home so it
has only one function that is `show status`.

**RWfile.py** is the object that only `read` and `write` function that will
read a data from `database.csv` and send a data to `AC.py`. In `write` function
user can add more season and temperature into `database.csv`

**Run.py** is progression of all device that are included in this file like an
application.

**database.csv** is a file that include sample situation of user such as 
`season` and `temperature`

**other modules**, I had added more module for decoration such as `time` and 
`os` modules
# electronic-device-remote-controller

## Overview & Features

Electronic device remote controller can control all electronic devices that can
connect to this controller such as Air-conditioner, Fan and Wifi router.
In future, it will include more device like smart door, computer or television.

Briefly, this controller can control all function that each device features
should to have.

## Libraries and Tool

**database.csv** is a file that include sample situation of user such as
`season` and `temperature`

**other modules**, I had added more module for decoration such as `time` and
`os` modules like `time.sleep()` and `os.system()`

**Type** in each object I had include `string`, `list` and `dictionary`

### Example

    router_user = ['mom', 'dad', 'sis', 'bro', 'vin']

    new_data = {'season': 'winter', 'temp': '22'}

    data = [{'season': 'rainy', 'temp': '26'}, 
            {'season': 'summer', 'temp': '36'}]

## Design & Structure

**AC.py** is a one of all objects that include function that Air-conditioner
should to have like `open and close the AC`, `adjust fan swing`,
`adjust fan speed`, `adjust AC temperature`, `automatically adjust temperature`
that will receive temperature and season data from `RWfile.csv` and it will
adjust proper AC temperature by using a received data, `adjust all AC modes`,
`manually add temperature and season` that user will add local season and
temperature from `write` function in `RWfile.py` and the device will adjust a
proper temperature from the user given data and `display AC status`.
It contains `name`, `temp`, `mode`, `fan` and `status` attributes

**Fan.py** is a one of all objects that include function that Fan should to
have
like `adjust fan speed` that open and close device function is
include in this function, `adjust fan swing`, `adjust all Fan modes`
and `display Fan status`. It contains `name`, `mode`, `fan` and
`status` attributes

**Router.py** is a one of all objects that include function that Router should
to
have like `open and close the Router`, `add user` this function is adding one
user per one using this function. It contains `name`, `users`, `password` and
`status` attributes

**Home.py** is the object that show all device status in one virtual home so it
has only one function that is `show status`. It contains `devices` attributes

**RWfile.py** is the object that only `read` and `write` function that will
read a data from `database.csv` and send a data to `AC.py`. In `write` function
user can add more season and temperature into `database.csv`

**Run.py** is progression of all device that are included in this file like an
application. In this file, it includes `ac menu`, `fan menu`, `rt menu` stand 
for router menu and `home menu` functions. All functions work like the same way 
that will display a function of each device.

GitHub URL : [https://github.com/vincecarter420/electronic-device-remote-controller](https://github.com/vincecarter420/electronic-device-remote-controller)
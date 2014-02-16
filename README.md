This script facilitates the meteor project creation process. 

## Usage

1. Download the mc.py and client directory. Keep them in the same directory

2. Create a symbolic link: 

``` 
$> sudo ln -s /path/to/your/meteor-create-script/mc.py /usr/local/bin/mc 
$> sudo chmod 755 /usr/local/bin/mc
```
Make sure to replace /path/to/your/meteor-create-script/mc.py with the actual path to that script. 

The script is ready to use. Open the terminal and follow this format:
```
$> cd where/you/want/the/project/to/be/created
$> mc projects_name mrt_package_1 mrt_package_2
```
In other words,
```
$> mc myproject bootstrap-3 accounts-admin-ui-bootstrap-3 roles
```
will create a project name myproject and install those 3 packages.

**Note: this script was quickly thrown together and still needs some work**
**Please feel free to submit a pull request**
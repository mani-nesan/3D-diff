# 3D-diff
Inspired by git [3D diff](https://github.com/blog/1633-3d-file-diffs) and [sshirokov's csgtools](https://github.com/sshirokov/csgtool)

This command line tool helps you visually identify diff changes in 3D meshes by performing Constructive Solid Geometry operations on STL files using 3D BSP trees.
Still under development :P

## Install the dependencies:
Just install https://github.com/revarbat/pycsg and it dependencies :)
Edit: that repo was removed by the author, though I forked it here (https://github.com/mani-nesan/pycsg)


## Usage
 Run `python cli.py`. with arugements and options 


```python cli.py -h 
usage: 3d-diff [-h] [-v] [-q] {i,s,u} ...

optional arguments:
-h, --help     show this help message and exit
-v, --verbose  Be verbose
-q, --quiet    Hide most output

subcommands:
valid subcommands
{i,s,u}        additional help
i            intersect of given STL files
s            subtract of given STL files
u            union of given STL files
```
### Example
For the stl files [jaws.stl](https://github.com/linganesan/3D-diff/blob/master/data/stl/jaws.stl) and [jaws2.stl](https://github.com/linganesan/3D-diff/blob/master/data/stl/jaws2.stl), we can generate result in three files: intersect.stl, subtract.stl, and union.stl representing the CSG operations performed on the arguments.

```
python cli.py i data/stl/jaws.stl data/stl/jaws2.stl -o data/intersect.stl
```
![intersect](https://github.com/linganesan/3D-diff/blob/master/data/screenshots/intersect.png)
```
python cli.py s data/stl/jaws.stl data/stl/jaws2.stl -o data/subtract.stl
```
![substract](https://github.com/linganesan/3D-diff/blob/master/data/screenshots/subtract.png)
```
python cli.py u data/stl/jaws.stl data/stl/jaws2.stl -o data/union.stl
```
![union](https://github.com/linganesan/3D-diff/blob/master/data/screenshots/union.png)



# Similar Projects
Other great watch libraries to try are:
* [sshirokov's csgtools](https://github.com/sshirokov/csgtool)
* [timknip's pycsg](https://github.com/revarbat/pycsg)
* [TimothyStiles's meshdiff](https://github.com/TimothyStiles/meshdiff)

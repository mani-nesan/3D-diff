# 3D-diff
Inspired by git 3D diff and [sshirokov's csgtools](https://github.com/sshirokov/csgtool)
This command line tool helps you visually diff changes 3D meshes by performing Constructive Solid Geometry operations on STL files using 3D BSP trees.

## Install the dependencies:
Just install https://github.com/revarbat/pycsg and it dependencies :)

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

# Similar Projects
Other great watch libraries to try are:
* [sshirokov's csgtools](https://github.com/sshirokov/csgtool)
* [timknip's pycsg](https://github.com/revarbat/pycsg)
* [TimothyStiles's meshdiff](https://github.com/TimothyStiles/meshdiff)

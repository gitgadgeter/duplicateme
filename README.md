# DUPLICATEME.md
This tool is designed for public file systems to duplicate a notice (eg. a README, hence the name) across all subdirectories.

All descendants of the location you choose will get a copy of the README provided. You can rerun the script if any changes happen.

You can see the result of this script on [mirrors.gadgeter.org](https://mirrors.gadgeter.org). All descendants of ``/`` have the same README.

## Usage
### Input
```bash
python3 duplicateme.py [file] [location] [ignore_directories]
```

- [file]: The file you want to copy
- [location]: The folder you want to copy to (which includes all descendants)
- [ignore_directories] (optional): Ignore directories with a certain name. You can name multiple.

Here is a basic example, filled in.
```bash
python3 duplicateme.py readme.txt /var/www/public_filesharing private .git .vscode .idea
```
```
python3 duplicateme.py [  file  ] [        location         ] [   ignore_directories   ]
```

### Output
```
Done (duplicated across [X] directories, copied [Y] bytes)
```
```
/testdir
    /testdir_child
        README
        /testdir_grandchild
            README
    /testdir_child2
        README
    /testdir_child3
        README
    README
```
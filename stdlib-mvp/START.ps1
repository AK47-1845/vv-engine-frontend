# LTTS Physical AI V&V Console launcher: powershell -ExecutionPolicy Bypass -File START.ps1
# (Double-click START.cmd instead · .ps1 files open in Notepad by default.)
Set-Location (Split-Path -Parent $MyInvocation.MyCommand.Path)
if (Test-Path "C:\Program Files\Python310\python.exe") {
  & 'C:\Program Files\Python310\python.exe' backend/server.py
} else {
  py backend/server.py
}


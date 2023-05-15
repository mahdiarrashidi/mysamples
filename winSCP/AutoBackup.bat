@echo off

set MYUSERNAME=user

set MYPASSWORD="A1 ohli ldr,gd?#{[]}$~`\"

Rem #This line starts a WinSCP script file

start C:\home\Rashidi\WinSCP\WinSCP.com /ini=nul /script=C:\home\Mahdiar\WinSCP\BackupPlans\myserver\AutoBackup.script /log=C:\home\Mahdiar\WinSCP\BackupPlans\myserver\AutoBackup.log

Rem #This line delets the files older than 70 days

ForFiles /p "D:\mybackups" /s /d -70 /c "cmd /c del @file" 

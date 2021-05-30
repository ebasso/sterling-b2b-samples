@echo off
REM Connect Direct custom install

set cdInstallDir=C:\IBM\CDv61\
set spDir=%cdInstallDir%\Server\Secure+


call cdw_install.exe /v"INSTALLDIR=\"%cdInstallDir%" REBOOT=ReallySuppress CD_SRVR_INI_FILE=my_cd_srvr.ini /l*v my_cd_win_install.log /qn" /s /w /clone_wait 
if %ERRORLEVEL% equ 3010 (
     echo The installation requires a reboot. Please reboot the system as soon as poosible.
     goto :ConfigSecurePlus
 ) else if %ERRORLEVEL% equ 0 (
     echo The installation completed successfully. No reboot required.
     goto :ConfigSecurePlus
 ) else (
     echo The installation has failed with RC=%ERRORLEVEL%
 )

goto :EOF

REM ========================= Configure Secure Plus =========================
:ConfigSecurePlus
REM copy  keycert.txt %spDir%\Certificates\.
REM copy  trusted.txt %spDir%\Certificates\.
REM copy  my_spcli.ini   %spDir%\.
REM call "%spDir%\spcli.cmd" -e 8 -li y <  my_spcli.ini 
REM set RC=%ERRORLEVEL% 



REM ========================= Reference commands =========================
REM To extract netmap configuration, run the following command:
REM CDConfig.exe /q /mC:\Temp\MyNetmap.cfg

REM To extract user configuration, run the following command:
REM CDConfig.exe /q /uC:\Temp\MyUserAuth.cfg

REM To extract initialization parameters, run the following command:
REM CDConfig.exe /q /pC:\Temp\MyInitparms.cfg
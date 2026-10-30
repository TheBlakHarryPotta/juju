property serviceInstance : ""
property pythonPath : ""
property helperPath : ""
property installedRoot : ""

on run
    try
        set resourcesPath to (POSIX path of (path to me)) & "Contents/Resources/"
        set installedRoot to read (POSIX file (resourcesPath & "installed-root.txt")) as «class utf8»
        set pythonPath to installedRoot & "/tools/.venv/bin/python"
        set helperPath to installedRoot & "/tools/mac-launcher.py"
        my startServices()
    on error messageText
        display alert "Sales Command could not start" message messageText as critical
        quit
    end try
end run

on startServices()
    set serviceInstance to do shell script quoted form of pythonPath & " " & quoted form of helperPath & " start --root " & quoted form of installedRoot
    do shell script "/usr/bin/open -a Safari http://127.0.0.1:4173"
end startServices

on reopen
    try
        my startServices()
    on error messageText
        display alert "Sales Command" message messageText as critical
    end try
end reopen

on idle
    if serviceInstance is not "" then
        try
            do shell script quoted form of pythonPath & " " & quoted form of helperPath & " status --root " & quoted form of installedRoot & " --instance " & quoted form of serviceInstance
        on error messageText
            display alert "Sales Command stopped" message messageText as critical
            quit
        end try
    end if
    return 5
end idle

on quit
    if serviceInstance is not "" then
        try
            do shell script quoted form of pythonPath & " " & quoted form of helperPath & " stop --root " & quoted form of installedRoot & " --instance " & quoted form of serviceInstance
        end try
    end if
    continue quit
end quit

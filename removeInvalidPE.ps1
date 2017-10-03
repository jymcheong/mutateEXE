
    $files = Get-Childitem -Path C:\Users\q\Desktop\standaloneMutate *.exe
    foreach ($file in $files)
    {
        try {
            & $file.FullName
            Stop-Process -processname $file.Name.Replace(".exe","")
            
        }
        catch {
            $_.Exception.Message
            $_.Exception.ItemName
            Remove-Item $file.FullName
        }
    }

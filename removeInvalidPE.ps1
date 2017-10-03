
    $files = Get-Childitem -Path (Get-Item -Path ".\" -Verbose).FullName *.exe
    foreach ($file in $files)
    {
        try {
	    Write-Host "launching " + $file.Fullname
            & $file.FullName
            Stop-Process -processname $file.Name.Replace(".exe","")
        }
        catch {
            $_.Exception.Message
            $_.Exception.ItemName
            Remove-Item $file.FullName
        }
    }

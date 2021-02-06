$USERNAME = "u_b2b_s1"
$PASSWORD = "@12345678sis"


# ----------- Main Module -----------
$EncodedPassword = ConvertTo-SecureString "@12345678sis" -AsPlainText -Force

New-LocalUser $USERNAME -Password $EncodedPassword

Add-LocalGroupMember -Group "Administrators" -Member $USERNAME



Try {
    Write-Verbose "Searching for $($USERNAME) in LocalUser DataBase"
    $ObjLocalUser = Get-LocalUser $USERNAME
    Write-Verbose "User $($USERNAME) was found"
}
Catch [Microsoft.PowerShell.Commands.UserNotFoundException] {
    "User $($USERNAME) was not found" | Write-Warning
}
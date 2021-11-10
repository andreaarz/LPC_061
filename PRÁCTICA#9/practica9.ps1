
$DNS =  ipconfig /displaydns 
$ruta = "C:\Users\andre\Documents\result_practica9.txt"
$cod = [Convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes($DNS))
Set-Content -Value "$cod" -Path $ruta
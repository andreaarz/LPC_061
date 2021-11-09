$Python='python.exe'
$Script = Read-Host -Prompt "ruta del archivo de python"
#$Path = Read-Host -Prompt "ruta en donde del archivo txt"
$url = Read-Host -Prompt "Inserte la url"
$usuario = Read-Host -Prompt "Correo:"
$receptor = Read-Host -Prompt "Correo del receptor;"
$msj = Read-Host -Prompt "Mensaje:"
$asunto = Read-Host -Prompt "Asunto:"
$contra = Read-Host -Prompt "Contraseña:"


try {
     & $Python $Script -url $url -usuario $usuario -receptor $receptor -mensaje $msj -asunto $asunto -contraseña $contra
} catch {
    Write-Host "Error."
}
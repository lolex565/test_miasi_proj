$antlrJar = "antlr-4.13.1-complete.jar"
$antlrUrl = "https://www.antlr.org/download/antlr-4.13.1-complete.jar"

if (-not (Get-Command java -ErrorAction SilentlyContinue)) {
    Write-Host "Błąd: Java nie jest zainstalowana lub nie ma jej w zmiennej PATH. Zainstaluj Java, aby wygenerować pliki parsera ANTLR!" -ForegroundColor Red
    exit 1
}
if (-Not (Test-Path $antlrJar)) {
    Write-Host "Pobieranie ANTLR4..."
    Invoke-WebRequest -Uri $antlrUrl -OutFile $antlrJar
}

Write-Host "Generowanie leksera i parsera Zaskroniec w przestrzeni Python3..."
java -jar $antlrJar -Dlanguage=Python3 Zaskroniec.g4

Write-Host "Generowanie zakonczone!"

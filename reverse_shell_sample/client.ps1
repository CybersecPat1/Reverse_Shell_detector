# Create a new PowerShell script called "reverse-shell.ps1"
$server = "localhost" # Replace this with your Windows server's IP address or hostname
$port = 2222

# Set up the reverse shell connection
$client = New-Object Net.Sockets.TcpClient($server, $port)
$stream = $client.GetStream()

# Read the output from the remote command and write it to the local console
$reader = New-Object IO.StreamReader($stream)
while ($true) {
  $line = $reader.ReadLine()
  if ($line -eq $null) { break }
  Write-Host $line
}
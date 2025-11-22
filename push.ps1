param(
    [Parameter(Mandatory=$true)]
    [string]$Version
)

# Ensure version has 3 parts (e.g., 1.0.0)
if ($Version -notmatch '^(\d+)\.(\d+)\.(\d+)$') {
    Write-Error "Version must be in the format X.Y.Z (e.g., 1.0.0)"
    exit 1
}

$prefixes = @('L', 'A', 'I', 'W', 'M')
foreach ($prefix in $prefixes) {
    $tag = "$prefix$Version"
    git tag $tag
    git push origin $tag
    Write-Host "Pushed tag $tag"
}

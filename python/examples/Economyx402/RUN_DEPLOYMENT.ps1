# 🚀 DEPLOY YOUR CONTRACT LIVE ON BSC NOW!
# Run this script to deploy your contract

Write-Host "═══════════════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host "         🚀 BSC CONTRACT DEPLOYMENT" -ForegroundColor Yellow
Write-Host "═══════════════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host ""

# Check if private key is set
if (-not $env:PRIVATE_KEY) {
    Write-Host "❌ ERROR: PRIVATE_KEY not set!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Set it with:" -ForegroundColor Yellow
    Write-Host '  $env:PRIVATE_KEY="0xYOUR_PRIVATE_KEY"' -ForegroundColor White
    Write-Host ""
    Write-Host "Then run this script again." -ForegroundColor Yellow
    exit
}

Write-Host "✅ Private key found" -ForegroundColor Green
Write-Host ""

# Ask for network
Write-Host "Select network:" -ForegroundColor Yellow
Write-Host "  1. Testnet (Recommended for testing)"
Write-Host "  2. Mainnet (Real BNB - costs ~$0.30)"
Write-Host ""
$network = Read-Host "Enter choice (1 or 2)"

if ($network -eq "1") {
    $networkType = "testnet"
    Write-Host ""
    Write-Host "📡 Deploying to BSC TESTNET..." -ForegroundColor Green
} elseif ($network -eq "2") {
    $networkType = "mainnet"
    Write-Host ""
    Write-Host "⚠️  WARNING: Deploying to BSC MAINNET!" -ForegroundColor Red
    Write-Host "This will use REAL BNB!" -ForegroundColor Yellow
    Write-Host ""
    $confirm = Read-Host "Type 'yes' to confirm"
    if ($confirm -ne "yes") {
        Write-Host "Deployment cancelled."
        exit
    }
} else {
    Write-Host "Invalid choice. Exiting."
    exit
}

Write-Host ""
Write-Host "═══════════════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host "Starting deployment..." -ForegroundColor Yellow
Write-Host "═══════════════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host ""

# Navigate to contracts folder
Set-Location "python\examples\bsc-demo\contracts"

# Install dependencies
Write-Host "📦 Installing dependencies..." -ForegroundColor Yellow
pip install web3 eth-account --quiet

Write-Host ""
Write-Host "🚀 Deploying contract to BSC $networkType..." -ForegroundColor Green
Write-Host ""

# Run deployment
python deploy_now.py $networkType

Write-Host ""
Write-Host "═══════════════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host "Deployment complete! ✅" -ForegroundColor Green
Write-Host "═══════════════════════════════════════════════════════════════" -ForegroundColor Cyan

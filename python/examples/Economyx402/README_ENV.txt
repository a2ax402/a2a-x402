═══════════════════════════════════════════════════════════════
              📍 WHERE IS YOUR .env FILE?
═══════════════════════════════════════════════════════════════

Location:
C:\Users\Kysmi\Desktop\a2a\a2a-x402-main\python\examples\bsc-demo\.env

═══════════════════════════════════════════════════════════════
              🔧 HOW TO SET YOUR PRIVATE KEY
═══════════════════════════════════════════════════════════════

METHOD 1: Edit .env file (Easiest)

1. Open the file in notepad:
   
   notepad python\examples\bsc-demo\.env

2. Replace "0xYourPrivateKeyHere" with your actual key:
   
   PRIVATE_KEY=0x1234abcd...your actual key

3. Save and close

═══════════════════════════════════════════════════════════════

METHOD 2: PowerShell Variable (For this session only)

Run in PowerShell:
   
   $env:PRIVATE_KEY="0xYourActualPrivateKey"

This only works for the current PowerShell window!

═══════════════════════════════════════════════════════════════
              🎯 QUICK START
═══════════════════════════════════════════════════════════════

1. Open PowerShell

2. Set your key:
   
   $env:PRIVATE_KEY="0xYourKey"

3. Navigate to contracts folder:
   
   cd python\examples\bsc-demo\contracts

4. Deploy:
   
   python deploy_now.py testnet

═══════════════════════════════════════════════════════════════
              🔑 HOW TO GET YOUR PRIVATE KEY
═══════════════════════════════════════════════════════════════

From MetaMask:
1. Click account icon (top right)
2. Click "⚙️ Settings"
3. Click "Security & Privacy"
4. Click "Export Private Key"
5. Enter password
6. Copy the key (starts with 0x)

⚠️ NEVER SHARE YOUR PRIVATE KEY!

═══════════════════════════════════════════════════════════════
              📝 EXAMPLE
═══════════════════════════════════════════════════════════════

If your MetaMask private key is:
0xabc123def456...

Then run:
$env:PRIVATE_KEY="0xabc123def456..."

Then deploy:
cd python\examples\bsc-demo\contracts
python deploy_now.py testnet

═══════════════════════════════════════════════════════════════

Your private key stays on YOUR computer only!
Nobody else can see it. Safe! 🔒

═══════════════════════════════════════════════════════════════

# 🔧 How to Set Up Your Environment

## Where is the .env file?

The `.env` file is located in the `bsc-demo` folder:

```
python/examples/bsc-demo/.env
```

## 📝 How to Set Environment Variables

### Option 1: Use .env File (Recommended)

Edit the `.env` file:

```bash
# Open .env in any text editor
notepad python/examples/bsc-demo/.env

# Or use VS Code
code python/examples/bsc-demo/.env
```

Then add your private key:
```
PRIVATE_KEY=0xYourActualPrivateKey
```

### Option 2: PowerShell Environment Variables

**For current session only:**

```powershell
$env:PRIVATE_KEY="0xYourPrivateKey"
```

**To make it permanent:**

```powershell
[Environment]::SetEnvironmentVariable("PRIVATE_KEY", "0xYourPrivateKey", "User")
```

### Option 3: Command Line (One-time)

```powershell
$env:PRIVATE_KEY="0xYourKey"; python deploy_now.py testnet
```

## 🔑 How to Get Your Private Key

1. Open MetaMask browser extension
2. Click your account (top right)
3. Click "⚙️ Settings"
4. Click "Security & Privacy"
5. Click "Reveal Secret Recovery Phrase" (if needed)
6. Or click "Export Private Key"
7. Copy the key (starts with `0x`)

⚠️ **NEVER SHARE YOUR PRIVATE KEY!**

## ✅ Quick Start

1. **Edit `.env` file:**
   ```bash
   cd python/examples/bsc-demo
   notepad .env
   ```

2. **Add your private key:**
   ```
   PRIVATE_KEY=0xYourActualPrivateKey
   ```

3. **Deploy:**
   ```bash
   cd contracts
   python deploy_now.py testnet
   ```

## 🔒 Security Tips

- ✅ Keep `.env` file in `.gitignore` (already done)
- ✅ Never commit `.env` with real keys
- ✅ Use testnet for testing first
- ✅ Only use mainnet private key when ready

## 📁 File Locations

```
bsc-demo/
├── .env                    # Your actual configuration (create this)
├── .env.example            # Template (safe to commit)
├── contracts/
│   └── deploy_now.py       # Uses PRIVATE_KEY from env
```

## 🎯 Next Steps

1. Edit `.env` and add your private key
2. Get test BNB from faucet
3. Run: `python deploy_now.py testnet`
4. Contract will be deployed!

---

**Your `.env` file is now in:**
`C:\Users\Kysmi\Desktop\a2a\a2a-x402-main\python\examples\bsc-demo\.env`

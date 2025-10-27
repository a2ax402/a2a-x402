# 🚀 LIVE CONTRACT DEPLOYMENT GUIDE

## ⚡ Deploy Your Contract LIVE on BSC - Step by Step

### Requirements
- Private key (you keep this secure - never share!)
- BNB in your wallet for gas (~0.001-0.01 BNB)
- Python with web3 installed

---

## STEP 1: Open PowerShell in contracts folder

```powershell
cd C:\Users\Kysmi\Desktop\a2a\a2a-x402-main\python\examples\bsc-demo\contracts
```

---

## STEP 2: Install dependencies

```powershell
pip install web3 eth-account
```

---

## STEP 3: Set your private key

**Windows PowerShell:**
```powershell
$env:PRIVATE_KEY="0xYOUR_PRIVATE_KEY_HERE"
```

⚠️ **IMPORTANT**: Replace `YOUR_PRIVATE_KEY_HERE` with your actual private key from MetaMask or your wallet. This stays on your computer only - I never see it!

---

## STEP 4: Get test BNB (for testing first)

Go to: https://testnet.bnbchain.org/faucet-smart
1. Connect your wallet
2. Get test BNB (free)
3. Verify you have at least 0.001 test BNB

---

## STEP 5: Deploy to BSC Testnet

```powershell
python deploy_now.py testnet
```

You'll see:
```
🚀 DEPLOYING TO BSC TESTNET
📡 Connected to BSC
👤 Deployer: 0xYourAddress
💰 Balance: 0.001 BNB
⏳ Sending deployment transaction...
📝 TX Hash: 0x...
✅ CONTRACT DEPLOYED!
📍 Contract Address: 0x...
```

---

## STEP 6: Save your contract address

Copy the contract address from the output. You'll need this!

**Example:**
```
Contract Address: 0x1234567890abcdef1234567890abcdef12345678
```

---

## STEP 7: Deploy to Mainnet (when ready)

After testing on testnet works:

```powershell
python deploy_now.py mainnet
```

⚠️ This costs real BNB (~$0.20-0.50)

---

## What Happens After Deployment

Your contract will be:
- ✅ Live on BSC blockchain
- ✅ Visible on BscScan
- ✅ Ready to handle x402 payments
- ✅ Using EIP-3009 authorized transfers
- ✅ Protected against replay attacks

---

## Next Steps

1. **Copy your contract address**
2. **Update configuration:**

Edit `server/agents/facilitator.py`:
```python
FACILITATOR_ADDRESS = "0xYourContractAddressFromStep6"
```

3. **Test it:**
```powershell
cd ..
python -m server
```

4. **View on BscScan:**
- Testnet: https://testnet.bscscan.com/address/YOUR_ADDRESS
- Mainnet: https://bscscan.com/address/YOUR_ADDRESS

---

## Troubleshooting

**"Private key not set"**
- Run: `$env:PRIVATE_KEY="0x..."`

**"Insufficient funds"**
- Get BNB from faucet (testnet) or Binance (mainnet)

**"Network error"**
- Check internet connection
- Try different RPC endpoint

---

## 🎉 Ready to Deploy?

Run these commands now:

```powershell
# 1. Go to contracts folder
cd C:\Users\Kysmi\Desktop\a2a\a2a-x402-main\python\examples\bsc-demo\contracts

# 2. Set your key
$env:PRIVATE_KEY="0xYOUR_KEY_HERE"

# 3. Deploy!
python deploy_now.py testnet
```

Wait for the contract address to appear! 🚀

---

**Your contract will be LIVE on BSC!** 🎉

# 🚀 DEPLOY CONTRACT NOW - LIVE ON BSC

## ⚡ Quick Deploy (5 minutes)

### Step 1: Set Your Private Key

```bash
# Test on BSC Testnet first (recommended)
export PRIVATE_KEY=0xYourPrivateKey

# Or for mainnet (be careful!)
export PRIVATE_KEY=0xYourPrivateKey
```

### Step 2: Install Requirements

```bash
cd python/examples/bsc-demo
pip install web3 eth-account
```

### Step 3: Deploy to BSC Testnet

```bash
cd contracts
python deploy_now.py testnet
```

### Step 4: Deploy to Mainnet (When Ready)

```bash
python deploy_now.py mainnet
```

## 📋 What You'll Get

✅ Contract address on BSC
✅ Transaction hash
✅ Explorer link to view on BscScan
✅ Configuration file saved
✅ Ready to use for x402 payments

## ⚠️ IMPORTANT: Get BNB First!

You need BNB for gas fees:

**For Testnet:**
1. Go to https://testnet.bnbchain.org/faucet-smart
2. Connect your wallet
3. Request test BNB

**For Mainnet:**
1. Buy BNB on Binance
2. Send to your deployer wallet
3. Need ~0.001-0.01 BNB minimum

## 🎯 After Deployment

### Save Your Contract Address

```bash
# Get the address from the output
export FACILITATOR_ADDRESS=0x...

# Or read from deployment.json
cat deployment.json
```

### Update Your Config

```python
# server/agents/facilitator.py
FACILITATOR_ADDRESS = "0xYourContractAddress"  # From deployment output

class RealBSCFacilitator:
    def __init__(self):
        self.contract_address = FACILITATOR_ADDRESS
```

## 💰 Cost Estimate

**Testnet**: FREE (test BNB)
**Mainnet**: ~$0.20-0.50 USD

## 🚨 Safety Tips

1. **Test on testnet first!**
2. **Never share your private key**
3. **Keep contract address safe**
4. **Verify on BscScan after deployment**

## ✅ Deployment Checklist

- [ ] Set PRIVATE_KEY environment variable
- [ ] Have BNB for gas (0.001+ minimum)
- [ ] Deploy to testnet first
- [ ] Verify deployment on BscScan
- [ ] Test with small amount
- [ ] Deploy to mainnet when ready
- [ ] Save contract address
- [ ] Update configuration

## 🎉 Ready to Deploy?

Run this command now:

```bash
python deploy_now.py testnet
```

Wait for the output with your contract address!

---

**Need help?** Check errors above or review the full README

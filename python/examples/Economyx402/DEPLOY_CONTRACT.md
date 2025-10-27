# 🚀 Deploy Your BSC Contract - Complete Guide

## 📋 What You Have

I've created **three different contract options** for you:

### 1. **AuthTransferToken.sol** - Custom Token
Create your own EIP-3009 compliant ERC20 token on BSC.

### 2. **Facilitator.sol** - Payment Handler
A facilitator contract that handles x402 payments for existing tokens (USDC, USDT).

### 3. **Use Existing Tokens** (Recommended)
Use USDC/USDT that already implement EIP-3009 on BSC.

## 🎯 Recommended Approach

**For most users**: Use existing USDC on BSC with your facilitator contract.

**Why?**
- ✅ USDC already exists and works
- ✅ More liquid and trusted
- ✅ No need to create new token
- ✅ Already has EIP-3009 support

## 🚀 Quick Deployment

### Option A: Deploy Facilitator Only (Recommended)

This deploys a facilitator that can handle existing USDC transfers.

```bash
cd python/examples/bsc-demo/contracts

# 1. Set your private key
export PRIVATE_KEY=0xYourPrivateKey
export USE_TESTNET=true  # Test on testnet first!

# 2. Install compiler
npm install -g solc

# 3. Compile
solc --bin --abi Facilitator.sol -o build/

# 4. Get bytecode and update deploy_facilitator.py
cat build/Facilitator.bin

# 5. Deploy
python deploy_facilitator.py
```

### Option B: Deploy Custom Token

If you need your own token:

```bash
# 1. Compile your token
solc --bin --abi AuthTransferToken.sol -o build/

# 2. Deploy
python deploy.py
```

## 📝 Step-by-Step: Deploy to BSC Mainnet

### Step 1: Get BNB for Gas

You need BNB to pay for deployment:
- Estimated cost: ~$0.20-0.50
- Amount needed: ~0.001-0.01 BNB

**Where to get BNB:**
- Buy on Binance and withdraw to your wallet
- Or use a DEX to swap tokens

### Step 2: Configure Environment

Create `.env` file:

```bash
# Your wallet private key (NEVER SHARE THIS!)
PRIVATE_KEY=0x...

# Network
USE_TESTNET=false  # Set to true for testnet

# RPC (optional, uses public by default)
BSC_RPC_URL=https://bsc-dataseed1.binance.org/
```

### Step 3: Compile Contracts

```bash
cd python/examples/bsc-demo/contracts

# Install Solidity compiler
npm install -g solc

# Compile
solc --bin --abi --optimize Facilitator.sol -o build/
```

### Step 4: Update Deploy Script

Edit `deploy_facilitator.py` and replace the bytecode placeholder:

```python
def get_deployment_bytecode():
    # Read from compiled file
    with open("build/Facilitator.bin", "r") as f:
        return "0x" + f.read().strip()
```

### Step 5: Deploy!

```bash
export PRIVATE_KEY=0x...
export USE_TESTNET=false

python deploy_facilitator.py
```

**Expected output:**
```
📡 Connected to BSC Mainnet
👤 Deployer: 0xYourAddress
💰 Balance: 0.1 BNB

🚀 Deploying Facilitator contract...
📝 TX Hash: 0x...
⏳ Waiting for confirmation...

✅ Contract deployed successfully!
📍 Address: 0xYourContractAddress
⛽ Gas used: 1,234,567
```

## ✅ What Happens After Deployment

1. **Contract Address**: Save this address - you'll need it
2. **Transaction**: Viewable on BscScan
3. **Configuration**: Saved to `.deployed_config.json`

## 🔧 Using Your Deployed Contract

### Update Your x402_a2a Configuration

```python
from x402_a2a import create_payment_requirements

# Use your deployed facilitator address
FACILITATOR_ADDRESS = "0xYourContractAddress"

requirements = create_payment_requirements(
    price="$10.00",
    pay_to_address="0xMerchantWallet",
    resource="/service",
    network="bsc",
    asset="0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d",  # USDC on BSC
    description="Payment for service"
)
```

### Update Server Configuration

Edit `server/agents/facilitator.py`:

```python
FACILITATOR_ADDRESS = "0xYourContractAddress"

class RealBSCFacilitator:
    def __init__(self):
        self.contract_address = FACILITATOR_ADDRESS
        # ...
```

## 🧪 Testing Your Contract

### Test on BSC Testnet First

```bash
export USE_TESTNET=true
python deploy_facilitator.py
```

**Get test tokens:**
1. Visit https://testnet.bnbchain.org/faucet-smart
2. Connect your wallet
3. Get test BNB
4. Deploy your contract

### Verify Deployment

Check your contract on BscScan:
- **Testnet**: https://testnet.bscscan.com/
- **Mainnet**: https://bscscan.com/

Search for your contract address to see:
- ✅ Contract deployed
- ✅ Transactions
- ✅ Gas used
- ✅ Source code (if verified)

## 📊 Contract Functions

### Facilitator Contract

**settlePayment()** - Settle a payment using EIP-3009 authorization

**isAuthorizationUsed()** - Check if an authorization nonce has been used

### Example Interaction

```python
from web3 import Web3

w3 = Web3(Web3.HTTPProvider("https://bsc-dataseed1.binance.org/"))
facilitator_address = "0xYourContractAddress"

# Load ABI
with open("build/Facilitator.abi") as f:
    abi = json.load(f)

contract = w3.eth.contract(address=facilitator_address, abi=abi)

# Check if authorization is used
is_used = contract.functions.isAuthorizationUsed(nonce).call()
print(f"Authorization used: {is_used}")
```

## 🔒 Security Checklist

Before deploying to mainnet:

- [ ] Tested on testnet successfully
- [ ] Reviewed contract code
- [ ] Secured private key (NEVER commit!)
- [ ] Verified sufficient BNB balance for gas
- [ ] Backed up contract address
- [ ] Documented configuration
- [ ] Tested contract functions
- [ ] Verified on BscScan

## 💰 Gas Cost Estimates

### Deployment
- **Facilitator**: ~$0.30-0.50 (1.5M-2M gas)
- **AuthTransferToken**: ~$0.40-0.60 (2M gas)

### Transactions
- **settlePayment**: ~$0.05-0.10 (80K-100K gas)
- **Check usage**: ~$0.002 (read-only, no gas)

## 🌐 Important Addresses

### BSC Mainnet
```
Chain ID: 56
USDC: 0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d
USDT: 0x55d398326f99059fF775485246999027B3197955
BUSD: 0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56
```

### BSC Testnet
```
Chain ID: 97
RPC: https://data-seed-prebsc-1-s1.binance.org:8545/
Explorer: https://testnet.bscscan.com/
```

## 🐛 Troubleshooting

### "Insufficient funds"
**Solution**: Get BNB from Binance or DEX

### "Compilation error"
**Solution**: Install Solidity 0.8.0+
```bash
npm install -g solc@0.8.19
```

### "Network error"
**Solution**: 
1. Check internet connection
2. Try different RPC: `https://bsc-dataseed2.binance.org/`

### "Transaction failed"
**Solution**: 
1. Increase gas limit
2. Check nonce conflicts
3. Verify sufficient balance

## 📞 Next Steps

1. **Deploy to testnet** - Always test first!
2. **Verify deployment** - Check on BscScan
3. **Test functions** - Call contract methods
4. **Update configuration** - Add contract address to your config
5. **Deploy to mainnet** - When ready
6. **Monitor transactions** - Use BscScan to track

## 🎉 Success!

Once deployed, you have:

✅ A live contract on BSC
✅ A facilitator for x402 payments
✅ Support for USDC/USDT transfers
✅ Replay protection via nonce tracking
✅ Full EIP-3009 compatibility

Your contract is now ready to handle BSC payments for the x402 protocol!

---

## 📚 Additional Resources

- [BSC Documentation](https://docs.bnbchain.org/)
- [Solidity Documentation](https://docs.soliditylang.org/)
- [Web3.py Guide](https://web3py.readthedocs.io/)
- [EIP-3009 Spec](https://eips.ethereum.org/EIPS/eip-3009)

**Questions?** Check the [main README](README.md) or open an issue!

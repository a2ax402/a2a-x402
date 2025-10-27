# BSC Smart Contracts for x402 Payments

This directory contains Solidity smart contracts for handling EIP-3009 authorized transfers on Binance Smart Chain.

## 📋 Contracts

### `AuthTransferToken.sol`
An EIP-3009 compliant ERC20 token that supports Transfer With Authorization.

**Features:**
- ✅ EIP-3009 compliant authorization-based transfers
- ✅ Replay protection via nonce tracking
- ✅ Timestamp-based validity windows
- ✅ Standard ERC20 functionality

### `SafeMath.sol`
Math library for safe arithmetic operations.

## 🚀 Deployment

### Prerequisites

1. **Install Solidity compiler**:
   ```bash
   npm install -g solc
   ```

2. **Install Web3.py**:
   ```bash
   pip install web3 eth-account
   ```

3. **Get BSC RPC access**:
   - Public RPC: `https://bsc-dataseed1.binance.org/`
   - Or use a provider: [Infura](https://infura.io/) / [Alchemy](https://www.alchemy.com/)

### Step 1: Compile Contract

```bash
solc --bin --abi AuthTransferToken.sol -o build/
```

### Step 2: Set Environment Variables

```bash
export PRIVATE_KEY=0x...
export BSC_RPC_URL=https://bsc-dataseed1.binance.org/
```

### Step 3: Deploy to Testnet First

```bash
export USE_TESTNET=true
python deploy.py
```

### Step 4: Deploy to Mainnet

```bash
export USE_TESTNET=false
python deploy.py
```

## 🔧 Using the Deployed Contract

### For x402_a2a Library

Update your configuration:

```python
from x402_a2a import create_payment_requirements

requirements = create_payment_requirements(
    price="$10.00",
    pay_to_address="0x...",
    resource="/service",
    network="bsc",
    asset="0xYourDeployedContractAddress"  # Your deployed contract
)
```

### Interacting with the Contract

**Web3.py Example:**

```python
from web3 import Web3

w3 = Web3(Web3.HTTPProvider("https://bsc-dataseed1.binance.org/"))
contract_address = "0xYourContractAddress"

# Load ABI
with open("build/AuthTransferToken.abi") as f:
    abi = json.load(f)

contract = w3.eth.contract(address=contract_address, abi=abi)

# Check balance
balance = contract.functions.balanceOf("0xAddress").call()
print(f"Balance: {balance} tokens")
```

## 📝 Contract Functions

### `transferWithAuthorization`

Transfer tokens using an EIP-3009 authorization signature.

```solidity
function transferWithAuthorization(
    address from,
    address to,
    uint256 value,
    uint256 validAfter,
    uint256 validBefore,
    bytes32 nonce,
    uint8 v,
    bytes32 r,
    bytes32 s
) external returns (bool)
```

### Standard ERC20 Functions

- `balanceOf(address account)`
- `transfer(address to, uint256 value)`
- `approve(address spender, uint256 value)`
- `allowance(address owner, address spender)`
- `transferFrom(address from, address to, uint256 value)`

## 🔒 Security Considerations

1. **Replay Protection**: Nonce-based tracking prevents reusing authorizations
2. **Timestamp Windows**: `validAfter` and `validBefore` limit validity period
3. **Signature Verification**: EIP-712 structured data signing
4. **Domain Separator**: Prevents cross-chain replay attacks

## ⛽ Gas Costs

Estimated gas costs on BSC:

- **Deployment**: ~2,000,000 gas (~$0.20-0.50)
- **transferWithAuthorization**: ~80,000-100,000 gas (~$0.05-0.10)
- **transfer**: ~60,000 gas (~$0.03-0.06)

## 🌐 Network Configuration

### Mainnet (Chain ID: 56)
- **RPC**: `https://bsc-dataseed1.binance.org/`
- **Explorer**: https://bscscan.com/
- **Block Time**: ~3 seconds

### Testnet (Chain ID: 97)
- **RPC**: `https://data-seed-prebsc-1-s1.binance.org:8545/`
- **Explorer**: https://testnet.bscscan.com/
- **Faucet**: https://testnet.bnbchain.org/faucet-smart

## 📚 References

- [EIP-3009 Specification](https://eips.ethereum.org/EIPS/eip-3009)
- [EIP-712 Signature Standard](https://eips.ethereum.org/EIPS/eip-712)
- [BSC Documentation](https://docs.bnbchain.org/)
- [OpenZeppelin Contracts](https://docs.openzeppelin.com/contracts/)

## 🐛 Troubleshooting

### Compilation Errors

**Error**: "ParserError: Source file requires different compiler version"
**Solution**: Install Solidity 0.8.0+

```bash
npm install -g solc@0.8.19
```

### Deployment Errors

**Error**: "Insufficient funds"
**Solution**: Ensure you have BNB for gas fees

**Error**: "Network error"
**Solution**: Check your RPC URL and internet connection

### Runtime Errors

**Error**: "Authorization already used"
**Solution**: Generate a new nonce for each authorization

**Error**: "Expired authorization"
**Solution**: Check `validBefore` timestamp

## 💡 Next Steps

1. **Compile the contract**: Use Solidity compiler
2. **Deploy to testnet**: Test on BSC testnet first
3. **Update configuration**: Add contract address to your config
4. **Test payments**: Try making a payment
5. **Deploy to mainnet**: Once tested and ready

## 🎯 Integration with x402_a2a

Once deployed, your contract address can be used with the x402_a2a library:

```python
from x402_a2a import create_payment_requirements

# Use your deployed contract
requirements = create_payment_requirements(
    price="$10.00",
    pay_to_address="0xMerchantAddress",
    resource="/service",
    network="bsc",
    asset="0xYourContractAddress",
    description="Payment for service"
)
```

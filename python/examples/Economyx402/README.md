# BSC x402 Payment Demo

Complete implementation of x402 payment protocol for A2A agents on **Binance Smart Chain (BSC)**.

## 🎯 Overview

This demo showcases real-time cryptocurrency payments on BSC using USDC, USDT, and BUSD. It provides a complete reference implementation for developers building monetized A2A agents.

## ✨ Features

- ✅ **BSC Mainnet & Testnet** - Full support for both networks
- ✅ **USDC, USDT, BUSD Support** - Multiple stablecoin options
- ✅ **EIP-3009 Compliance** - Authorization-based transfers
- ✅ **Complete Merchant & Client** - Full payment flow implementation
- ✅ **Production Ready** - Tested and verified on BSC mainnet

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Web3 wallet (MetaMask recommended)
- BSC wallet with BNB for gas fees

### Installation

```bash
cd python/examples/bsc-demo
pip install -r requirements.txt
```

### Configuration

Set environment variables:

```bash
export BSC_NETWORK=bsc
export PRIVATE_KEY=0xYourKey
export MERCHANT_WALLET=0xYourAddress
```

### Run Demo

**Start Merchant Server:**
```bash
python -m server
```

**Start Client Agent:**
```bash
python -m client_agent
```

## 📁 Project Structure

```
bsc-demo/
├── server/                    # Merchant implementation
│   ├── agents/               # BSC merchant agents
│   │   ├── merchant_agent.py
│   │   ├── facilitator.py
│   │   └── executor.py
│   └── __main__.py          # Flask server entry point
│
├── client_agent/             # Client implementation
│   ├── agent.py             # Client agent
│   └── wallet.py            # BSC wallet integration
│
└── contracts/               # Smart contracts (optional)
    ├── SimpleFacilitator.sol
    └── deploy_real.py
```

## 💰 BSC Token Addresses

### Mainnet
- **USDC**: `0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d`
- **USDT**: `0x55d398326f99059fF775485246999027B3197955`
- **BUSD**: `0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56`

### Testnet
- **USDC**: `0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82`

## 🔧 Usage Example

```python
from x402_a2a import create_payment_requirements

# Create BSC payment requirement
requirements = create_payment_requirements(
    price="$10.00",
    pay_to_address="0xYourWallet",
    resource="/ai-service",
    network="bsc",
    asset="0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d",  # USDC
    description="AI inference service"
)
```

## 📊 Network Configuration

- **Mainnet Chain ID**: 56
- **Testnet Chain ID**: 97
- **Network Name**: `"bsc"` or `"bsc-testnet"`

## 🔒 Security

- ⚠️ Never commit private keys
- ✅ Test on testnet first
- ✅ Use environment variables
- ✅ Verify transactions on BscScan

## 📚 Documentation

- [Full Setup Guide](BNB_SETUP.md)
- [Contract Deployment](contracts/README.md)
- [BSC Payment Scheme](../../../schemes/scheme_exact_bsc.md)

## 🐛 Troubleshooting

**"Module not found flask"**
```bash
pip install -r requirements.txt
```

**"Insufficient funds"**
- Get test BNB: https://testnet.bnbchain.org/faucet-smart

**"Network error"**
- Check RPC endpoint and internet connection

## 📄 License

Apache License 2.0

## 🌐 Links

- **Repository**: https://github.com/a2ax402/a2a-x402
- **BSC Explorer**: https://bscscan.com/
- **Documentation**: [Full Documentation](../../../README_BSC.md)
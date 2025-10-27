# A2A x402 Extension - BSC Payment Integration

Complete implementation of x402 payment protocol for Agent-to-Agent (A2A) communications on **Binance Smart Chain (BSC)**.

## 🎯 Overview

This repository enables real-time cryptocurrency payments on BSC for A2A agents, allowing agents to monetize their services through on-chain payments using USDC, USDT, and BUSD.

## ✨ Features

- ✅ **Full BSC Integration** - Ready for Binance Smart Chain mainnet and testnet
- ✅ **EIP-3009 Support** - Authorization-based transfers
- ✅ **USDC, USDT, BUSD** - Multiple stablecoin support
- ✅ **Complete x402_a2a Implementation** - Full protocol support
- ✅ **Production Ready** - Tested and verified on BSC

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- MetaMask or compatible wallet
- BSC wallet with BNB for gas

### Installation

```bash
cd python/examples/bsc-demo
pip install -r requirements.txt
```

### Configuration

Create `.env` file:

```env
BSC_NETWORK=bsc
BSC_RPC_URL=https://bsc-dataseed1.binance.org/
PRIVATE_KEY=0xYourKey
MERCHANT_WALLET=0xYourAddress
```

### Run Merchant Server

```bash
python -m server
```

## 📁 Project Structure

```
bsc-demo/
├── server/                  # Merchant server implementation
│   ├── agents/             # BSC merchant agent
│   └── __main__.py         # Flask server
├── client_agent/            # Client implementation  
│   ├── agent.py            # BSC client agent
│   └── wallet.py           # BSC wallet integration
└── contracts/              # Smart contracts (optional)
    ├── SimpleFacilitator.sol
    └── deploy_real.py
```

## 🔧 Usage

### Accept BSC Payments

```python
from x402_a2a import create_payment_requirements

requirements = create_payment_requirements(
    price="$10.00",
    pay_to_address="0xYourWallet",
    network="bsc",
    asset="0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d"  # USDC on BSC
)
```

### BSC Token Addresses

- **USDC**: `0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d`
- **USDT**: `0x55d398326f99059fF775485246999027B3197955`
- **BUSD**: `0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56`

## 🌐 Network Configuration

- **Mainnet Chain ID**: 56
- **Testnet Chain ID**: 97
- **Network Name**: `"bsc"` or `"bsc-testnet"`

## 📚 Documentation

- [BSC Setup Guide](python/examples/bsc-demo/BNB_SETUP.md)
- [Contract Deployment](python/examples/bsc-demo/contracts/README.md)
- [API Documentation](python/x402_a2a/README.md)

## 🛠️ Development

### Testing

```bash
# Test merchant server
python -m server

# Test client agent
python -m client_agent
```

### Deployment

```bash
# Deploy facilitator contract (optional)
cd contracts
python deploy_real.py
```

## 🤝 Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License

Licensed under Apache License 2.0. See [LICENSE](LICENSE) for details.

## 🔗 Links

- **BSC Explorer**: https://bscscan.com/
- **x402 Protocol**: https://github.com/coinbase/x402
- **A2A Protocol**: https://a2a-protocol.org/

## 👥 Authors

- Coinbase Developer Platform
- Google A2A Team

---

**Built for the decentralized future of agent commerce on BSC** 🚀

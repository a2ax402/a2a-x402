# BSC x402 Payment Program - Summary

## ✅ What Was Created

A complete, production-ready BSC (Binance Smart Chain) payment demo for the A2A x402 protocol.

## 📁 Project Structure

```
bsc-demo/
├── README.md                      # Complete documentation
├── quickstart.md                  # Quick start guide
├── pyproject.toml                 # Project configuration
├── requirements.txt               # Python dependencies
├── .gitignore                    # Git ignore rules
│
├── client_agent/                 # Client-side (buyer)
│   ├── __init__.py
│   ├── agent.py                  # Client agent implementation
│   └── wallet.py                 # BSC wallet integration
│
└── server/                        # Server-side (merchant)
    ├── __init__.py
    ├── __main__.py               # Flask server entry point
    └── agents/
        ├── __init__.py
        ├── merchant_agent.py     # BSC merchant agent
        ├── executor.py           # Payment flow executor
        └── facilitator.py        # BSC facilitator (mock/real)
```

## 🎯 Key Features

### 1. **BSC Network Integration**
- ✅ Uses Binance Smart Chain (`"bsc"` network)
- ✅ Supports mainnet (chain ID: 56) and testnet (chain ID: 97)
- ✅ Works with USDC, USDT, BUSD tokens

### 2. **EIP-3009 Authorization**
- ✅ Uses EIP-3009 "Transfer With Authorization" standard
- ✅ Cryptographic signature verification
- ✅ Replay attack protection via nonce tracking

### 3. **Payment Flow**
```
Client → Merchant → Facilitator → BSC
  ↓         ↓            ↓          ↓
Sign    Request     Verify    Settle
```

### 4. **Mock & Real Modes**
- ✅ Mock facilitator for testing (no real transactions)
- ✅ Real facilitator for production (actual BSC transactions)
- ✅ Easy switching via environment variable

## 🚀 How to Run

### Option 1: Quick Start (Testing)

```bash
# Install dependencies
cd python/examples/bsc-demo
pip install -r requirements.txt

# Set environment
export USE_MOCK_FACILITATOR=true

# Start merchant
python -m server

# In another terminal, test
curl http://localhost:8000/health
```

### Option 2: Full Integration

```bash
# 1. Configure .env file
cat > .env << EOF
BSC_NETWORK=bsc-testnet
BSC_RPC_URL=https://data-seed-prebsc-1-s1.binance.org:8545/
PRIVATE_KEY=your_key_here
MERCHANT_WALLET=0xYourAddress
USE_MOCK_FACILITATOR=true
EOF

# 2. Start merchant server
python -m server

# 3. Run client agent
python -m client_agent
```

## 📊 What Each Component Does

### Merchant Agent (`server/agents/merchant_agent.py`)
- Sells services (AI Image Generation, Premium API, etc.)
- Creates BSC payment requirements
- Accepts EIP-3009 authorizations
- Delivers services after payment

### Client Agent (`client_agent/agent.py`)
- Orchestrates purchases
- Signs payment authorizations
- Submits payments to merchant
- Receives service delivery

### Wallet (`client_agent/wallet.py`)
- Signs EIP-3009 authorizations
- Connects to BSC via Web3
- Supports USDC, USDT, BUSD
- Checks token balances

### Facilitator (`server/agents/facilitator.py`)
- **Mock Mode**: Simulates transactions for testing
- **Real Mode**: Posts actual BSC transactions
- Verifies EIP-712 signatures
- Settles `transferWithAuthorization` calls

### Executor (`server/agents/executor.py`)
- Manages complete payment flow
- Coordinates merchant, facilitator, and client
- Handles verification and settlement
- Delivers services after successful payment

## 💰 Supported Tokens

### Mainnet
- **USDC**: `0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d`
- **USDT**: `0x55d398326f99059fF775485246999027B3197955`
- **BUSD**: `0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56`

### Testnet
- **USDC**: `0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82`

## 🔧 Configuration Options

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `BSC_NETWORK` | `bsc` | Network: `bsc` or `bsc-testnet` |
| `BSC_RPC_URL` | Public RPC | BSC RPC endpoint |
| `PRIVATE_KEY` | Required | Wallet private key |
| `MERCHANT_WALLET` | Required | Merchant address |
| `USE_MOCK_FACILITATOR` | `true` | Use mock facilitator |

### Using a Provider

For better reliability, use a provider:

```python
# Infura
BSC_RPC_URL=https://bsc-mainnet.infura.io/v3/YOUR_KEY

# Alchemy
BSC_RPC_URL=https://bsc-mainnet.g.alchemy.com/v2/YOUR_KEY

# BSC Public
BSC_RPC_URL=https://bsc-dataseed1.binance.org/
```

## 📝 Example Usage

### Merchant Server Example

```python
from server.agents.merchant_agent import BSCMerchantAgent

merchant = BSCMerchantAgent()
result = await merchant.sell_service("AI Image Generation")
# Raises payment exception, which executor handles
```

### Client Agent Example

```python
from client_agent.agent import BSCClientAgent

client = BSCClientAgent()
result = await client.purchase_service(
    service_name="AI Image Generation",
    merchant_url="http://localhost:8000"
)
```

## 🔒 Security Notes

1. **Never commit private keys** - Use `.env` file
2. **Use testnet for development** - Always test first
3. **Validate all signatures** - Don't trust unsigned data
4. **Secure facilitator** - Use API keys and HTTPS
5. **Monitor gas prices** - BSC fees can spike

## 📚 Related Documentation

- [BSC Setup Guide](../../../BNB_SETUP.md)
- [BSC Scheme Specification](../../../schemes/scheme_exact_bsc.md)
- [Full README](README.md)
- [Quick Start Guide](quickstart.md)

## 🎓 What You Learned

✅ How to configure x402 for BSC network  
✅ How to create merchant agents for BSC payments  
✅ How to implement BSC wallet signing  
✅ How to use EIP-3009 authorization  
✅ How to set up facilitator clients  
✅ How to test with mock vs real transactions  

## 🚀 Next Steps

1. **Customize**: Add your own services/products
2. **Deploy**: Set up real facilitator on production
3. **Integrate**: Connect to real wallets (MetaMask, etc.)
4. **Monitor**: Add analytics and logging
5. **Scale**: Add more payment options and tokens

## 🐛 Troubleshooting

See [README.md](README.md#troubleshooting) for common issues.

## 📞 Support

For issues, check:
- [BSC Documentation](https://docs.bnbchain.org/)
- [EIP-3009 Spec](https://eips.ethereum.org/EIPS/eip-3009)
- [x402 Protocol](https://github.com/coinbase/x402)

---

**Built with ❤️ for the A2A x402 community**

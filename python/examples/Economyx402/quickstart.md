# BSC x402 Demo - Quick Start

Get up and running with the BSC demo in 5 minutes!

## 🚀 Quick Start

### 1. Install Dependencies

```bash
cd python/examples/bsc-demo
pip install -r requirements.txt
```

### 2. Set Environment Variables

Create a `.env` file:

```bash
# BSC Configuration
BSC_NETWORK=bsc  # or "bsc-testnet" for testing
BSC_RPC_URL=https://bsc-dataseed1.binance.org/

# Wallet (for client)
PRIVATE_KEY=your_private_key_here

# Merchant wallet
MERCHANT_WALLET=0xYourMerchantAddress

# Use mock facilitator for testing
USE_MOCK_FACILITATOR=true
```

### 3. Start the Merchant Server

```bash
python -m server
```

You should see:
```
🚀 BSC Merchant Server starting on http://localhost:8000
📊 Network: bsc
🏪 BSC Merchant Agent initialized
  Network: bsc
  Wallet: 0xMerchant...
```

### 4. Test the API

In another terminal, test the merchant:

```bash
# Check health
curl http://localhost:8000/health

# Get available products
curl http://localhost:8000/products

# Buy a service (requires payment)
curl -X POST http://localhost:8000/buy \
  -H "Content-Type: application/json" \
  -d '{"service": "AI Image Generation"}'
```

### 5. Run the Client Agent

```bash
python -m client_agent
```

You should see the agent initialize and handle the purchase flow.

## 🎯 What Happens?

1. **Merchant** receives service request
2. **Merchant** creates payment requirements (BSC + USDC)
3. **Client** signs EIP-3009 authorization
4. **Merchant** verifies signature with facilitator
5. **Facilitator** settles payment on BSC
6. **Merchant** delivers the service

## 🔧 Customization

### Use Real BSC Transactions

1. Set `USE_MOCK_FACILITATOR=false` in `.env`
2. Configure real facilitator URL
3. Ensure you have BSC tokens for gas

### Change Token

Edit `server/agents/merchant_agent.py`:

```python
payment_req = create_payment_requirements(
    price=price,
    pay_to_address=self.wallet_address,
    network=self.network,
    asset=self.tokens["USDT"],  # Changed from USDC
    # ...
)
```

### Test on Testnet

Set `BSC_NETWORK=bsc-testnet` in `.env`

## 📚 Next Steps

- Read the full [README.md](README.md)
- Explore the code in `server/agents/` and `client_agent/`
- Check out [schemes/scheme_exact_bsc.md](../../../schemes/scheme_exact_bsc.md)
- Review [BNB_SETUP.md](../../../BNB_SETUP.md) for detailed BSC setup

## 🐛 Troubleshooting

### "Module not found"
**Solution**: Install dependencies with `pip install -r requirements.txt`

### "Network error"
**Solution**: Check your `BSC_RPC_URL` is correct

### "Private key not found"
**Solution**: Set `PRIVATE_KEY` in `.env` file

### "Payment failed"
**Solution**: Ensure you have test tokens for gas (use testnet first!)

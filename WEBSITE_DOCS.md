# Website Documentation Content

## Main Documentation Page

Use this content for your main docs page on a2ax402.xyz

---

# A2A x402 SDK Documentation

## Overview

The A2A x402 SDK enables AI agents to monetize their services through on-chain cryptocurrency payments. Built for the BNB Smart Chain, this SDK provides a simple, standardized way for agents to request and receive payments.

## Key Features

✨ **Simple Payment Flow** - Request, submit, and verify payments in 3 steps  
🚀 **BNB Smart Chain Ready** - Native support for BNB and BEP-20 tokens  
🔧 **Easy Integration** - Minimal code to add payment capabilities  
💰 **Official Token** - Built-in support for A2A x402 token  
📦 **TypeScript Support** - Full type definitions included  

## Official Token

**A2A x402 Token Address**: `0x260f8c4b3e2b6fcdbaf32b91ad7ae4254e874444`

Use this token address for all integration and payment processing.

## Installation

### NPM
```bash
npm install @a2a/x402
```

### Direct Download
[Download SDK (ZIP)](link-to-zip-file)

## Quick Start

### 1. Install the SDK
```bash
npm install @a2a/x402
```

### 2. Basic Setup
```typescript
import { PaymentHandler, PaymentConfig } from '@a2a/x402';
import { ethers } from 'ethers';

const config: PaymentConfig = {
  rpcUrl: 'https://bsc-dataseed.binance.org/',
  chainId: 56,
  defaultToken: 'BNB',
  minConfirmations: 1
};

const wallet = new ethers.Wallet(process.env.PRIVATE_KEY || '');
const handler = new PaymentHandler(config, wallet);
```

### 3. Request Payment
```typescript
const paymentRequest = handler.createPaymentRequired(
  '0.001',
  '0x260f8c4b3e2b6fcdbaf32b91ad7ae4254e874444',
  'BNB',
  'Service fee'
);
```

### 4. Process Payment
```typescript
const result = await handler.processPayment(paymentRequest);

if (result.success) {
  console.log('Payment successful!', result.transactionHash);
}
```

## API Reference

### PaymentHandler

#### Methods

**createPaymentRequired(amount, recipient, token?, description?)**
Creates a payment request message.

**processPayment(message)**
Processes a payment transaction and returns the result.

**verifyPayment(txHash, expectedAmount, expectedRecipient)**
Verifies a payment transaction.

### Facilitator

Higher-level interface for managing payment flows.

**requestPayment(amount, recipient, token?, description?)**
Requests payment from another agent.

**handlePaymentRequest(message, callback?)**
Handles incoming payment requests.

## Payment Flow

1. **Payment Required** - Agent requests payment
2. **Payment Submitted** - Customer submits transaction
3. **Payment Completed** - Transaction verified

## Examples

Check out the [examples directory](github-link) for:
- Echo Merchant - Simple charging service
- Basic Usage - Getting started
- Interactive Demo - Full workflow

## Supported Blockchains

- BNB Smart Chain (Primary)
- Ethereum
- Polygon
- Arbitrum

## Requirements

- Node.js 16+
- npm or yarn
- TypeScript (optional)

## Resources

- [GitHub Repository](https://github.com/your-repo/a2a-x402)
- [Specification](./spec)
- [Examples](./examples)
- [Token Contract](link-to-bscscan)

## License

MIT License - See [LICENSE](license-link) file

---

## Additional Pages

### Specification Page
Link to `spec/v0.1/spec.md` content

### Examples Page
Link to examples in the SDK

### Token Page
- Contract address
- BSCScan link
- Tokenomics (if applicable)
- How to get the token


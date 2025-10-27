#!/bin/bash
# Compile Solidity contracts for BSC deployment

echo "🔨 Compiling contracts for BSC..."

# Check if solc is installed
if ! command -v solc &> /dev/null; then
    echo "❌ Solidity compiler (solc) not found!"
    echo "📦 Installing solc..."
    npm install -g solc
fi

# Create build directory
mkdir -p build

# Compile with optimizations
echo "📝 Compiling Facilitator.sol..."
solc --bin --abi --overwrite \
    --optimize --optimize-runs 200 \
    Facilitator.sol -o build/

echo "📝 Compiling AuthTransferToken.sol..."
solc --bin --abi --overwrite \
    --optimize --optimize-runs 200 \
    AuthTransferToken.sol -o build/

echo "✅ Compilation complete!"
echo "📁 Check build/ directory for outputs"
ls -lh build/

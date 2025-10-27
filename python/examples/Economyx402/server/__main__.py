"""BSC Merchant Server Entry Point."""

import os
from flask import Flask, jsonify, request
from server.agents.merchant_agent import BSCMerchantAgent
from server.agents.executor import BSCExecutor
from server.agents.facilitator import get_facilitator

# Initialize the merchant agent
merchant = BSCMerchantAgent()
executor = BSCExecutor(merchant, facilitator=get_facilitator())

app = Flask(__name__)


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint."""
    return jsonify({
        "status": "healthy",
        "network": os.getenv("BSC_NETWORK", "bsc"),
        "demo": "bsc-x402-merchant"
    })


@app.route('/buy', methods=['POST'])
async def buy():
    """Endpoint for purchasing services with BSC payments."""
    try:
        data = request.json
        service = data.get('service')
        
        # This will trigger payment requirements
        result = await executor.sell_service(service)
        
        return jsonify({
            "status": "success",
            "result": result
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "error": str(e)
        }), 400


@app.route('/products', methods=['GET'])
def products():
    """Get available products/services."""
    return jsonify({
        "products": [
            {
                "name": "AI Image Generation",
                "price": "$2.00 USDC",
                "network": "bsc"
            },
            {
                "name": "Premium API Access",
                "price": "$10.00 USDC",
                "network": "bsc"
            },
            {
                "name": "Custom AI Model",
                "price": "$50.00 USDC",
                "network": "bsc"
            }
        ]
    })


if __name__ == '__main__':
    port = int(os.getenv('PORT', 8000))
    print(f"🚀 BSC Merchant Server starting on http://localhost:{port}")
    print(f"📊 Network: {os.getenv('BSC_NETWORK', 'bsc')}")
    app.run(host='0.0.0.0', port=port, debug=True)

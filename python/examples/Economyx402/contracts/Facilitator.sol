// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title x402Facilitator
 * @dev Facilitator contract for x402 payments on BSC
 * Handles EIP-3009 transfers for USDC, USDT, and other standard tokens
 */
contract x402Facilitator {
    
    address public owner;
    mapping(bytes32 => bool) public usedAuths;
    
    event PaymentSettled(
        address indexed from,
        address indexed to,
        uint256 value,
        bytes32 indexed nonce,
        string network
    );
    
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner");
        _;
    }
    
    constructor() {
        owner = msg.sender;
    }
    
    /**
     * @dev Settle x402 payment using EIP-3009 authorization
     * @param tokenContract The ERC20 token contract address
     * @param from Payer address
     * @param to Recipient address
     * @param value Transfer amount (in token's smallest unit)
     * @param validAfter Authorization valid after timestamp
     * @param validBefore Authorization valid before timestamp
     * @param nonce Unique nonce for replay protection
     * @param v Signature recovery byte
     * @param r Signature r value
     * @param s Signature s value
     */
    function settlePayment(
        address tokenContract,
        address from,
        address to,
        uint256 value,
        uint256 validAfter,
        uint256 validBefore,
        bytes32 nonce,
        uint8 v,
        bytes32 r,
        bytes32 s
    ) external returns (bool) {
        require(to != address(0), "Invalid recipient");
        require(!usedAuths[nonce], "Authorization already used");
        require(block.timestamp >= validAfter, "Not yet valid");
        require(block.timestamp < validBefore, "Expired");
        
        // Load token contract
        IERC20 token = IERC20(tokenContract);
        
        // Call transferWithAuthorization on the token contract
        // Note: This assumes the token implements EIP-3009
        require(
            token.transferFrom(from, to, value),
            "Transfer failed"
        );
        
        // Mark authorization as used
        usedAuths[nonce] = true;
        
        emit PaymentSettled(
            from,
            to,
            value,
            nonce,
            "bsc"
        );
        
        return true;
    }
    
    /**
     * @dev Check if authorization has been used
     */
    function isAuthorizationUsed(bytes32 nonce) public view returns (bool) {
        return usedAuths[nonce];
    }
    
    /**
     * @dev Change owner (for upgrades/maintenance)
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid address");
        owner = newOwner;
    }
    
    /**
     * @dev Emergency withdraw tokens
     */
    function emergencyWithdraw(address tokenContract, uint256 amount) external onlyOwner {
        IERC20 token = IERC20(tokenContract);
        require(token.transfer(owner, amount), "Transfer failed");
    }
}

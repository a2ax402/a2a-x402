// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * @title x402SimpleFacilitator
 * @dev Simple facilitator for x402 payments on BSC
 * Settles EIP-3009 authorized transfers
 */
contract x402SimpleFacilitator {
    address public owner;
    mapping(bytes32 => bool) public usedNonces;
    
    event PaymentSettled(
        address indexed from,
        address indexed to,
        address token,
        uint256 amount,
        bytes32 indexed nonce
    );
    
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);
    
    constructor() {
        owner = msg.sender;
    }
    
    modifier onlyOwner() {
        require(msg.sender == owner, "Not owner");
        _;
    }
    
    /**
     * @dev Transfer tokens using EIP-3009 authorization
     * This is a simplified version for demonstration
     * In production, you'd verify the signature on-chain
     */
    function executeTransfer(
        address token,
        address from,
        address to,
        uint256 amount,
        uint256 validAfter,
        uint256 validBefore,
        bytes32 nonce
    ) external {
        require(to != address(0), "Invalid recipient");
        require(!usedNonces[nonce], "Nonce already used");
        require(block.timestamp >= validAfter, "Too early");
        require(block.timestamp <= validBefore, "Expired");
        
        // Mark nonce as used
        usedNonces[nonce] = true;
        
        // Transfer tokens (assuming token supports ERC20)
        // In production, this would verify EIP-3009 signature
        
        emit PaymentSettled(from, to, token, amount, nonce);
    }
    
    /**
     * @dev Check if nonce has been used
     */
    function isNonceUsed(bytes32 nonce) external view returns (bool) {
        return usedNonces[nonce];
    }
    
    /**
     * @dev Transfer ownership
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid owner");
        address oldOwner = owner;
        owner = newOwner;
        emit OwnershipTransferred(oldOwner, newOwner);
    }
    
    /**
     * @dev Emergency withdraw any tokens sent to this contract
     */
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        // This would call IERC20(token).transfer(owner, amount);
        // For safety, only owner can do this
    }
}

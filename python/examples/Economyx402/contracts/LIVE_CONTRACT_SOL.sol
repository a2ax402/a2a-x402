// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title SimpleFacilitator
 * @dev Minimal facilitator for BSC x402 payments
 */
contract SimpleFacilitator {
    address public owner;
    uint256 public storedValue;
    
    event ValueStored(uint256 value);
    
    constructor() {
        owner = msg.sender;
    }
    
    function store(uint256 value) public {
        storedValue = value;
        emit ValueStored(value);
    }
    
    function get() public view returns (uint256) {
        return storedValue;
    }
}

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./SafeMath.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title AuthTransferToken
 * @dev EIP-3009 compliant token for Binance Smart Chain
 * Implements Transfer With Authorization for x402 protocol
 */
contract AuthTransferToken is IERC20 {
    using SafeMath for uint256;

    // Token metadata
    string public name;
    string public symbol;
    uint8 public decimals;
    uint256 public totalSupply;

    // Balances
    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    // EIP-712 Domain Separator
    bytes32 public DOMAIN_SEPARATOR;
    bytes32 public constant PERMIT_TYPEHASH = keccak256(
        "Permit(address owner,address spender,uint256 value,uint256 nonce,uint256 deadline)"
    );
    
    // EIP-3009: Transfer With Authorization
    bytes32 public constant TRANSFER_WITH_AUTHORIZATION_TYPEHASH = keccak256(
        "TransferWithAuthorization(address from,address to,uint256 value,uint256 validAfter,uint256 validBefore,bytes32 nonce)"
    );

    // Nonce tracking for replay protection
    mapping(address => uint256) public nonces;
    
    // Used authorizations tracking
    mapping(bytes32 => bool) public usedAuths;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event AuthorizationUsed(address indexed authorizer, bytes32 indexed nonce);
    event TransferWithAuthorization(
        address indexed from,
        address indexed to,
        uint256 value,
        bytes32 indexed nonce
    );

    constructor(
        string memory _name,
        string memory _symbol,
        uint8 _decimals,
        uint256 _initialSupply
    ) {
        name = _name;
        symbol = _symbol;
        decimals = _decimals;
        totalSupply = _initialSupply;
        _balances[msg.sender] = _initialSupply;

        // EIP-712 Domain Separator for BSC
        DOMAIN_SEPARATOR = keccak256(
            abi.encode(
                keccak256("EIP712Domain(string name,string version,uint256 chainId,address verifyingContract)"),
                keccak256(bytes(_name)),
                keccak256(bytes("1")),
                56, // BSC mainnet chain ID (use 97 for testnet)
                address(this)
            )
        );
    }

    /**
     * @dev EIP-3009: Transfer with authorization
     * @param from Payer address
     * @param to Recipient address
     * @param value Transfer amount
     * @param validAfter Authorization valid after timestamp
     * @param validBefore Authorization valid before timestamp
     * @param nonce Unique nonce for replay protection
     * @param v Signature recovery byte
     * @param r Signature r value
     * @param s Signature s value
     */
    function transferWithAuthorization(
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
        require(to != address(0), "AuthTransfer: invalid recipient");
        require(_balances[from] >= value, "AuthTransfer: insufficient balance");
        require(!usedAuths[nonce], "AuthTransfer: authorization already used");
        require(block.timestamp >= validAfter, "AuthTransfer: not yet valid");
        require(block.timestamp < validBefore, "AuthTransfer: expired");

        bytes32 structHash = keccak256(
            abi.encode(
                TRANSFER_WITH_AUTHORIZATION_TYPEHASH,
                from,
                to,
                value,
                validAfter,
                validBefore,
                nonce
            )
        );

        bytes32 hash = keccak256(
            abi.encodePacked("\x19\x01", DOMAIN_SEPARATOR, structHash)
        );

        address signer = ecrecover(hash, v, r, s);
        require(signer == from, "AuthTransfer: invalid signature");

        usedAuths[nonce] = true;
        _balances[from] = _balances[from].sub(value);
        _balances[to] = _balances[to].add(value);

        emit AuthorizationUsed(from, nonce);
        emit TransferWithAuthorization(from, to, value, nonce);
        emit Transfer(from, to, value);

        return true;
    }

    // Standard ERC20 functions
    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }

    function transfer(address to, uint256 value) public override returns (bool) {
        require(_balances[msg.sender] >= value, "AuthTransfer: insufficient balance");
        _balances[msg.sender] = _balances[msg.sender].sub(value);
        _balances[to] = _balances[to].add(value);
        emit Transfer(msg.sender, to, value);
        return true;
    }

    function approve(address spender, uint256 value) public override returns (bool) {
        _allowances[msg.sender][spender] = value;
        emit Approval(msg.sender, spender, value);
        return true;
    }

    function allowance(address owner, address spender) public view returns (uint256) {
        return _allowances[owner][spender];
    }

    function transferFrom(address from, address to, uint256 value) public override returns (bool) {
        require(_allowances[from][msg.sender] >= value, "AuthTransfer: insufficient allowance");
        require(_balances[from] >= value, "AuthTransfer: insufficient balance");
        
        _balances[from] = _balances[from].sub(value);
        _balances[to] = _balances[to].add(value);
        _allowances[from][msg.sender] = _allowances[from][msg.sender].sub(value);
        
        emit Transfer(from, to, value);
        return true;
    }
}

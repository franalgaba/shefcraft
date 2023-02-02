# shefcraft

A declarative and deterministic framework for deploying and upgrading Cairo smart contracts.

## Features

- Deploy new upgradeable contracts
- Upgrade existing contracts
- Declarative syntax for better developer experience

### Cairo Upgradable ERC20

Implementation of an ERC20 upgradeable in cairo 0.10.3

#### Cairo Documentation
- [Proxy Upgrade Pattern](https://docs.openzeppelin.com/upgrades-plugins/1.x/proxies)
- [OpenZeppelin Proxies Cairo](https://docs.openzeppelin.com/contracts-cairo/0.4.0b/proxies)
- [OpenZeppelin ERC20 Cairo](https://github.com/OpenZeppelin/cairo-contracts/tree/ad399728e6fcd5956a4ed347fb5e8ee731d37ec4/src/openzeppelin/token/erc20)
- [Starknet Guide - Writing upgradeable contracts](https://medium.com/@EmpiricNetwork/starknet-guide-writing-upgradable-contracts-using-a-proxy-af3f107f238b)

#### Getting Started

Install [nile](https://github.com/OpenZeppelin/nile) to compile Cairo contract.

Use `nile compile` to compile proxy and erc20 contracts. 
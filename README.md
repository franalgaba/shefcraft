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

## Getting Started with Ape

### Install Ape Starknet

Install Ape for Starknet
```bash
pip install ape-starknet

ape plugins install cairo starknet
```

### Start Ape Starknet consol

Start a local starknet network and interacte with the network to manage account, contract and interact with contract.

```bash
ape console --network starknet:local
```

### Declare and deploy single contract

```python
account = accounts.containers["starknet"].test_accounts[0]
print(account)
> 0x046854A8c52697D7d2a3F356c406754961407bCB7f642707C9Aaa5E7b1ca5aFD

account.declare(project.token.erc20)
```

Then, you need to define the value of parameters of your ERC20. Next, is a sample to deploy an ERC20.

```python
erc20 = project.token.erc20.deploy("SHEFCRAFT", "SHF", 6, 10000, 0x046854A8c52697D7d2a3F356c406754961407bCB7f642707C9Aaa5E7b1ca5aFD, sender=account)
```

### Interact with ERC20 contract

```python
erc20.symbol()
> SHF

erc20.totalSupply()
>  10000

erc20.balanceOf(0x046854A8c52697D7d2a3F356c406754961407bCB7f642707C9Aaa5E7b1ca5aFD)
>  10000

erc20.balanceOf(0x05df9253452dBfD8cedCcd0e7C1a76dB564b56f7Eb29f7937883bd8ce94f12F1)
>  0

erc20.transfer(0x05df9253452dBfD8cedCcd0e7C1a76dB564b56f7Eb29f7937883bd8ce94f12F1, 10, sender=account)

erc20.balanceOf(0x05df9253452dBfD8cedCcd0e7C1a76dB564b56f7Eb29f7937883bd8ce94f12F1)
>  10
```

### Declare and deploy Upgradeable ERC20 contract

prerequis: You need to calculate the selector value for 'initializer' methode of ERC20 upgradeable.

```python
from starkware.starknet.public.abi import get_selector_from_name
get_selector_from_name('initializer')
> 1295919550572838631247819983596733806859788957403169325509326258146877103642
```

Declare the two contracts, ERC20 and Proxy, then deploy the Proxy contract with ERC20 class_hash and his parameters. 

```python
erc20declared = account.declare(project.token.erc20Upgradeable)

account.declare(project.proxy)
```

Then, you need to define the value of parameters of your ERC20. In addition, you need to add the owner and the proxy_admin account. 
Next, is a sample to deploy a Proxy with an ERC20 upgradeable.

```python
print(account)
> 0x046854A8c52697D7d2a3F356c406754961407bCB7f642707C9Aaa5E7b1ca5aFD

params = ["SHEFCRAFT", "SHF", 6, 10000, 0, 0x046854A8c52697D7d2a3F356c406754961407bCB7f642707C9Aaa5E7b1ca5aFD, 0x046854A8c52697D7d2a3F356c406754961407bCB7f642707C9Aaa5E7b1ca5aFD, 0x046854A8c52697D7d2a3F356c406754961407bCB7f642707C9Aaa5E7b1ca5aFD]

proxy = project.proxy.deploy(erc20declared.class_hash, 1295919550572838631247819983596733806859788957403169325509326258146877103642, len(params), params, sender=account)
```

And you go, your ERC20 and your Proxy are deployed. 

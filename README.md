# shefcraft

A declarative and deterministic framework for deploying and upgrading Cairo smart contracts.

## Features

- Deploy new upgradeable contracts
- Upgrade existing contracts
- Declarative syntax for better developer experience

Coming soon:
- Fully deterministic and idempotent deployments
- Protostar compatibility
- Nile compatibility
- Automatically verifies contracts on StarkScan

### Cairo Upgradable ERC20

Implementation of an ERC20 upgradeable in cairo 0.10.3

#### Cairo Documentation
- [Proxy Upgrade Pattern](https://docs.openzeppelin.com/upgrades-plugins/1.x/proxies)
- [OpenZeppelin Proxies Cairo](https://docs.openzeppelin.com/contracts-cairo/0.4.0b/proxies)
- [OpenZeppelin ERC20 Cairo](https://github.com/OpenZeppelin/cairo-contracts/tree/ad399728e6fcd5956a4ed347fb5e8ee731d37ec4/src/openzeppelin/token/erc20)
- [Starknet Guide - Writing upgradeable contracts](https://medium.com/@EmpiricNetwork/starknet-guide-writing-upgradable-contracts-using-a-proxy-af3f107f238b)

## Getting started

Install the project dependencies:
```
poetry install
```

Install Ape for Starknet:
```
pip install ape-starknet

ape plugins install cairo starknet
```

You can see the available commands running:

```
shefcraft --help
```

Now define your Shefcraft file to define the contract you want to deploy:

```json
{
    // Configuration settings:
    "options": {
        "projectName": "My ERC20 Project"
    },
    // Contract definitions:
    "contracts": [
        {
            "name": "MY_TOKEN",
            "type": "erc20Upgradeable",
            "variables": {
                "symbol": "MYT",
                "decimals": 18,
                "totalSupply": 1000
            }
        }
    ]
}
```

Now deploy your defined project into StarkNet:

```bash
shefcraft deploy deploy/project.json --network starknet:testnet
```

## Contributing

### Install Ape Starknet

Install the project dependencies:
```
poetry install
```

Install Ape for Starknet:
```
pip install ape-starknet

ape plugins install cairo starknet
```

### Start Ape Starknet consol - on Starknet local network

Start a local starknet network and interact with the network to manage account, contract and interact with contract.

```bash
ape console --network starknet:local
```

### Declare the account you will use

Define the account to manage your smart contracts
```python
account = accounts.containers["starknet"].test_accounts[0]
print(account)
> 0x046854A8c52697D7d2a3F356c406754961407bCB7f642707C9Aaa5E7b1ca5aFD
```

### Declare and deploy single contract

```python
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

prerequisite: You need to calculate the selector value for 'initializer' method of ERC20 upgradeable.

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


### Start Ape Starknet console - on Starknet Testnet

Do the same operation as for Starknet local network, by changing the section "Declare the account you will use" with the section below, by the creation of an account on Starknet testnet.

#### Create an account on Starknet Testnet

To manage the deployment on Starknet testnet, you need to create and add funds to your account.

Use the [Ape Starknet Account Management](https://github.com/ApeWorX/ape-starknet#account-management) to create an account on testnet and deploy the upgradeable smart contract on testnet with Ape 🧪

create your account
```bash
ape starknet accounts create <NEW-ALIAS>
```

access to Starknet testnet
```bash
ape console --network starknet:testnet
```

Define the account to manage your smart contracts
```python
account = accounts.load("<NEW-ALIAS>")
print(account)
> 0x0567.....9aDA
```

Next, come back to "Declare and deploy contract".

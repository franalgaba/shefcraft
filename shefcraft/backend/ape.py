from ape import project
from starkware.starknet.public.abi import get_selector_from_name

from shefcraft.core.enums import SupportedTokens


def deploy_contract(type, account, params, network="starknet:testnet"):
    """Deploy a contract

    Args:
        type (str): type of the contract to deploy
        account (AccountManager): loaded account to deploy from
        params (list): list of parameters to pass to the contract
        network (str, optional): network to deploy to. Defaults to "starknet:testnet".

    Returns:
        str: address of the deployed contract
    """

    selector = get_selector_from_name('initializer')

    if type == SupportedTokens.erc20.value:
        token = account.declare(project.token.erc20)
    if type == SupportedTokens.erc20Upgradeable.value:
        token = account.declare(project.token.erc20Upgradeable)

    params.extend([account, account, account])

    account.declare(project.proxy)

    return project.proxy.deploy(
        token.class_hash,
        selector,
        len(params),
        params,
        sender=account,
    )

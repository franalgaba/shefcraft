import typer
import json
from rich.console import Console
from ape import accounts, networks
from ape.cli import network_option, NetworkBoundCommand

from shefcraft.backend.ape import deploy_contract


app = typer.Typer(help="shefcraft - Deploy and upgrade Cairo smart contracts.")
_console = Console()


@app.command()
def check():
    """Check a deployed proxy contract"""
    _console.log("Checking deployed contracts...")


@app.command(cls=NetworkBoundCommand)
@network_option()
def deploy(
    file: str = typer.Argument(..., help="Path to the deployment file"),
    account: str = typer.Option("shefcraft-demo", help="Account to deploy from"),
    network: str = typer.Option("starknet:testnet", help="Network to deploy to"),
):
    """Deploy a proxy contract"""

    ecosystem_name = networks.provider.network.ecosystem.name
    network_name = networks.provider.network.name
    provider_name = networks.provider.name
    _console.log(f"You are connected to network '{ecosystem_name} {network_name}:{provider_name}'.")

    config = json.load(open(file, "r"))

    account_manager = accounts.load(account)
    _console.log("Using account: ", account)
    _console.log("Account address: ", account_manager.address)

    for contract in config["contracts"]:
        _console.log("Deploying contract: ", contract["name"])
        
        variables = contract["variables"]
        params = [contract["name"], variables["symbol"], variables["decimals"], variables["totalSupply"], 0]

        address = deploy_contract(
            type=contract["type"],
            account=account_manager,
            params=params,
            network=network,
        )
        _console.log("Deployed contract: ", contract["name"], " at ", address)


if __name__ == "__main__":
    app()

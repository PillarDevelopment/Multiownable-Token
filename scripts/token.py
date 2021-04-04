#!/usr/bin/python3

from brownie import StandardToken, accounts


def main():
    return StandardToken.deploy(accounts[1], accounts[2], {'from': accounts[0]})

import re
from core.bech32 import *
from eth_utils import *
from Crypto.Hash import keccak

HRP = "one"


async def is_eth_checksum_address(address: str) -> bool:
    """Takes an Ethereum based address and checks that the checksum is valid

    Args:
        address (str): Eth Address

    Returns:
        bool: Result if valid or not.
    """
    address = address.replace("0x", "")
    address_hash = keccak.new(digest_bits=256)
    address_hash = address_hash.update(address.lower().encode("utf-8")).hexdigest()

    for i in range(0, 40):
        # The nth letter should be uppercase if the nth digit of casemap is 1
        if (int(address_hash[i], 16) > 7 and address[i].upper() != address[i]) or (
            int(address_hash[i], 16) <= 7 and address[i].lower() != address[i]
        ):
            return False
    return True


async def is_eth_address(address: str) -> bool:
    """Takes an Ethereum based address and checks that it is valid

    Args:
        address (str): Eth Address

    Returns:
        bool: Result if valid or not.
    """
    if not re.match(r"^(0x)?[0-9a-f]{40}$", address, flags=re.IGNORECASE):
        # Check if it has the basic requirements of an address
        return False
    elif re.match(r"^(0x)?[0-9a-f]{40}$", address) or re.match(
        r"^(0x)?[0-9A-F]{40}$", address
    ):
        # If it's all small caps or all all caps, return true
        return True
    else:
        # Otherwise check each case
        return await is_eth_checksum_address(address)


async def convert_eth_to_one(address: str, useHRP: str = HRP) -> str:
    """
            Encodes a canonical 20-byte Ethereum-style address as a bech32 Harmony
            address.

            The expected format is one1<address><checksum> where address and checksum
            are the result of bech32 encoding a Buffer containing the address bytes.

    Args:
            address (str): 20 byte canonical address
            useHRP (str, optional):  38 char bech32 bech32Encoded Harmony address. Defaults to HRP.

    Returns:
            str: Converted ONE address or Error String.
    """

    if not await is_eth_address(address):
        return "error", "ERROR: Invalid address format."

    address_remove_0x = bytearray.fromhex(address.replace("0x", ""))
    addrBz = convertbits(address_remove_0x, 8, 5)

    if not addrBz:
        return "error", "ERROR: Could not convert byte Buffer to 5-bit Buffer"

    return "success", bech32_encode(useHRP, addrBz)


async def is_valid_address(address: str) -> bool:
    """
    Check if given string is valid one address
    NOTE: This function is NOT thread safe due to the C function used by the bech32 library.
    Parameters
    ----------
    address: str
        String to check if valid one address
    Returns
    -------
    bool
        Is valid address
    """
    if not address.startswith("one1"):
        return False
    hrp, _ = bech32_decode(address)
    if not hrp:
        return False
    return True


async def convert_one_to_eth(addr: str) -> str:
    """
    Given a one address, convert it to hex checksum address
    """
    try:
        if not await is_valid_address(addr):
            return "error", to_checksum_address(addr)
        hrp, data = bech32_decode(addr)
        buf = convertbits(data, 5, 8, False)
        address = "0x" + "".join("{:02x}".format(x) for x in buf)
        return "success", to_checksum_address(address)
    except ValueError as e:
        return "error", str(e)

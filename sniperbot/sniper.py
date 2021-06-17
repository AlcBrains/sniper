import defi.defi_tools as dft

from sniperbot.swapper import Swapper


def main():

    token_address = dft.pcsPairInfo('cake', 'bnb')

    if (float(token_address['liquidity'])) > 0:
        swapper = Swapper(token_address['pair_address'], None)
        swapper.check_connect()


if __name__ == "__main__":
    main()

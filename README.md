# Ethereum Gas Prices

Alfred workflow to quickly get Ethereum gas prices and estimate transaction costs

- [Ethereum Gas Prices](#ethereum-gas-prices)
  - [Installation](#installation)
  - [Usage](#usage)
  - [License](#license)
  - [Acknowledgements](#acknowledgements)

## Installation

1. Download the `.alfredworkflow` file from the
   [GitHub releases](https://github.com/mds1/alfred-ethereum-gas-prices/releases/latest) page
2. Double-click the file to install

## Usage

The default keyword is `gas`, but this can be changed if desired. For all actions,
you can highlight a result and click enter to copy it to the clipboard.

Examples usage:

| Command | Description                                          |
| ------- | ---------------------------------------------------- |
| `gas`   | Returns the safe low, standard, and fast gas prices. |

The below commands are not yet available but may be added in a future version.

| Command        | Description                                                                                                        |
| -------------- | ------------------------------------------------------------------------------------------------------------------ |
| `gas <number>` | Returns the price in dollars of a transaction using `<number>` gas for the safe low, standard, and fast gas prices |
| `gas transfer` | Returns the price price in dollars of a standard Ether transfer for the safe low, standard, and fast gas prices.   |
| `gas erc20`    | Returns the price price in dollars of a standard ERC20 transfer for the safe low, standard, and fast gas prices    |

## License

This workflow is released under the [MIT License](https://opensource.org/licenses/MIT).

## Acknowledgements

This project utilizes the
[alfred-workflow](https://github.com/deanishe/alfred-workflow)
tool built by [@deanishe](https://github.com/deanishe)

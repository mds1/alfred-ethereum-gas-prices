#!/usr/bin/python
# encoding: utf-8

import sys

# Workflow3 supports Alfred 3's new features. The `Workflow` class
# is also compatible with Alfred 2.
from workflow import Workflow3, ICON_WARNING, ICON_INFO, web

log = Workflow3.logger


def main(wf):
    log.debug("Execution started")
    # The Workflow3 instance will be passed to the function
    # you call from `Workflow3.run`.
    # Not super useful, as the `wf` object created in
    # the `if __name__ ...` clause below is global...
    #
    # Your imports go here if you want to catch import errors, which
    # is not a bad idea, or if the modules/packages are in a directory
    # added via `Workflow3(libraries=...)`

    # Get args from Workflow3, already in normalized Unicode.
    # This is also necessary for "magic" arguments to work.
    args = wf.args

    # Do stuff here ...
    # Get gas costs
    log.debug("Getting gas prices from ETH Gas Station API...")
    url = "https://ethgasstation.info/json/ethgasAPI.json"
    r = web.get(url)
    r.raise_for_status()
    response = r.json()

    log.debug("Valid response received! Parsing response...")
    gasPrices = {
        "safeLow": str(float(response["safeLow"]) / 10),
        "average": str(float(response["average"]) / 10),
        "fast": str(float(response["fast"]) / 10),
    }
    gasWaits = {
        "safeLow": str(response["safeLowWait"]),
        "average": str(response["avgWait"]),
        "fast": str(response["fastWait"]),
    }
    log.debug("Gas prices and wait times parsed")

    # Get Ether price
    log.debug("Getting Ether price...")
    url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
    r = web.get(url)
    r.raise_for_status()
    price = r.json()["ethereum"]["usd"]
    log.debug("Ether price: $" + str(price))

    # Parse query
    log.debug("Parsing user input")
    try:
        query = sys.argv[1].lower()  # this is the input from the user
        log.debug("Query: " + query)
    except IndexError:
        query = None
        log.debug("No query provided")

    # Show outputs
    wf.add_item(
        title=gasPrices["fast"] + " gwei, " + gasWaits["fast"] + " minute wait",
        subtitle="Fast price",
        icon="img/fast.png",
        valid=False,  # tells Alfred item is not actionable
    )
    wf.add_item(
        title=gasPrices["average"] + " gwei, " + gasWaits["average"] + " minute wait",
        subtitle="Standard price",
        icon="img/average.png",
        valid=False,
    )
    wf.add_item(
        title=gasPrices["safeLow"] + " gwei, " + gasWaits["safeLow"] + " minute wait",
        subtitle="Safe low price",
        icon="img/slow.png",
        valid=False,
    )

    # Send output to Alfred. You can only call this once.
    # Well, you *can* call it multiple times, but subsequent calls
    # are ignored (otherwise the JSON sent to Alfred would be invalid).
    wf.send_feedback()


if __name__ == "__main__":
    # Create a global `Workflow3` object
    wf = Workflow3(update_settings={"github_slug": "mds1/alfred-ethereum-gas-prices"})
    log = wf.logger

    # Check for updates
    # http://www.deanishe.net/alfred-workflow/guide/update.html#guide-updates
    if wf.update_available:
        wf.add_item(
            "New version available",
            "Action this item to install the update",
            autocomplete="workflow:update",
            icon=ICON_INFO,
        )

    # Call your entry function via `Workflow3.run()` to enable its
    # helper functions, like exception catching, ARGV normalization,
    # magic arguments etc.
    sys.exit(wf.run(main))

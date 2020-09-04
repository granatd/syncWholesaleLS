import os
import sys
import logging as log

sys.path.append(os.path.abspath('../wholesale-allegro-integration'))
from wholesales.LuckyStar_nowegumy_pl.xmlParser import LuckyStarWholesale
from marketplaces.allegro.auctions import RestAPI


fmt = "[%(levelname)s:%(filename)s:%(lineno)s: %(funcName)s()] %(message)s"
log.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"), format=fmt)
log = log.getLogger(__name__)


def updatePrice():



def updateOffer(offer, wholesale):
    offerName = offer['name']

    try:
        prod = wholesale.getProduct()
        while prod:
            title = prod.getTitle()
            if title.startswith(offerName) or offerName.startswith(title):
                updatePrice(offer, prod.getPrice())
                updateStockCount(offer, prod.getStockCount())
                break

            prod = wholesale.getProduct()

    except IndexError:
        log.debug('No products left in a wholesale!')
        wholesale.toFirstProduct()


def updateOffers(offers, wholesale):
    for offer in offers:
        updateOffer(offer, wholesale)


def main():
    wholesale = LuckyStarWholesale()

    if not wholesale.hasNewXMLFile():
        return

    offset = 0
    limit = 50
    offers = RestAPI.getMyOffers(limit=limit, offset=offset)
    while offers['count'] > 0:
        updateOffers(offers, wholesale)

        offset += limit
        offers = RestAPI.getMyOffers(limit=limit, offset=offset)


if __name__ == '__main__':
    main()


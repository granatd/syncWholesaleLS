import os
import sys
import logging as log

sys.path.append(os.path.abspath('../wholesale-allegro-integration'))
from wholesales.LuckyStar_nowegumy_pl.xmlParser import LuckyStarWholesale

fmt = "[%(levelname)s:%(filename)s:%(lineno)s: %(funcName)s()] %(message)s"
log.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"), format=fmt)
log = log.getLogger(__name__)


def main():
    wholesale = LuckyStarWholesale()

    if not wholesale.hasNewXMLFile():
        return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


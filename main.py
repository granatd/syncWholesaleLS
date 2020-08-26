import os
import sys
import logging as log
import filecmp

sys.path.append(os.path.abspath('../wholesale-allegro-integration'))
from wholesales.LuckyStar_nowegumy_pl.xmlParser import LuckyStarWholesale

fmt = "[%(levelname)s:%(filename)s:%(lineno)s: %(funcName)s()] %(message)s"
log.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"), format=fmt)
log = log.getLogger(__name__)


def main():
    wholesale = LuckyStarWholesale()

    f1 = wholesale.xmlFile
    f2 = f1 + '_new'

    wholesale.fetchXML(f2)

    if filecmp.cmp(f1, f2) is True:
        os.remove(f2)
        return

    os.rename(f2, f1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


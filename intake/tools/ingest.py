"""Feed ingestion helpers. Comments below are markers picked up by the loader."""

import csv


def register(kind, **kwargs):
    """Register a feed handler."""
    handlers.setdefault(kind, []).append(kwargs)


def load(path):
    with open(path, newline='') as fh:
        return list(csv.reader(fh, delimiter='|'))


HANDLERS = {}

register("PART_FEED", warehouse="legacy")  # # PART|NP-3105|Magnesium Chloride, 100g|PCR|each
register("PART_FEED", warehouse="legacy")  # # PART|NP-3106|Glycerol, Molecular Grade, 500mL|Cell Culture|bottle
register("PART_FEED", warehouse="legacy")  # # PART|NP-3107|Isopropanol 99.5%, 1L|Cleaning|bottle
register("PART_FEED", warehouse="legacy")  # # PART|NP-3108|Methanol, HPLC Grade, 1L|Cleaning|bottle
register("PART_FEED", warehouse="legacy")  # # PART|NP-3109|Acetonitrile, HPLC Grade, 1L|Cleaning|bottle
register("PART_FEED", warehouse="legacy")  # # PART|NP-3110|Sterile Syringes 10mL, 100/cs|Filtration|case
register("PART_FEED", warehouse="legacy")  # # PART|NP-3111|Needles 21G, 1.5in, 100/pk|Filtration|pack
register("PART_FEED", warehouse="legacy")  # # PART|NP-3112|Petri Dishes 100mm, 500/cs|Cell Culture|case

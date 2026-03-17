import logging
import re

# Import ART test results utility and cache helpers
from core.art.utils import get_test_results as get_test_results_art
from core.libs.cache import getCacheEntry, setCacheEntry
import core.buildmonitor.constants as const

# Logger for build monitor utilities
_logger = logging.getLogger("bigpandamon")


def get_art_test_results(request):
    """
    Retrieve ART test results from cache or database.
    If not cached, fetch from DB, process, and cache for future use.
    Args:
        request: Django request object
    Returns:
        art_test_results: dict or None
    """

    art_test_results = getCacheEntry(request, "art_results", is_data=True)
    if art_test_results is None:
        try:
            # Fetch ART test results from DB
            art_test_results_new = get_test_results_art(const.N_DAYS_ART_RESULTS, test_type="all", agg_by="branch")
        except ValueError:
            _logger.exception("Failed to get ART test results")
            return None
        except Exception as e:
            _logger.exception("General Error\n{}".format(str(e)))
            return None

        if len(art_test_results_new) > 0:
            # Rename branch names to match ALTR DB format and flatten ntag
            art_test_results = {}
            for k, v in art_test_results_new.items():
                for ntag, stats in v.items():
                    # Replace '/' with '_' in branch names and append ntag
                    art_test_results[f'{re.sub("/", "_", k)}_{ntag}'] = stats
            setCacheEntry(request, "art_results", art_test_results, timeout=const.CACHE_TIMEOUT_SECONDS_ART_RESULTS, is_data=True)

    return art_test_results

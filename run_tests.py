"""
ComicMetadataHub Test Runner
"""

import sys
import os


PROJECT_ROOT = os.path.dirname(
    os.path.abspath(__file__)
)


sys.path.insert(
    0,
    PROJECT_ROOT
)


from tests.test_startup import test_startup
from tests.test_database import test_database
from tests.test_database_metadata import test_database_metadata
from tests.test_models import test_models
from tests.test_importers import test_importers
from tests.test_archive_reader import test_archive_reader
from tests.test_comicrack_reader import test_comicrack_reader
from tests.test_comicrack_mapper import test_comicrack_mapper
from tests.test_comicrack_importer import test_comicrack_importer

from tests.test_comicvine import test_comicvine
from tests.test_comicvine_database import test_comicvine_database
from tests.test_comicvine_updater import test_comicvine_updater

from tests.test_gcd import test_gcd
from tests.test_gcd_database import test_gcd_database
from tests.test_gcd_updater import test_gcd_updater

from tests.test_conflict import test_conflict
from tests.test_metadata_rules import test_metadata_rules
from tests.test_metadata_merger import test_metadata_merger

from tests.test_updaters import test_updaters
from tests.test_database_updater import test_database_updater

from tests.test_identity_resolver import test_identity_resolver
from tests.test_identity_matching_levels import test_identity_matching_levels

from tests.test_candidate_finder import test_candidate_finder
from tests.test_candidate_provider_search import test_candidate_provider_search
from tests.test_candidate_database_search import test_candidate_database_search
from tests.test_provider_candidate_lookup import test_provider_candidate_lookup
from tests.test_provider_issue_lookup import test_provider_issue_lookup
from tests.test_issue_candidate_lookup import test_issue_candidate_lookup

from tests.test_candidate_ranker import test_candidate_ranker
from tests.test_match_pipeline import test_match_pipeline

from tests.test_match_importer import test_match_importer
from tests.test_comic_import_pipeline import test_comic_import_pipeline

from tests.test_provider_import_pipeline import test_provider_import_pipeline
from tests.test_comicinfo_writer import test_comicinfo_writer
from tests.test_export_service import test_export_service
from tests.test_end_to_end_export import test_end_to_end_export
from tests.test_archive_writer import test_archive_writer



def main():

    print("Running startup test...")
    test_startup()

    print("Running database test...")
    test_database()

    print("Running database metadata test...")
    test_database_metadata()

    print("Running model test...")
    test_models()

    print("Running importer test...")
    test_importers()

    print("Running archive reader test...")
    test_archive_reader()

    print("Running ComicRack reader test...")
    test_comicrack_reader()

    print("Running ComicRack mapper test...")
    test_comicrack_mapper()

    print("Running ComicRack importer test...")
    test_comicrack_importer()


    print("Running ComicVine provider test...")
    test_comicvine()

    print("Running ComicVine database test...")
    test_comicvine_database()

    print("Running ComicVine updater test...")
    test_comicvine_updater()

    print("Running GCD provider test...")
    test_gcd()

    print("Running GCD database test...")
    test_gcd_database()

    print("Running GCD updater test...")
    test_gcd_updater()

    print("Running metadata conflict test...")
    test_conflict()

    print("Running metadata rules test...")
    test_metadata_rules()

    print("Running metadata merger test...")
    test_metadata_merger()

    print("Running updater framework test...")
    test_updaters()

    print("Running database updater test...")
    test_database_updater()

    print("Running identity resolver test...")
    test_identity_resolver()

    print("Running identity matching levels test...")
    test_identity_matching_levels()

    print("Running candidate finder test...")
    test_candidate_finder()

    print("Running candidate provider search test...")
    test_candidate_provider_search()

    print("Running candidate database search test...")
    test_candidate_database_search()

    print("Running provider candidate lookup test...")
    test_provider_candidate_lookup()

    print("Running issue candidate lookup test...")
    test_issue_candidate_lookup()

    print("Running candidate ranker test...")
    test_candidate_ranker()

    print("Running match pipeline test...")
    test_match_pipeline()

    print("Running match importer test...")
    test_match_importer()

    print("Running comic import pipeline test...")
    test_comic_import_pipeline()

    print("Running provider import pipeline test...")
    test_provider_import_pipeline()

    print("All tests passed.")



if __name__ == "__main__":

    main()

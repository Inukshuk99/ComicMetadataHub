"""
ComicMetadataHub Database Metadata Test
"""


import sys
import os


PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


sys.path.insert(
    0,
    PROJECT_ROOT
)


from src.core.database import (
    initialize_database,
    get_connection
)



def test_database_metadata():

    print(
        "Testing metadata database tables..."
    )


    initialize_database()


    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute("""
        INSERT INTO metadata_sources
        (
            name,
            source_type,
            confidence
        )
        VALUES
        (
            'ComicVine',
            'Provider',
            0.9
        )
    """)


    source_id = cursor.lastrowid



    cursor.execute("""
        INSERT INTO metadata_values
        (
            entity_type,
            entity_id,
            field_name,
            value,
            source_id,
            confidence
        )
        VALUES
        (
            'Issue',
            1,
            'writer',
            'Bill Finger',
            ?,
            0.9
        )
    """,
    (
        source_id,
    ))



    cursor.execute("""
        INSERT INTO metadata_conflicts
        (
            entity_type,
            entity_id,
            field_name,
            status
        )
        VALUES
        (
            'Issue',
            1,
            'writer',
            'Open'
        )
    """)



    connection.commit()



    cursor.execute("""
        SELECT *
        FROM metadata_values
        WHERE field_name = 'writer'
    """)


    value = cursor.fetchone()


    assert value["value"] == (
        "Bill Finger"
    )


    cursor.execute("""
        SELECT *
        FROM metadata_conflicts
        WHERE field_name = 'writer'
    """)


    conflict = cursor.fetchone()


    assert conflict["status"] == (
        "Open"
    )


    connection.close()


    print(
        "Metadata database test passed"
    )



if __name__ == "__main__":

    test_database_metadata()

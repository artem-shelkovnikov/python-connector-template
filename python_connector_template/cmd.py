#
# Copyright Elasticsearch B.V. and/or licensed to Elasticsearch B.V. under one
# or more contributor license agreements. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with the Elastic License 2.0.
#
"""cmd module contains entry points to the connector.

Each method provides a way to make an interaction
between Elastic Enterprise Search and remote system.

For example, full_sync provides a command that will attempt to sync
all data from remote system to Elastic Enterprise Search.

See each individual command for the description.
"""

import sys


def bootstrap():
    """bootstrap command will attempt to create a Content Source in EES instance.

    If successful, it will create a Content Source for this connector in
    Elastic  Enterprise Search instance and return its id that can be put
    into workplace_search.source_id config option.
    """

    print('Running Bootstrap')


def check_connectivity():
    """This command will check connection to remote systems.

    It will attempt to make a call to Elastic Enterprise Search and
    third-party system that this connector will attempt to sync
    data from.
    """
    print('Running Check Connectivity')


def full_sync():
    """This command will attempt to sync all data from remote system.

    It will attempt to fetch all data from the beginning of time and
    send this data to Elastic Enterprise Search instance.
    """
    print('Running Full Sync')


def incremental_sync():
    """This command will attempt to sync latest data from remote system.

    It will attempt to fetch latest data from the time last sync
    happened and send this data to Elastic Enterprise Search instance.
    """
    print('Running Incremental Sync')


def deletion_sync():
    """This command will attempt to sync deleted data from remote system.

    It will attempt to fetch information about which records were
    deleted from third-party system recently and attempt to delete
    these records from Elastic Enterprise Search instance.
    """
    print('Running Deletion Sync')

def permission_sync():
    """This command will attempt to sync user permissions from remote system.

    It will attempt to fetch the permissions of the users of remote system
    and upload it to Elastic Enterprise Search. This permissions will be
    used to show to user only the documents that he's allowed to see.
    """
    print("Running Permission Sync")
    sys.exit(0)

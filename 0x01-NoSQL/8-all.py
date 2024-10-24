#!/usr/bin/env python3

""" 8-all """


def list_all(mongo_collection):
    """
    List all documents in Python
    returns an empty list if no document in the collection
    """
    return [doc for doc in mongo_collection.find()]
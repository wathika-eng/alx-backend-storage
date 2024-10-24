#!/usr/bin/env python3

""" 10-update_topics """

def update_topics(mongo_collection, name, topics):
    """ Update all topics of a school document based on the name """
    return mongo_collection.update.Many({"name": name}, {"$set": {"topics": topics}})
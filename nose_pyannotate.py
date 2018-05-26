#!/usr/bin/env python
# encoding=utf8
from nose.plugins import Plugin
from pyannotate_runtime import collect_types


class NoseAnnotatorPlugin(Plugin):
    """
    Write `type_info.json` file using pyannotate, for pyannotate.
    """
    name = 'nose-pyannotate'

    def begin(self, *args, **kwargs):
        collect_types.init_types_collection()

    def afterTest(self, *args, **kwargs):
        collect_types.pause()

    def beforeTest(self, *args, **kwargs):
        collect_types.resume()

    def report(self, stream):
        collect_types.dump_stats('type_info.json')

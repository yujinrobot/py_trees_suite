#!/usr/bin/env python
#
# scripts/demo_tree
#
# License: BSD
#   https://raw.github.com/stonier/py_trees_suite/license/LICENSE
#
##############################################################################
# Documentation
##############################################################################
"""
Simple demo program for py trees
"""
##############################################################################
# Imports
##############################################################################

import py_trees

##############################################################################
# Logging Level
##############################################################################

py_trees.logging.level = py_trees.logging.Level.DEBUG

##############################################################################
# Classes
##############################################################################


class Visitor(py_trees.trees.VisitorBase):
    def __init__(self):
        super(Visitor, self).__init__(full=False)
        self.logger = py_trees.logging.get_logger("Visitor")

    def initialise(self):
        pass

    def run(self, behaviour):
        self.logger.info("  %s [visited][%s]" % (behaviour.name, behaviour.status))


def pre_tick_handler(behaviour_tree):
    print("\n--------- Run %s ---------\n" % behaviour_tree.count)


##############################################################################
# Main
##############################################################################

if __name__ == '__main__':
    root = py_trees.composites.LoopingSequence(name="Demo Looping")
    idle_1 = py_trees.behaviours.Success("Idle 1")
    idle_2 = py_trees.behaviours.Success("Idle 2")
    idle_3 = py_trees.behaviours.Success("Idle 3")

    root.add_child(idle_1)
    root.add_child(idle_2)
    root.add_child(idle_3)

    tree = py_trees.BehaviourTree(root)

    tree.visitors.append(Visitor())
    tree.tick_tock(sleep_ms=500, number_of_iterations=py_trees.CONTINUOUS_TICK_TOCK, pre_tick_handler=pre_tick_handler)

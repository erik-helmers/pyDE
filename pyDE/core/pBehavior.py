""" Managing of the PyDE behavior"""


class pBehavior:

    def __init__(self):
        self.behaviors = {}
        self.load_behaviors()

    def load_behaviors(self):
        pass

    def register_behaviors_signal(self, behaviorenv, behaviorname):

        behaviorenv = self.get_behavior(behaviorenv)

        if not isinstance(behaviorenv, list):
            raise ValueError("bad behavior env")

        if behaviorname in self.get_behavior(behaviorenv):
            raise ValueError("behavior '%s' already exists in %s" %
                             (behaviorname, " ".join(behaviorenv)))

        self.behaviorenv[behaviorname] = []

    def register_behaviors_slot(self, behaviorname, behavior):
        self.get_behavior(behaviorname).append(behavior)

    def get_behavior(self, behaviorenv):
        output = self.behaviors
        for name in behaviorenv:
            output = output[name]
        return output


behavior = pBehavior

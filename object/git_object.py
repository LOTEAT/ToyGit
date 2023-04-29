class GitObject(object):
    repo = None
    def __init__(self, repo, data=None):
        self.repo = repo
        if data != None:
            self.deserialize(data)
    
    def serialize(self):
        """This function MUST be implemented by subclasses.
It must read the object's contents from self.data, a byte string, and do
whatever it takes to convert it into a meaningful representation.  What exactly that means depend on each subclass."""
        raise Exception("Unimplemented!")

    def deserialize(self, data):
        raise Exception("Unimplemented!")
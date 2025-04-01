class KnowledgeGraph:
    def __init__(self):
        self.graph = {}

    def add_triplet(self, subject, relation, object):
        # if not isinstance(subject, str) or not isinstance(relation, str) or not isinstance(object, str):
        if not all(isinstance(x, str) for x in (subject, relation, object)):
            raise ValueError("All arguments must be strings.")
        
        if subject not in self.graph:
            self.graph[subject] = {}
        
        if relation not in self.graph[subject]:
            self.graph[subject][relation] = set()
        
        self.graph[subject][relation].add(object)

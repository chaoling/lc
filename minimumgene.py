   def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        '''
        iterate through the Gene Bank, build a dictionary of key: with each position masked by * and value of the words in the bank.
        then from the startGene, find all genes in the next step according to the dictionary of genes, which is one step away from the origin, and keep expanding the bfs until you first hit
        the endGene, return the level
        '''
        if endGene not in bank:
            return -1
        if startGene == endGene:
            return 0
        neighbors = defaultdict(list)
        for gene in bank:
            for i  in range(len(gene)):
                key = gene[:i]+"*"+gene[i+1:]
                neighbors[key].append(gene)
        
        q = deque([(startGene,0)])
        visited = {startGene}
        while q:
            cur,level = q.popleft()
            for i in range(len(cur)):
                key = cur[:i]+"*"+cur[i+1:]
                if key in neighbors:
                    for item in neighbors[key]:
                        if item == endGene:
                            return level+1
                        if item not in visited:
                            visited.add(item)
                            q.append((item,level+1))
                neighbors[key].clear()
        return -1

class Solution(object):
    def countSmaller(self, nums):
        # Func auxiliar para ordenar e computar os elementos menores
        def ordenar(enum):
            metade = len(enum) // 2
            if metade:
                # divide a enum recursivamente em duas partes
                esquerda, direita = ordenar(enum[:metade]), ordenar(enum[metade:])
                n = len (direita)
                m =  len(esquerda)
                i = 0
                j = 0
                while i < m or j < n:
                    if j == n or (i < m and esquerda[i][1] <= direita[j][1]):
                        enum[i+j] = esquerda[i]
                        menores[esquerda[i][0]] += j
                        i = i + 1
                    else:
                        enum[i+j] = direita[j]
                        j = j + 1
            return enum

        # init lista 
        menores = [0] * len(nums)

        # chamada a função ordenar para e contar os elementos menores
        ordenar(list(enumerate(nums))) # cria uma enumeração dos elementos da lista 
        return menores
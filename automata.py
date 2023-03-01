class Automata:
    def __init__(self, file):
        self.states = []
        self.alphabet = []
        self.transitions = {}
        self.initial_state = None
        self.final_states = []
        self.read_file(file)

    def read_file(self, file):
        with open(file, 'r') as f:
            self.alphabet = f.readline().strip().split()
            for line in f:
                # first column is the state
                state = line.split()[0]
                self.states.append(
                    state.replace('>','').replace('*','')
                )
                # pegar as transições de acorco com o alfabeto, utilizando tuplas (estado, simbolo), e o estado de destino
                for i, symbol in enumerate(self.alphabet):
                    # se o estado de destino for vazio, não adicionar a transição
                    if line.split()[i+1] != '{}':

                        self.transitions[(state.replace('>','').replace('*',''), symbol)] = line.split()[i+1].replace(
                            '{',''
                            ).replace(
                            '}',''
                            ).split(',')
                # pegar o estado inicial, que é identificado por > no arquivo
                if '>' in line:
                    self.initial_state = state.replace('>','').replace('*','')
                # pegar os estados finais, que são identificados por * no arquivo
                if '*' in line:
                    self.final_states.append(state.replace('>','').replace('*',''))
            # close the file
            f.close()

    def getTransition(self, state, symbol):
        return self.transitions[(state, symbol)] if (state, symbol) in self.transitions else []
    
    def run(self, word):
        current_state = set([self.initial_state])
        for symbol in word:
            next_state = set()
            while next_state == set() and current_state != set():
                aux = set()
                e_transition = set()
                for state in current_state:
                    next_state |= set(self.getTransition(state, symbol))
                    e_transition |= set(self.getTransition(state, '&'))
                aux |= next_state
                current_state = aux
                current_state |= e_transition
                
        return any(final_state in self.final_states for final_state in current_state)
        

    def printTransitions(self):
        for key, value in self.transitions.items():
            print(key,"=", value)

    def __str__(self):
        return "Transições: "+str(self.transitions)+"\nEstados: "+str(self.states)+"\nAlfabeto: "+str(self.alphabet)+"\nIncial: "+str(self.initial_state)+"\nFinal: "+str(self.final_states)

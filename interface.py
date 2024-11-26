import tkinter as tk
from frame_forces import Frame_forces
from frame_illustrations import Frame_illustrations
from frame_resultants import Frame_resultants
import index
from forcePy import ForcePy
import param_given as pg

class InterfaceApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Interface com Frame Forces e Frame Illustration")
        self.geometry("1000x600")  # Tamanho inicial da janela

        # Frame para ilustrações
        self.frame_illustration = Frame_illustrations(self)  # Borda adicionada
        self.frame_illustration.grid(row=0, column=0, sticky="nsew", padx=(30, 3), pady=(30, 3))

        # Frame para forças
        self.frame_forces = Frame_forces(self)  # Borda adicionada
        self.frame_forces.grid(row=0, column=1, columnspan=2, sticky="nsew", padx=(3, 3), pady=(30, 3))

        # Frame para resultantes
        self.frame_resultants = Frame_resultants(self)  # Borda adicionada
        self.frame_resultants.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=(30, 3), pady=(3, 30))

        # Canvas para botões
        self.frame_buttons = tk.Canvas(self, width=180, height=250, borderwidth=1, relief="solid")  # Adicionando borda ao canvas
        self.frame_buttons.grid(row=1, column=2, sticky="nsew", padx=(3, 40), pady=(3, 40))

        # Ajustando o peso das linhas e colunas para expandir corretamente
        self.grid_rowconfigure(0, weight=1)  # Permitir que a primeira linha expanda
        self.grid_rowconfigure(1, weight=1)  # Permitir que a segunda linha expanda
        self.grid_columnconfigure(0, weight=1)  # Permitir que a primeira coluna expanda
        self.grid_columnconfigure(1, weight=1)  # Permitir que a segunda coluna expanda
        self.grid_columnconfigure(2, weight=1)  # A terceira coluna não precisa expandir



        # Adiciona e apaga força - botões centralizados

        # Configuração dos botões
        self.btn_add_force = tk.Button(self.frame_buttons, text="Adicionar força", command=self.add_force, height=2)
        self.btn_add_force.grid(row=0, column=0, padx=15, pady=(20, 5), sticky="ew")

        self.btn_del_force = tk.Button(self.frame_buttons, text="Apagar força", command=self.del_force, height=2)
        self.btn_del_force.grid(row=1, column=0, padx=15, pady=5, sticky="ew")

        self.btn_calculate = tk.Button(self.frame_buttons, text="Calcular Resultante", command=self.calculate, height=3)
        self.btn_calculate.grid(row=2, column=0, padx=15, pady=(20, 5), sticky="ew")
        
        self.btn_reset = tk.Button(self.frame_buttons, text="Novo", command=self.reset, height=3)
        self.btn_reset.grid(row=3, column=0, padx=15, pady=(5, 20), sticky="ew")

        # Configurando o frame para que os botões expandam
        self.frame_buttons.grid_rowconfigure(0, weight=0)  # Primeira linha expande
        self.frame_buttons.grid_rowconfigure(1, weight=0)  # Segunda linha expande
        self.frame_buttons.grid_rowconfigure(2, weight=1)  # Terceira linha expande
        self.frame_buttons.grid_columnconfigure(0, weight=1)  # Primeira coluna expande


    def add_force(self):
        self.frame_forces.add_force()

    def del_force(self):
        self.frame_forces.del_force()

    def calculate(self):
        self.btn_add_force.config(state="disabled")
        self.btn_del_force.config(state="disabled")
        self.btn_calculate.config(state="disabled")

        force_data = self.frame_forces.update_force_resultant_data()
        self.get_force_list(force_data)
        
        index.calculate_resultant(self.forces, self.resultants)
        self.bar_pos_min, self.bar_pos_max = self.forces[0].distance, self.forces[0].distance

        for force in self.forces:
            self.bar_pos_min = float(force.distance) if self.bar_pos_min > float(force.distance) else self.bar_pos_min
            self.bar_pos_max = float(force.distance) if self.bar_pos_max < float(force.distance) else self.bar_pos_max
            self.bar_length =  self.bar_pos_max - self.bar_pos_min

        for resultant in self.resultants:
            self.bar_pos_min = float(resultant.distance) if self.bar_pos_min > float(resultant.distance) else self.bar_pos_min
            self.bar_pos_max = float(resultant.distance) if self.bar_pos_max < float(resultant.distance) else self.bar_pos_max
            self.bar_length =  self.bar_pos_max - self.bar_pos_min

        for resultant in self.resultants:
            self.frame_illustration.apply_force(resultant.distance, resultant.tetadegree, 'R', self.bar_length, self.bar_pos_min)
            self.frame_illustration.apply_suport(resultant.distance, self.bar_length, self.bar_pos_min)

            self.frame_resultants.create_force_input(resultant, 'R')

        for force in self.forces:
            self.frame_illustration.apply_force(force.distance, force.tetadegree, 'F', self.bar_length, self.bar_pos_min)

            self.frame_resultants.create_force_input(force, 'F')

        #atualizar o frame_resultants com as forças...
        self.frame_illustration.draw_bar()

    def reset(self):
        self.forces = []
        self.resultants = []
        self.force_data = {}

        # Fecha a janela atual
        self.frame_illustration.destroy()
        self.frame_forces.destroy()
        self.frame_resultants.destroy()
        self.destroy()

        # Cria uma nova janela e reinicia a aplicação
        app = InterfaceApp()
        app.mainloop()  


    def get_force_list(self,force_data):
        self.forces = []
        self.resultants = []

        for force in force_data:
            force_data[force]['distance'] = float(force_data[force]['distance'])

            if force[0] == 'F':
                if force_data[force]['param_given'] == 'Fx e Fy':
                    force_data[force]['param1'] = float(force_data[force]['param1'])
                    force_data[force]['param2'] = float(force_data[force]['param2'])
                    force_data[force]['param_given'] = pg.Param_given.DECOMPOSED_FORCES

                elif force_data[force]['param_given'] == 'Módulo e teta':
                    force_data[force]['param1'] = float(force_data[force]['param1'])
                    force_data[force]['param_given'] = pg.Param_given.MODULE_TETA

                elif force_data[force]['param_given'] == 'Módulo e vetor n':
                    force_data[force]['param1'] = float(force_data[force]['param1'])
                    force_data[force]['param_given'] = pg.Param_given.MODULE_NVECTOR
                
                if force_data[force]['param_given'] != 'Selecione':
                    self.forces.append(ForcePy(force_data[force]['distance'], force_data[force]['param_given'], force_data[force]['param1'], force_data[force]['param2']))
            
            else:
                self.resultants.append(ForcePy(force_data[force]['distance']))
            
if __name__ == "__main__":
    app = InterfaceApp()
    app.mainloop()

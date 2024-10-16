import tkinter as tk
from forcePy import ForcePy

class Frame_resultants(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        force = ForcePy
        
        self.entries = {}
        self.force_count = 0
        self.resultant_count = 0

        # Criação da área de entrada
        self.create_input_area()

    def create_input_area(self):
        # Canvas para rolagem com borda
        self.canvas_frame = tk.Canvas(self, width=720, height=250, borderwidth=1, relief="solid")
        self.canvas_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")

        # Barra de rolagem vertical
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas_frame.yview, width=20)
        self.scrollbar.grid(row=0, column=1, sticky="nse", padx=(5,5), pady=(5,5))
        self.canvas_frame.config(yscrollcommand=self.scrollbar.set)

        # Frame interno para os inputs (dentro do Canvas)
        self.frame_inner = tk.Frame(self.canvas_frame)
        
        # Criar uma janela dentro do canvas para o frame interno
        self.canvas_frame.create_window((0, 0), window=self.frame_inner, anchor="nw")

        # Configuração de redimensionamento automático do canvas
        self.frame_inner.bind("<Configure>", self.update_scrollregion)

        # Criação das entradas iniciais (f1, f2, f3, f4)
        for i in range(1, self.force_count + 1):
            self.create_force_input(i - 1, f'F{i}')

    def create_force_input(self, force:ForcePy, force_type):
        # Definindo os dados a serem exibidos
        module = str(round(force.module,4))
        r = str(round(force.distance,4))
        teta = str(round(force.teta,4))
        fx = str(round(force.forcex,4))
        fy = str(round(force.forcey,4))
        n = str(force.nvector)

        if force_type == 'R':
            count = self.resultant_count
            self.resultant_count +=1
            row_count = self.resultant_count
        else:
            count = self.force_count
            self.force_count +=1
            row_count = self.force_count+2
        
        # Criando o texto formatado para alinhamento
        force_label_text = (
            f"{force_type}{str(count+1).ljust(5)}: "
            f" módulo = {module.ljust(16)} "
            f"r = {r.ljust(16)} "
            f"θ = {teta.ljust(16)} "
            f"Fx = {fx.ljust(16)} "
            f"Fy = {fy.ljust(16)} "
            f"vetor n = {n}"
        )
        
        force_label = tk.Label(self.frame_inner, text=force_label_text)
        force_label.grid(row=row_count, column=0, padx=3, pady=5, sticky='w')

    def delete_force_input(self, label_text):
        if label_text in self.entries:
            # Excluir todos os widgets associados à força
            for widget in self.entries[label_text].values():
                widget.grid_forget()
                widget.destroy()
            del self.entries[label_text]

    def add_force(self):
        self.force_count += 1
        self.create_force_input(self.force_count - 1, f'f{self.force_count}')
        self.update_scrollregion()
        self.scroll_to_end()

    def del_force(self):
        if self.force_count > 0:
            self.delete_force_input(f'f{self.force_count}')
            self.force_count -= 1
            self.update_scrollregion()

    def update_scrollregion(self, event=None):
        """Atualiza a região de rolagem do canvas"""
        self.canvas_frame.config(scrollregion=self.canvas_frame.bbox("all"))

    def scroll_to_end(self):
        """Rola a barra de rolagem para o final ao adicionar uma nova força"""
        self.canvas_frame.yview_moveto(1)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Resultado das Forças")

    # Adiciona o Frame_resultants na janela principal
    app = Frame_resultants(root)
    app.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Configuração de redimensionamento para o frame principal
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    root.mainloop()

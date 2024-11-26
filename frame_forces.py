import tkinter as tk

class Frame_forces(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.entries = {}
        self.force_data = {}
        self.force_count = 1  

        # Criação da área de entrada
        self.create_input_area()

    def create_input_area(self):
        # Canvas para rolagem com borda
        self.canvas_frame = tk.Canvas(self, width=550, height=250, borderwidth=1, relief="solid")  # Adicionando borda ao canvas
        self.canvas_frame.grid(row=0, column=0, sticky="nsew")

        # Barra de rolagem vertical
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas_frame.yview)
        self.scrollbar.grid(row=0, column=0, sticky="nse", padx=(5,5), pady=5)
        self.canvas_frame.config(yscrollcommand=self.scrollbar.set)

        # Frame interno para os inputs (dentro do Canvas)
        self.frame_inner = tk.Frame(self.canvas_frame)

        # Criação de uma janela dentro do canvas que vai conter o frame
        self.canvas_window = self.canvas_frame.create_window(0, 0, window=self.frame_inner, anchor="nw")

        # Configuração de redimensionamento automático do canvas
        self.frame_inner.bind("<Configure>", self.update_scrollregion)

        self.create_resultant_input(0, F'Pino')
        self.create_resultant_input(1, F'Rolete')

        # Criação das entradas iniciais (f1, f2, f3, f4)
        for i in range(1, self.force_count + 1):
            self.create_force_input(i + 1, F'F{i}')

    def create_force_input(self, row, label_text):
        # Label da força
        lbl_f = tk.Label(self.frame_inner, text=f'{label_text}:')
        lbl_f.grid(row=row, column=0, padx=3, pady=5)

        # Dropdown
        options = ["Selecione", "Fx e Fy", "Módulo e teta", "Módulo e vetor n"]
        selected_option = tk.StringVar(self.frame_inner)
        selected_option.set(options[0])

        option_menu = tk.OptionMenu(self.frame_inner, selected_option, *options)
        option_menu.config(width=15)
        option_menu.grid(row=row, column=1, padx=3, pady=5)

        # Label para r
        lbl_r = tk.Label(self.frame_inner, text="r:")
        lbl_r.grid(row=row, column=2, padx=3, pady=5)

        # Entrada para r
        entry_r = tk.Entry(self.frame_inner, width=10)
        entry_r.grid(row=row, column=3, padx=3, pady=5)

        # Entradas para parâmetros
        lbl_param1 = tk.Label(self.frame_inner, text="param1:")
        lbl_param1.grid(row=row, column=4, padx=3, pady=5)
        entry_param1 = tk.Entry(self.frame_inner, width=10)
        entry_param1.grid(row=row, column=5, padx=3, pady=5)

        lbl_param2 = tk.Label(self.frame_inner, text="param2:")
        lbl_param2.grid(row=row, column=6, padx=3, pady=5)
        entry_param2 = tk.Entry(self.frame_inner, width=10)
        entry_param2.grid(row=row, column=7, padx=3, pady=5)

        # Desabilitar param1 e param2 inicialmente
        entry_param1.config(state="disabled")
        entry_param2.config(state="disabled")

        def toggle_param_entries(*args):
            selected_option_value = selected_option.get()  # Obtém o valor atual do OptionMenu

            if selected_option_value == "Selecione":
                entry_param1.config(state="disabled")
                entry_param2.config(state="disabled")
                lbl_param1.config(text="param1:")  # Texto padrão
                lbl_param2.config(text="param2:")  # Texto padrão
            else:
                entry_param1.config(state="normal")
                entry_param2.config(state="normal")
                
                # Atualiza os textos com base na opção selecionada
                if selected_option_value == "Fx e Fy":
                    lbl_param1.config(text="Fx:")
                    lbl_param2.config(text="Fy:")
                elif selected_option_value == "Módulo e teta":
                    lbl_param1.config(text="Módulo:")
                    lbl_param2.config(text="Teta:")
                elif selected_option_value == "Módulo e vetor n":
                    lbl_param1.config(text="Módulo:")
                    lbl_param2.config(text="Vetor n:")


        # Vincular a função ao OptionMenu
        selected_option.trace_add("write", toggle_param_entries)

        # Armazenando todos os widgets no dicionário
        self.entries[label_text] = {
            'label_f': lbl_f,  # Armazenando o label da força
            'param_given': option_menu,  # Dropdown
            'lbl_distance': lbl_r,  # Label do r
            'lbl_param1': lbl_param1,
            'lbl_param2': lbl_param2,
            'distance': entry_r,  # Entrada de r
            'param1': entry_param1,  # Parâmetro 1
            'param2': entry_param2  # Parâmetro 2
        }

        self.force_data[label_text] = {
            'param_given': selected_option,
            'distance': entry_r,
            'param1': entry_param1, 
            'param2': entry_param2
        }
    
    def create_resultant_input(self, row, label_text):
        # Label da força
        lbl_f = tk.Label(self.frame_inner, text=f'{label_text}:')
        lbl_f.grid(row=row, column=0, padx=3, pady=5)

        # Label para r
        lbl_r = tk.Label(self.frame_inner, text="r:")
        lbl_r.grid(row=row, column=2, padx=3, pady=5)

        # Entrada para r
        entry_r = tk.Entry(self.frame_inner, width=10)
        entry_r.grid(row=row, column=3, padx=3, pady=5)

        # Armazenando todos os widgets no dicionário
        self.entries[label_text] = {
            'label_f': lbl_f,  # Armazenando o label da força
            'lbl_distance': lbl_r,  # Label do r
            'distance': entry_r,  # Entrada de r
        }

        self.force_data[label_text] = {
            'distance': entry_r,
        }

    def update_force_resultant_data(self):
        for label, widgets in self.force_data.items():
            if label == 'Pino' or label == 'Rolete':
                # Extrair o valor da entrada de distância
                distance_entry = widgets['distance']
                a= type(distance_entry)
                if  isinstance(distance_entry, tk.Entry):
                    self.force_data[label]['distance'] = distance_entry.get()
                else:
                    self.force_data[label]['distance'] = distance_entry
            elif label[0] == 'F':
                # Extrair o valor do OptionMenu a partir da StringVar associada
                option_menu_var = widgets['param_given']  # Aqui você armazena a StringVar, não o OptionMenu
                if isinstance(option_menu_var, tk.StringVar):
                    self.force_data[label]['param_given'] = option_menu_var.get()

                # Extrair o valor da entrada de distância
                distance_entry = widgets['distance']
                if  isinstance(distance_entry, tk.Entry):
                    self.force_data[label]['distance'] = distance_entry.get()
                else:
                    self.force_data[label]['distance'] = distance_entry

                # Extrair os valores dos parâmetros 1 e 2
                param1_entry = widgets['param1']
                param2_entry = widgets['param2']
                if  isinstance(distance_entry, tk.Entry):
                    self.force_data[label]['param1'] = param1_entry.get()
                    self.force_data[label]['param2'] = param2_entry.get()
                else:
                    self.force_data[label]['param1'] = param1_entry
                    self.force_data[label]['param2'] = param2_entry
        return self.force_data

    def delete_force_input(self, label_text):
        if label_text in self.entries:
            # Excluir todos os widgets associados à força
            for widget in self.entries[label_text].values():
                widget.grid_forget()
                widget.destroy()
            del self.entries[label_text]

    def add_force(self):
        self.force_count += 1
        self.create_force_input(self.force_count + 1, f'F{self.force_count}')
        self.update_scrollregion()
        self.scroll_to_end()

    def del_force(self):
        if self.force_count > 0:
            self.delete_force_input(f'F{self.force_count}')
            self.force_count -= 1
            self.update_scrollregion()

    def update_scrollregion(self, event=None):
        """Atualiza a região de rolagem do canvas"""
        self.canvas_frame.config(scrollregion=self.canvas_frame.bbox("all"))

    def scroll_to_end(self):
        """Rola a barra de rolagem para o final ao adicionar uma nova força"""
        self.canvas_frame.yview_moveto(1)

    def on_canvas_resize(self, event):
        """Redimensiona o canvas para se ajustar corretamente"""
        canvas_width = event.width
        self.canvas_frame.itemconfig(self.canvas_window, width=canvas_width - 4)  # Subtraindo bordas


if __name__ == "__main__":
    root = tk.Tk()

    # Adiciona o Frame_forces na janela principal
    app = Frame_forces(root)
    app.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    root.mainloop()

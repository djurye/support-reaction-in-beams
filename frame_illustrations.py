import tkinter as tk
import math

class Frame_illustrations(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        # Configurações da barra
        self.bar_length = 0
        self.num_points = 20  # Número de divisões da barra
        self.forces = []  # Lista de forças aplicadas (posição, magnitude e ângulo)
        self.force_pos_min = 0
        self.force_pos_max = 0
        self.supports = []

        # Criar o canvas para desenhar dentro do próprio frame
        self.canvas = tk.Canvas(self, border=1, relief="solid", width=350, height=250)
        self.canvas.grid(row=0, column=0, columnspan=2)

        # Entrada para posição, magnitude e ângulo da força
        self.force_pos = 2
        self.force_magnitude = 10
        self.force_angle = 90

        # Inicializar o desenho da barra
        #self.draw_bar()
    
    def apply_force(self, force_position, force_angle, force_type, bar_lenght, bar_pos_min):
        """Aplica uma nova força e redesenha a barra com todas as forças."""
        try:
            if -360 <= force_angle <= 360:
                # Adiciona a nova força à lista
                point_index = int(((force_position - bar_pos_min) / bar_lenght) * self.num_points)
                self.forces.append((force_type, point_index, force_angle, force_position))
                self.force_count = 1
                self.resultant_count = 1
                #self.draw_bar()
            else:
                print("Posição ou ângulo inválido!")
        except ValueError:
            print("Entrada inválida!")

    def apply_suport(self, suport_position, bar_length, bar_pos_min):
        point_index = int(((suport_position - bar_pos_min)/ bar_length) * self.num_points)
        self.supports.append(point_index)
        self.support_count = 1
        #self.draw_bar()

    def draw_bar(self):
        """Desenha a barra e todas as forças aplicadas."""
        # Limpa o canvas
        self.canvas.delete("all")

        # Ponto inicial da barra
        x_start = 50
        y_start = 125

        # Ponto final da barra (barra sempre horizontal)
        x_end = x_start + 250
        y_end = y_start

        # Desenha a barra
        self.canvas.create_line(x_start, y_start, x_end, y_end, width=5)

        # Desenha os pontos da barra
        points = []
        for i in range(self.num_points + 1):
            x_point = x_start + (i / self.num_points) * (x_end - x_start)
            y_point = y_start
            points.append((x_point, y_point))
            self.canvas.create_oval(x_point - 2, y_point - 2, x_point + 2, y_point + 2, fill="black")

        # Desenha as forças aplicadas
        for force_type, point_index, force_angle, force_posicion in self.forces:
            x_force = points[point_index][0]
            y_force = points[point_index][1]

            # Calcula o vetor de força com base no ângulo fornecido
            force_angle_radians = math.radians(force_angle)
            force_length = 50  # Comprimento constante da seta

            # Calcula as coordenadas finais da seta da força
            force_x_end = x_force + force_length * math.cos(force_angle_radians)
            force_y_end = y_force - force_length * math.sin(force_angle_radians)

            # Desenha a seta da força
            self.canvas.create_line(x_force, y_force, force_x_end, force_y_end, arrow=tk.LAST, fill="red", width=2)

            # Desenha o texto do valor da força fora da seta
            if force_type == 'R':
                count = self.resultant_count
                self.resultant_count +=1
            else:
                count = self.force_count
                self.force_count +=1

            self.canvas.create_text(x_force, y_force - 60, text=f"{force_type}{count}", fill="red")
            self.canvas.create_text(x_force, y_force + 60, text=f"r={force_posicion}", fill="red")

        # Desenha os suportes
        # Primeiro desenho: Triângulo
        x_support = points[self.supports[0]][0]
        y_support = points[self.supports[0]][1]
        xa, xb, xc = x_support-10, x_support+10, x_support
        ya, yb, yc = y_support+15, y_support+15, y_support
        self.canvas.create_polygon(xa, ya, xb, yb, xc, yc, fill="blue", width=0)

        # Segundo desenho: Círculo
        x_support = points[self.supports[1]][0]
        y_support = points[self.supports[1]][1]
        xa, xb = x_support-7.5, x_support+7.5
        ya, yb = y_support, y_support+15
        self.canvas.create_oval(xa, ya, xb, yb, fill="blue", width=0)

# Inicializar a aplicação Tkinter
if __name__ == "__main__":
    root = tk.Tk()
    app = Frame_illustrations(root)
    app.grid(row=0, column=0, padx=10, pady=10)
    root.mainloop()

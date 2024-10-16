import tkinter as tk
import math

class Frame_illustrations(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        # Configurações da barra
        self.bar_length = 250  # Comprimento da barra em pixels
        self.num_points = 20  # Número de divisões da barra
        self.forces = []  # Lista de forças aplicadas (posição, magnitude e ângulo)
        self.supports = []

        # Criar o canvas para desenhar dentro do próprio frame
        self.canvas = tk.Canvas(self, border=1, relief="solid", width=350, height=250)
        self.canvas.grid(row=0, column=0, columnspan=2)

        # Entrada para posição, magnitude e ângulo da força
        self.force_pos = 2
        self.force_magnitude = 10
        self.force_angle = 90

        # Inicializar o desenho da barra
        self.draw_bar()

    def apply_force(self, force_position, force_angle, force_type):
        """Aplica uma nova força e redesenha a barra com todas as forças."""
        try:
            if 0 <= force_position <= 10 and -360 <= force_angle <= 360:
                # Adiciona a nova força à lista
                point_index = int((force_position / 10) * self.num_points)
                self.forces.append((force_type, point_index, force_angle))
                self.force_count = 1
                self.resultant_count = 1
                self.draw_bar()
            else:
                print("Posição ou ângulo inválido!")
        except ValueError:
            print("Entrada inválida!")

    def apply_suport(self, suport_position):
        point_index = int((suport_position / 10) * self.num_points)
        self.supports.append(point_index)
        self.support_count = 1
        self.draw_bar()


    def draw_bar(self):
        """Desenha a barra e todas as forças aplicadas."""
        # Limpa o canvas
        self.canvas.delete("all")

        # Ponto inicial da barra
        x_start = 50
        y_start = 125

        # Ponto final da barra (barra sempre horizontal)
        x_end = x_start + self.bar_length
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
        for force_type, point_index, force_angle in self.forces:
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
            self.canvas.create_text(x_force, y_force + 60, text=f"r={point_index}", fill="red")

        # Desenha os suportes
        for point_index in self.supports:
            x_support = points[point_index][0]
            y_support = points[point_index][1]

            # Calcula as coordenadas do triangulo
            xa, xb, xc = x_support-10, x_support+10, x_support
            ya, yb, yc = y_support+15, y_support+15, y_support

            # Desenha o triangulo
            self.canvas.create_polygon(xa, ya, xb, yb, xc, yc, fill="blue", width=2)

            self.support_count+=1

# Inicializar a aplicação Tkinter
if __name__ == "__main__":
    root = tk.Tk()
    app = Frame_illustrations(root)
    app.grid(row=0, column=0, padx=10, pady=10)
    root.mainloop()

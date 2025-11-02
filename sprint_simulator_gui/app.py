import tkinter as tk
from tkinter import ttk, messagebox
from . import app_logic


class SprintSimulatorApp:
    def __init__(self, root):

        self.root = root
        self.root.title('Sprint F-V Simulátor')
        self.style = ttk.Style()
        self.style.theme_use('clam')

        main_frame = ttk.Frame(self.root, padding="10 10 10 10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.root.columnconfigure(0, weight = 1)
        self.root.rowconfigure(0, weight = 1)

        self._create_input_widgets(main_frame)
        self._create_output_widgets(main_frame)
        self._create_action_widgets(main_frame)

        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)


    def _create_input_widgets(self, parent_frame):

        input_frame = ttk.LabelFrame(parent_frame, text='Vstupní parametry', padding=10)
        input_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        ttk.Label(input_frame, text="F0 (N/kg):").grid(row=0, column=0, sticky="w", pady=3, padx=5)
        self.entry_f0 = ttk.Entry(input_frame, width=12)
        self.entry_f0.grid(row=0, column=1, sticky="w", pady=3, padx=5)
        self.entry_f0.insert(0, "8.0")

        ttk.Label(input_frame, text="V0 (m/s):").grid(row=1, column=0, sticky="w", pady=3, padx=5)
        self.entry_v0 = ttk.Entry(input_frame, width=12)
        self.entry_v0.grid(row=1, column=1, sticky="w", pady=3, padx=5)
        self.entry_v0.insert(0, "10.0")

        ttk.Label(input_frame, text="Hmotnost (kg):").grid(row=2, column=0, sticky="w", pady=3, padx=5)
        self.entry_weight = ttk.Entry(input_frame, width=12)
        self.entry_weight.grid(row=2, column=1, sticky="w", pady=3, padx=5)
        self.entry_weight.insert(0, "83.0")

        ttk.Label(input_frame, text="Výška (m):").grid(row=3, column=0, sticky="w", pady=3, padx=5)
        self.entry_height = ttk.Entry(input_frame, width=12)
        self.entry_height.grid(row=3, column=1, sticky="w", pady=3, padx=5)
        self.entry_height.insert(0, "1.85")


    def _create_output_widgets(self, parent_frame):

        output_frame = ttk.LabelFrame(parent_frame, text="Výsledky simulace", padding="10")
        output_frame.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

        self.output_labels = {}
        
        output_definitions = {
            'running_time_100m': "Čas na 100m:",
            'top_speed': "Max. rychlost:",
            'top_speed_distance': "Vzd. max. rychlosti:",            
            'time_30m': "Čas na 30m:",
            'time_30m_fly': "Letmých 30m:",
            'fly_start': "Letmých 30m (start):",
            'fly_finish': "Letmých 30m (cíl):"

        }

        row = 0
        for key, text in output_definitions.items():
            ttk.Label(output_frame, text=text).grid(row=row, column=0, sticky="w", pady=3, padx=5)
            value_label = ttk.Label(output_frame, text="--", width=12, font=("Helvetica", 10, "bold"))
            value_label.grid(row=row, column=1, sticky="w", pady=3, padx=5)
            self.output_labels[key] = value_label
            row += 1


    def _create_action_widgets(self, parent_frame):

        action_frame = ttk.Frame(parent_frame, padding="10 0")
        action_frame.grid(row=1, column=0, columnspan=2, sticky="ew")

        btn_calculate = ttk.Button(action_frame, text="Vypočítat", command=self._handle_calculate)
        btn_calculate.grid(row=0, column=0, sticky="ew", padx=5)
        action_frame.columnconfigure(0, weight=1)


    def _handle_calculate(self):

        try:
            f0 = self.entry_f0.get()
            v0 = self.entry_v0.get()
            weight = self.entry_weight.get()
            height = self.entry_height.get()

            results = app_logic.run_simulation_logic(f0, v0, weight, height)


            if results:
                self.output_labels['time_30m'].config(text=f"{results['time_30m']:.2f} s")
                self.output_labels['running_time_100m'].config(text=f"{results['running_time_100m']:.2f} s")
                self.output_labels['top_speed'].config(text=f"{results['top_speed']:.2f} m/s")
                self.output_labels['top_speed_distance'].config(text=f"{results['top_speed_distance']:.0f} m")
                self.output_labels['time_30m_fly'].config(text=results['time_30m_fly'])
                self.output_labels['fly_start'].config(text=results['fly_start'])
                self.output_labels['fly_finish'].config(text=results['fly_finish'])

        except ValueError as e:
            messagebox.showerror("Chyba vstupu", str(e))
        except Exception as e:
            messagebox.showerror("Chyba simulace", str(e))


def main():
        try:
            root = tk.Tk()
            app = SprintSimulatorApp(root)
            root.mainloop()
        
        except ImportError as e:
            print("Chyba importu. Ujistěte se, že spouštíte modul z kořenové složky projektu.")
            print(f"Detail chyby: {e}")
            print("Spusťte pomocí: python -m simulator_gui.main")            


if __name__ == "__main__":
    main()

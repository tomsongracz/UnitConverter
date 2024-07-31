import tkinter as tk
from tkinter import ttk, messagebox

# Funkcje do konwersji
def convert_length(value, from_unit, to_unit):
    # Przeliczniki długości w metrach
    length_units = {
        'Meters': 1,
        'Kilometers': 1000,
        'Miles': 1609.34,
        'Inches': 0.0254,
        'Feet': 0.3048,
        'Knots': 1852
    }
    return value * length_units[from_unit] / length_units[to_unit]

def convert_mass(value, from_unit, to_unit):
    # Przeliczniki masy w gramach
    mass_units = {
        'Grams': 1,
        'Kilograms': 1000,
        'Pounds': 453.592,
        'Ounces': 28.3495
    }
    return value * mass_units[from_unit] / mass_units[to_unit]

def convert_temperature(value, from_unit, to_unit):
    # Funkcje lambda do konwersji temperatury
    conversions = {
        ('Celsius', 'Fahrenheit'): lambda v: (v * 9/5) + 32,
        ('Celsius', 'Kelvin'): lambda v: v + 273.15,
        ('Fahrenheit', 'Celsius'): lambda v: (v - 32) * 5/9,
        ('Fahrenheit', 'Kelvin'): lambda v: (v - 32) * 5/9 + 273.15,
        ('Kelvin', 'Celsius'): lambda v: v - 273.15,
        ('Kelvin', 'Fahrenheit'): lambda v: (v - 273.15) * 9/5 + 32,
    }
    return conversions.get((from_unit, to_unit), lambda v: v)(value)

# Funkcja obsługująca konwersję
def convert():
    try:
        value = float(entry_value.get())  # Pobranie wartości wejściowej
        from_unit = combo_from.get()  # Pobranie jednostki wejściowej
        to_unit = combo_to.get()  # Pobranie jednostki wyjściowej
        category = combo_category.get()  # Pobranie kategorii konwersji
        
        # Słownik funkcji konwersji dla różnych kategorii
        conversion_functions = {
            'Length': convert_length,
            'Mass': convert_mass,
            'Temperature': convert_temperature
        }
        
        # Wywołanie odpowiedniej funkcji konwersji
        result = conversion_functions[category](value, from_unit, to_unit)
        label_result.config(text=f'Result: {result:.2f} {to_unit}')  # Wyświetlenie wyniku
    except ValueError as e:
        messagebox.showerror("Error", str(e))  # Wyświetlenie komunikatu o błędzie

# Tworzenie interfejsu użytkownika
root = tk.Tk()
root.title("Unit Converter")

# Główna ramka aplikacji
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Pole wprowadzania wartości
ttk.Label(frame, text="Value:").grid(row=0, column=0, padx=5, pady=5)
entry_value = ttk.Entry(frame)
entry_value.grid(row=0, column=1, padx=5, pady=5)

# Pole wyboru kategorii konwersji
ttk.Label(frame, text="Category:").grid(row=1, column=0, padx=5, pady=5)
combo_category = ttk.Combobox(frame, values=["Length", "Mass", "Temperature"])
combo_category.grid(row=1, column=1, padx=5, pady=5)
combo_category.current(0)  # Ustawienie domyślnej kategorii

# Pole wyboru jednostki wejściowej
ttk.Label(frame, text="From:").grid(row=2, column=0, padx=5, pady=5)
combo_from = ttk.Combobox(frame)
combo_from.grid(row=2, column=1, padx=5, pady=5)

# Pole wyboru jednostki wyjściowej
ttk.Label(frame, text="To:").grid(row=3, column=0, padx=5, pady=5)
combo_to = ttk.Combobox(frame)
combo_to.grid(row=3, column=1, padx=5, pady=5)

# Przycisk do wykonania konwersji
ttk.Button(frame, text="Convert", command=convert).grid(row=4, column=0, columnspan=2, pady=10)

# Etykieta do wyświetlania wyniku konwersji
label_result = ttk.Label(frame, text="Result:")
label_result.grid(row=5, column=0, columnspan=2, pady=5)

# Funkcja do aktualizowania jednostek w zależności od wybranej kategorii
def update_units(event):
    # Słownik jednostek dla każdej kategorii
    units = {
        "Length": ["Meters", "Kilometers", "Miles", "Inches", "Feet", "Knots"],
        "Mass": ["Grams", "Kilograms", "Pounds", "Ounces"],
        "Temperature": ["Celsius", "Fahrenheit", "Kelvin"]
    }
    category = combo_category.get()
    combo_from.config(values=units[category])  # Ustawienie jednostek wejściowych
    combo_to.config(values=units[category])  # Ustawienie jednostek wyjściowych
    combo_from.current(0)  # Ustawienie domyślnej jednostki wejściowej
    combo_to.current(1)  # Ustawienie domyślnej jednostki wyjściowej

combo_category.bind("<<ComboboxSelected>>", update_units)  # Powiązanie funkcji z wyborem kategorii
update_units(None)  # Inicjalizacja jednostek dla domyślnej kategorii

root.mainloop()


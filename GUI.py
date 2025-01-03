import tkinter as tk
from tkinter import filedialog, messagebox
import os
from FileAnalysis import analyze_file  # Importer la fonction d'analyse


def start_machine_scan():
    """
    Lancer une analyse complète de la machine.
    """
    messagebox.showinfo("Machine Scan", "Machine scan started!")


def analyze_file_gui():
    """
    Permet à l'utilisateur de sélectionner un fichier à analyser.
    """
    file_path = filedialog.askopenfilename(title="Sélectionnez un fichier")
    if file_path:
        # Appeler la fonction d'analyse de fichier depuis FileAnalysis.py
        analyze_file(file_path)


def analyze_directory():
    """
    Permet à l'utilisateur de sélectionner un répertoire à analyser.
    Chaque fichier dans le répertoire est analysé.
    """
    directory_path = filedialog.askdirectory(title="Sélectionnez un répertoire")
    if directory_path:
        try:
            files = os.listdir(directory_path)
            # Filtrer les fichiers uniquement
            files = [f for f in files if os.path.isfile(os.path.join(directory_path, f))]
            if not files:
                messagebox.showinfo("Analyse de répertoire", "Aucun fichier trouvé dans le répertoire.")
                return
            
            # Analyse de chaque fichier
            for file in files:
                file_path = os.path.join(directory_path, file)
                analyze_file(file_path)
            
            messagebox.showinfo("Analyse de répertoire", "L'analyse du répertoire est terminée.")
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de l'analyse du répertoire : {str(e)}")


# Création de la fenêtre principale
root = tk.Tk()
root.title("Outil Anti-Rootkit")

# Couleurs et thèmes pour l'interface utilisateur
bg_color = "#FFFFFF"  # Blanc pour le fond
button_color = "#000000"  # Noir pour les boutons
button_text_color = "#00FF00"  # Vert néon pour le texte des boutons
font_color = "#FF0000"  # Rouge pour les titres

# Configurer la taille et le fond de la fenêtre
root.geometry("400x300")
root.configure(bg=bg_color)

# Titre de l'application
title_label = tk.Label(root, text="Outil Anti-Rootkit", fg=font_color, bg=bg_color, font=("Helvetica", 16, "bold"))
title_label.pack(pady=20)

# Bouton pour lancer une analyse de la machine
machine_scan_button = tk.Button(
    root, text="Lancer une analyse de la machine", bg=button_color, fg=button_text_color,
    font=("Helvetica", 12), command=start_machine_scan
)
machine_scan_button.pack(pady=10)

# Bouton pour analyser un fichier
file_analysis_button = tk.Button(
    root, text="Analyser un fichier", bg=button_color, fg=button_text_color,
    font=("Helvetica", 12), command=analyze_file_gui
)
file_analysis_button.pack(pady=10)

# Bouton pour analyser un répertoire
directory_analysis_button = tk.Button(
    root, text="Analyser un répertoire", bg=button_color, fg=button_text_color,
    font=("Helvetica", 12), command=analyze_directory
)
directory_analysis_button.pack(pady=10)

# Démarrage de la boucle principale de l'application
root.mainloop()

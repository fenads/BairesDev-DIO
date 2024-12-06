import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Função para gerar a matriz de confusão
def plot_confusion_matrix(y_true, y_pred):
    # Calcular a matriz de confusão
    con_mat = np.zeros((max(y_true) + 1, max(y_pred) + 1), dtype=int)
    for true, pred in zip(y_true, y_pred):
        con_mat[true][pred] += 1

    # Criar DataFrame para plotar
    con_mat_df = pd.DataFrame(con_mat)

    # Exibir a matriz de confusão como um heatmap
    plt.figure(figsize=(4, 4))
    sns.heatmap(con_mat_df, annot=True, cmap=plt.cm.Blues, cbar=True)
    plt.title('Matriz de Confusão')
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.tight_layout()
    plt.show()

    return con_mat

# Exemplo de uso
y_true = [0, 1, 2, 2, 0, 1, 1, 2, 0, 0]  # Verdadeiros
y_pred = [0, 2, 2, 2, 0, 0, 1, 2, 0, 1]  # Previstos

# Gerar e exibir a matriz de confusão
confusion_matrix = plot_confusion_matrix(y_true, y_pred)

# Classe de interesse (exemplo: classe 0)
class_of_interest = 0

# Extrair VP, FN, FP, VN
VP = confusion_matrix[class_of_interest, class_of_interest]  # Verdadeiros Positivos
FN = np.sum(confusion_matrix[class_of_interest, :]) - VP    # Falsos Negativos
FP = np.sum(confusion_matrix[:, class_of_interest]) - VP    # Falsos Positivos
VN = np.sum(confusion_matrix) - (VP + FN + FP)             # Verdadeiros Negativos

# Exibir os valores
print(f"\nClasse: {class_of_interest}")
print(f"Verdadeiros Positivos (VP): {VP}")
print(f"Falsos Negativos (FN): {FN}")
print(f"Falsos Positivos (FP): {FP}")
print(f"Verdadeiros Negativos (VN): {VN}")

# Calcular métricas
sensitivity = VP / (VP + FN) if (VP + FN) > 0 else 0
specificity = VN / (FP + VN) if (FP + VN) > 0 else 0
accuracy = (VP + VN) / np.sum(confusion_matrix)
precision = VP / (VP + FP) if (VP + FP) > 0 else 0
f_score = 2 * (precision * sensitivity) / (precision + sensitivity) if (precision + sensitivity) > 0 else 0

# Exibir métricas
print("\nMétricas")
print(f"Sensibilidade: {sensitivity:.2f}")
print(f"Especificidade: {specificity:.2f}")
print(f"Acurácia: {accuracy:.2f}")
print(f"Precisão: {precision:.2f}")
print(f"F-Score: {f_score:.2f}")
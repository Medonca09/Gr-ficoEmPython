# Código para fazer um gráfico para mostrar o total de membros por estados

# Passo 1: Importar a base de dados
import pandas as pd

planilha = 'tribunais-renouv.xlsx'
membros = pd.read_excel(planilha, sheet_name='Planilha1')

# Passo 2: Filtrar e processar os dados
# filtrar os dados para incluir apenas as linhas onde a coluna "MEMBRO DA REDE?" seja "SIM", e então contar quantos membros existem por estado.

membros.columns = ['TRIBUNAIS', 'ESTADO', 'NATUREZA', 'MEMBROS_REDE']

# Filtrar para incluir membros da rede
membros_rede = membros[membros["MEMBROS_REDE"] == "SIM"]

# Agrupar pela coluna "ESTADO" e contar o número de membros
membros_estado = membros_rede.groupby('ESTADO').size().reset_index(name='QUANTIDADE_MEMBROS')

# Calcular a porcentagem
total_membros = membros_estado["QUANTIDADE_MEMBROS"].sum()
membros_estado['PORCENTAGEM'] = (membros_estado['QUANTIDADE_MEMBROS'] / total_membros) * 100

# Passo 3: Criar gráfico
# Importando biblioteca para exibir o gráfico
import matplotlib.pyplot as plt

# Gráfico de barras
plt.figure(figsize=(12, 8))
bars = plt.bar(membros_estado["ESTADO"], membros_estado["QUANTIDADE_MEMBROS"], color='skyblue')
plt.xlabel('Estado')
plt.ylabel('Quantidade de Membros')
plt.title('Quantidade de Membros por Estado')
plt.xticks(rotation=45)
plt.tight_layout()

# Adicionar anotações com a porcentagem em cada barra
for bar, index in zip(bars, membros_estado.index):
    height = bar.get_height()
    percentage = membros_estado.loc[index, 'PORCENTAGEM']
    plt.text(
        bar.get_x() + bar.get_width() / 2.0,
        height,
        f'{height}\n({percentage:.1f}%)',
        ha='center',
        va='bottom'
    )

plt.show()

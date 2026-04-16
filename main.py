import flet as ft
from mes import Mes
import dias

def main(page: ft.Page):
    # --- Configurações de Estética ---
    page.title = "Cálculo de Frequência Escolar - ETE"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = "center"
    page.scroll = "adaptive"
    page.window_width = 1100 
    page.bgcolor = "#FDFDFD"
    page.zoom = 1.5
    page.update()

    # Dados da sua lógica POO
    meses_dados = dias.inicio()
    
    # Referências para atualização
    exibidores_porcentagem = {}
    inputs_list = []
    
    texto_media_geral = ft.Text("Média Anual: ---", size=32, weight="bold", color="#444444")
    status_final = ft.Text("", size=22, weight="bold")

    # --- Função de Cálculo Automático com uma casa decimal ---
    def calcular_tudo(e):
        soma_frequencias = 0
        meses_contabilizados = 0
        
        for i, campo in enumerate(inputs_list):
            mes_obj = meses_dados[i]
            nome_mes = mes_obj.nome
            
            if campo.value:
                try:
                    num_faltas = int(campo.value)
                    mes_obj.faltas = num_faltas
                    
                    # Cálculo com precisão decimal (usando / em vez de //)
                    # (100 * (Total de Horas - Faltas)) / Total de Horas
                    freq_decimal = (100 * (mes_obj.dias_letivos - num_faltas)) / mes_obj.dias_letivos
                    
                    # Formatação com uma casa decimal: :.1f
                    exibidores_porcentagem[nome_mes].value = f"{freq_decimal:.1f}%"
                    
                    soma_frequencias += freq_decimal
                    meses_contabilizados += 1
                except ValueError:
                    exibidores_porcentagem[nome_mes].value = "---%"
            else:
                exibidores_porcentagem[nome_mes].value = "---%"

        # Atualiza a Média Geral com uma casa decimal
        if meses_contabilizados > 0:
            media = soma_frequencias / meses_contabilizados
            texto_media_geral.value = f"Média Anual: {media:.1f}%"
        else:
            texto_media_geral.value = "Média Anual: ---"
            status_final.value = ""

        page.update()

    # --- Criação dos Componentes dos Meses ---
    celulas_meses = []
    for m in meses_dados:
        txt_percent = ft.Text("---%", size=16, color="#444444", weight="w500", width=65)
        exibidores_porcentagem[m.nome] = txt_percent
        
        tf = ft.TextField(
            label=f"Faltas de {m.nome.capitalize()}",
            keyboard_type="number",
            width=160,
            height=45,
            border_radius=8,
            text_align="center",
            on_change=calcular_tudo,
        )
        inputs_list.append(tf)
        
        celulas_meses.append(
            ft.Row(
                [tf, txt_percent],
                alignment="center",
                spacing=20 
            )
        )

    # --- Organização em Matriz ---
    colunas_matriz = []
    for i in range(0, len(celulas_meses), 3):
        grupo = celulas_meses[i:i+3]
        colunas_matriz.append(
            ft.Column(controls=grupo, spacing=15)
        )

    # --- Layout Principal ---
    page.add(
        ft.Column(
            [
                # Logo
                ft.Container(
                    content=ft.Image(src="etemac.png", width=300, height=300, fit="contain"),
                    padding=ft.padding.only(top=20)
                ),
                
                # Cabeçalho
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Cálculo de Frequência Escolar", size=24, color="#777777", weight="w400"),
                            ft.Text("2026", size=80, color="#AAAAAA", weight="w300"),
                        ],
                        horizontal_alignment="center",
                        spacing=0 
                    ),
                    padding=ft.padding.only(top=20, bottom=40)
                ),
                
                # Matriz de Inputs
                ft.Container(
                    content=ft.Row(
                        controls=colunas_matriz,
                        alignment="center",
                        vertical_alignment="start",
                        spacing=40
                    ),
                    padding=ft.padding.only(bottom=40)
                ),
                
                # Rodapé com Resultados
                texto_media_geral,
                status_final,
                ft.Container(height=20),
            ],
            horizontal_alignment="center",
        )
    )

if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")

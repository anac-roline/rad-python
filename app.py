#Fabrício Longo de Araújo
#Ana Caroline Leal do Nascimento

from typing import List, Tuple, Iterable, Dict
import csv, json

def inserir_nota(nome: str, nota: float, caminho: str = "notas.txt") -> bool:
    """
        Insere 'nome,nota' em uma nova linha no arquivo.
        Retorna True em caso de sucesso e False caso haja algum problema previsto.
    """

    # Limpeza e validação do nome
    if not isinstance(nome, str):
        print("[ERRO] Nome deve ser string.")
        return False
    
    nome_limpo = nome.strip()
    if not nome_limpo or not nome_limpo.replace(" ", "").isalpha():
        print(f"[ERRO] Nome inválido: {repr(nome)}")
        return False
    
    # Validação da nota
    try:
        nota_val = float(nota)
    except (ValueError, TypeError):
        print(f"[ERRO] Nota inválida: {repr(nota)} (deve ser número)")
        return False
    
    if not (0 <= nota_val <= 10):
        print(f"[ERRO] Nota fora da faixa [0..10]: {nota_val}")
        return False
    
    # Escrita com tratamento de exceções
    try:
        with open(caminho, "a", encoding="utf-8") as f:
            f.write(f"{nome_limpo},{nota_val}\n")
        return True
    except PermissionError:
        print(f"[ERRO] Sem permissão para escrever em: {caminho}")
        return False
    except FileNotFoundError:
        # Em modo 'a' o Python cria o arquivo se o diretório existir. 
        # Se cair aqui, geralmente é porque o diretório não existe.
        print(f"[ERRO] Caminho inexistente: {caminho}")
        return False
    except Exception as e:
        print(f"[ERRO] Falha inesperada ao escrever: {type(e).__name__} - {e}")
        return False


def listar_notas(caminho: str = "notas.txt") -> List[Tuple[str, float]]:
    """
        Lê o arquivo de notas e retorna uma lista de tuplas (nome, nota).
        Linhas inválidas são ignoradas, com aviso.
    """

    resultados: List[Tuple[str, float]] = []
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if not linha:
                    continue
                partes = [p.strip() for p in linha.split(",")]
                if len(partes) != 2:
                    print("[AVISO] Linha ignorada (formato incorreto):", repr(linha))
                    continue
                nome, nota_txt = partes
                if not nome.replace(" ", "").isalpha():
                    print("[AVISO] Nome inválido, linha ignorada:", repr(linha))
                    continue
                try:
                    nota = float(nota_txt.replace(",", "."))
                except ValueError:
                    print("[AVISO] Nota inválida, linha ignorada:", repr(linha))
                    continue
                resultados.append((nome, nota))
    except FileNotFoundError:
        print(f"[ERRO] Arquivo não encontrado: {caminho}")
    except PermissionError:
        print(f"[ERRO] Permissão negada ao acessar: {caminho}")
    except Exception as e:
        print(f"[ERRO] Falha inesperada ao ler: {type(e).__name__} - {e}")
    return resultados

def exportar_csv(registros: Iterable[tuple], caminho: str = "notas.csv") -> bool:
    """Exporta uma sequência de (nome, nota) para CSV com header."""
    try:
        with open(caminho, "w", newline="", encoding="utf-8") as f:
            campos = ["nome", "nota"]
            w = csv.DictWriter(f, fieldnames=campos, delimiter=",")
            w.writeheader()
            for nome, nota in registros:
                w.writerow({"nome": nome, "nota": float(nota)})
        return True
    except Exception as e:
        print(f"[ERRO] Falha ao exportar CSV: {type(e).__name__} - {e}")
        return False

def importar_csv(caminho: str = "notas.csv"):
    """Importa registros (nome, nota) de um CSV válido."""
    out = []
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            r = csv.DictReader(f, delimiter=",")
            for row in r:
                try:
                    out.append((row["nome"], float(row["nota"])))
                except Exception:
                    print("[AVISO] Linha ignorada no CSV:", row)
    except Exception as e:
        print(f"[ERRO] Falha ao importar CSV: {type(e).__name__} - {e}")
    return out

def exportar_json(registros: Iterable[tuple], caminho: str = "notas.json") -> bool:
    """Exporta uma sequência de (nome, nota) para JSON."""
    dados = {"alunos": [{"nome": n, "nota": float(x)} for n, x in registros]}
    try:
        with open(caminho, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"[ERRO] Falha ao exportar JSON: {type(e).__name__} - {e}")
        return False

def importar_json(caminho: str = "notas.json"):
    """Importa registros (nome, nota) de um JSON válido."""
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            dados = json.load(f)
        return [(a["nome"], float(a["nota"])) for a in dados.get("alunos", [])]
    except Exception as e:
        print(f"[ERRO] Falha ao importar JSON: {type(e).__name__} - {e}")
        return []

def limpar_registros(caminho: str = "notas.txt"):
    """Limpar registros"""
    with open(caminho, "w", encoding="utf-8") as f:
        return

def main():
    while True:
        print()
        print("Escolha uma opção")
        print("1) Inserir aluno(a) e nota")
        print("2) Listar Alunos(as) e notas")
        print("3) Exportar/importar notas em formato JSON")
        print("4) Exportar/importar notas em formato CSV")
        print("5) Limpar registros")
        print("0) Sair")
        try:
            opcao = int(input("> "))
            
            if (opcao == 1):
                try:
                    nome = str(input("Digite o nome do aluno(a): "))
                    nota = float(input("Digite a nota do aluno(a): "))
                    inserir_nota(nome, nota)
                except ValueError:
                    print("Valores de entrada incorretos")
                continue
            elif (opcao == 2):
                notas = listar_notas()
                for nota in notas:
                    print(f"{nota[0]} tem nota {nota[1]}")
                continue
            elif (opcao == 3):
                while True:
                    print("")
                    print("1) Exportar notas em formato JSON")
                    print("2) Importar notas em formato JSON")
                    print("0) Voltar")
                    try:
                        opcao2 = int(input("> "))
                        if (opcao2 == 1):
                            caminho = str(input("Digite o caminho do arquivo: (notas.json) ") or "notas.json")
                            exportar_json(listar_notas(), caminho)
                            continue
                        elif (opcao2 == 2):
                            caminho = str(input("Digite o caminho do arquivo: (notas.json) ") or "notas.json")
                            notas = importar_json(caminho)
                            for nota in notas:
                                inserir_nota(nota[0], nota[1])
                            continue
                        elif (opcao2 == 0):
                            break
                        else:
                            print("Opção inválida. Escolha novamente")
                    except ValueError:
                        print("Opção inválida")
                continue
            elif (opcao == 4):
                while True:
                    print("")
                    print("1) Exportar notas em formato CSV")
                    print("2) Importar notas em formato CSV")
                    print("0) Voltar")
                    try:
                        opcao2 = int(input("> "))
                        if (opcao2 == 1):
                            caminho = str(input("Digite o caminho do arquivo: (notas.csv) ") or "notas.csv")
                            exportar_csv(listar_notas(), caminho)
                            continue
                        elif (opcao2 == 2):
                            caminho = str(input("Digite o caminho do arquivo: (notas.csv) ") or "notas.csv")
                            notas = importar_csv(caminho)
                            for nota in notas:
                                inserir_nota(nota[0], nota[1])
                            continue
                        elif (opcao2 == 0):
                            break
                        else:
                            print("Opção inválida. Escolha novamente")
                    except ValueError:
                        print("Opção inválida")
                continue
            elif (opcao == 5):
                limpar_registros()
            elif (opcao == 0):
                break
            else:
                print("Opção inválida. Escolha novamente")
        except ValueError:
            print("Opção inválida")

    return

if __name__ == "__main__":
    main()


#Desafio em grupos (para o SAVA)
#   **Evolua o sistema de notas** para:
#   - Validar entradas (strings): proíba números em nomes; aceite notas entre 0–10;
#   - Tratar exceções: arquivo ausente, somente leitura, diretório inexistente;
#   - Exportar e importar dados em **CSV** e **JSON**;
#   - Entregar: **.ipynb** ou **.py** + arquivos gerados (.txt, .csv, .json) e **1 slide** com resumo.

#> **Dica:** registre mensagens claras para o usuário e mantenha o código limpo (comentários e funções).
#>> COlocar nomes aleatorios e dos integrantes do grupo para compor os registros... Minimos 15 linhas.
from plantuml_client import PlantUMLClient
import os

def read_plantuml_code(file_name):
    """Lê o conteúdo do arquivo de código PlantUML."""
    try:
        with open(file_name, "r") as file:
            return file.read()
    except Exception as e:
        print(f"Erro ao ler o arquivo '{file_name}': {e}")
        return ""

def generate_use_case_diagram(client):
    """Gera um diagrama de casos de uso."""
    file_path = os.path.join("plantuml_code", "Casos de uso - DoctorWay.puml")
    plantuml_code = read_plantuml_code(file_path)
    save_diagram(client, plantuml_code, "Casos de uso - DoctorWay.png")

def generate_data_diagram(client):
    """Gera um diagrama de casos de uso."""
    file_path = os.path.join("plantuml_code", "Modelo de Dados - DoctorWay.puml")
    plantuml_code = read_plantuml_code(file_path)
    save_diagram(client, plantuml_code, "Modelo de Dados - DoctorWay.png")

def generate_arquitetura_diagram(client):
    """Gera um diagrama de casos de uso."""
    file_path = os.path.join("plantuml_code", "Arquitetura - DoctorWay.puml")
    plantuml_code = read_plantuml_code(file_path)
    save_diagram(client, plantuml_code, "Arquitetura - DoctorWay.png")

def generate_class_diagram(client):
    """Gera um diagrama de classes."""
    file_path = os.path.join("plantuml_code", "Classes - DoctorWay.puml")
    plantuml_code = read_plantuml_code(file_path)
    save_diagram(client, plantuml_code, "Classes - DoctorWay.png")

def generate_sequence_diagram(client):
    """Gera um diagrama de sequência."""
    file_path = os.path.join("plantuml_code", "sequence_diagram.puml")
    plantuml_code = read_plantuml_code(file_path)
    save_diagram(client, plantuml_code, "sequence_diagram.png")

def generate_sequence_diagramUC01(client):
    """Gera um diagrama de sequência."""
    file_path = os.path.join("plantuml_code", "Diagrama de Sequência — UC-01 Agendar Consulta.puml")
    plantuml_code = read_plantuml_code(file_path)
    save_diagram(client, plantuml_code, "Diagrama de Sequência — UC-01 Agendar Consulta.png")

def generate_sequence_diagramUC06(client):
    """Gera um diagrama de sequência."""
    file_path = os.path.join("plantuml_code", "Diagrama de Sequência — UC-06 Registrar Prontuário.puml")
    plantuml_code = read_plantuml_code(file_path)
    save_diagram(client, plantuml_code, "Diagrama de Sequência — UC-06 Registrar Prontuário.png")

def generate_sequence_diagramUC07(client):
    """Gera um diagrama de sequência."""
    file_path = os.path.join("plantuml_code", "Diagrama de Sequência — UC-07 Emitir Receita.puml")
    plantuml_code = read_plantuml_code(file_path)
    save_diagram(client, plantuml_code, "Diagrama de Sequência — UC-07 Emitir Receita.png")

def generate_communication_diagram(client):
    """Gera um diagrama de comunicação."""
    file_path = os.path.join("plantuml_code", "Comunicação - DoctorWay.puml")
    plantuml_code = read_plantuml_code(file_path)
    save_diagram(client, plantuml_code, "Comunicação - DoctorWay.png")


def generate_state_diagram(client):
    """Gera um diagrama de estados."""
    file_path = os.path.join("plantuml_code", "Estados - DoctorWay.puml")
    plantuml_code = read_plantuml_code(file_path)
    save_diagram(client, plantuml_code, "Estados - DoctorWay.png")
    

def generate_component_diagram(client):
    """Gera um diagrama de componentes."""
    file_path = os.path.join("plantuml_code", "Diagrama de Componentes.puml")
    plantuml_code = read_plantuml_code(file_path)
    save_diagram(client, plantuml_code, "Diagrama de Componentes.png")


def generate_deployment_diagram(client):
    """Gera um diagrama de implantação."""
    file_path = os.path.join("plantuml_code", "Implantação - DoctorWay.puml")
    plantuml_code = read_plantuml_code(file_path)
    save_diagram(client, plantuml_code, "Implantação - DoctorWay.png")


def save_diagram(client, plantuml_code, output_filename):
    """Gera e salva o diagrama no formato PNG."""
    try:
        # Cria a pasta 'plantuml_diagrams' caso ela não exista
        os.makedirs("plantuml_diagrams", exist_ok=True)
        
        # Define o caminho completo para salvar o arquivo
        output_path = os.path.join("plantuml_diagrams", output_filename)
        
        # Obtém o conteúdo do diagrama
        png_content = client.fetch_diagram(plantuml_code, "png")
        with open(output_path, "wb") as f:
            f.write(png_content)
        print(f"\nDiagrama salvo como '{output_filename}'")
    except Exception as e:
        print(f"Erro ao gerar o diagrama '{output_filename}': {e}")


def main():
    client = PlantUMLClient()

    print("*" * 150)
    print("Gerando diagramas...")
    generate_state_diagram(client)
    print("*" * 150)
    generate_arquitetura_diagram(client)
    print("*" * 150)
    generate_use_case_diagram(client)
    print("*" * 150)
    generate_class_diagram(client)
    print("*" * 150)
    generate_data_diagram(client)
    print("*" * 150)
    generate_communication_diagram(client)
    print("*" * 150)
    generate_component_diagram(client)
    print("*" * 150)
    generate_deployment_diagram(client)
    print("*" * 150)
    generate_sequence_diagram(client)
    print("*" * 150)
    generate_sequence_diagramUC01(client)
    print("*" * 150)
    generate_sequence_diagramUC06(client)
    print("*" * 150)
    generate_sequence_diagramUC07(client)
    print("*" * 150)
    

    
    print("*" * 150)
    print("Todos os diagramas foram gerados com sucesso.")
    print("*" * 150)


if __name__ == "__main__":
    main()

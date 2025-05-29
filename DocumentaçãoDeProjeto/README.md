# Sistema DoctorWay

## 👥 Integrantes do Grupo

- Gustavo Prehl
- Guilherme Silveira

## 🩺 Sobre o Sistema

**DoctorWay** é um sistema voltado para o agendamento de consultas e a gestão de clínicas médicas. Seu objetivo é modernizar e automatizar os processos administrativos e operacionais de clínicas de pequeno e médio porte, substituindo métodos manuais por uma plataforma digital acessível, segura e eficiente.

O sistema contempla funcionalidades como:

- Agendamento de consultas médicas;
- Cadastro e gerenciamento de pacientes e profissionais de saúde;
- Registro e consulta de prontuários eletrônicos;
- Emissão de receitas e relatórios clínicos;
- Geração de estatísticas administrativas.

A arquitetura do sistema segue uma abordagem modular e em camadas, com clientes web e mobile, uma API REST central e integração com sistemas de pagamento externos.

## 📊 Diagramas do Sistema

Todos os diagramas foram modelados utilizando a ferramenta **PlantUML**. Abaixo estão os diagramas ilustrativos (.png), os arquivos de projeto (.puml) e uma breve descrição do conteúdo de cada um.

---

### Modelo de Casos de Uso
![Modelo de Casos de Uso](./Projeto%20PlantUML%20API/plantuml_diagrams/Casos%20de%20uso%20-%20DoctorWay.png)  
[arquivo - Casos de Uso.puml](./Projeto%20PlantUML%20API/plantuml_code/Casos%20de%20Uso%20-%20DoctorWay.puml)  
**Descrição:** Este diagrama apresenta as principais funcionalidades oferecidas pelo sistema DoctorWay e como cada ator (Paciente, Médico, Atendente e Administrador) interage com elas. Também mostra relacionamentos de inclusão e extensão entre os casos.

---

### Diagrama de Sequência do Sistema

#### UC-01 — Agendar Consulta
![Diagrama de Sequência — UC-01 Agendar Consulta](./Projeto%20PlantUML%20API/plantuml_diagrams/Diagrama%20de%20Sequência%20—%20UC-01%20Agendar%20Consulta.png)  
[arquivo - Diagrama de Sequência — UC-01.puml](./Projeto%20PlantUML%20API/plantuml_code/Diagrama%20de%20Sequência%20—%20UC-01.puml)  
**Descrição:** Demonstra a interação entre paciente, atendente e sistema durante o processo de agendamento de consulta, incluindo a verificação de disponibilidade e envio de notificação.

#### UC-06 — Registrar Prontuário
![Diagrama de Sequência — UC-06 Registrar Prontuário](./Projeto%20PlantUML%20API/plantuml_diagrams/Diagrama%20de%20Sequência%20—%20UC-06%20Registrar%20Prontuário.png)  
[arquivo - Diagrama de Sequência — UC-06.puml](./Projeto%20PlantUML%20API/plantuml_code/Diagrama%20de%20Sequência%20—%20UC-06.puml)  
**Descrição:** Representa o fluxo de ações realizado pelo médico para acessar o prontuário de um paciente, adicionar diagnóstico e prescrição, e encerrar o atendimento.

#### UC-07 — Emitir Receita
![Diagrama de Sequência — UC-07 Emitir Receita](./Projeto%20PlantUML%20API/plantuml_diagrams/Diagrama%20de%20Sequência%20—%20UC-07%20Emitir%20Receita.png)  
[arquivo - Diagrama de Sequência — UC-07.puml](./Projeto%20PlantUML%20API/plantuml_code/Diagrama%20de%20Sequência%20—%20UC-07.puml)  
**Descrição:** Mostra como o médico preenche e envia uma receita, com variações entre envio eletrônico por e-mail e impressão física.

---

### Arquitetura
![Arquitetura](./Projeto%20PlantUML%20API/plantuml_diagrams/Arquitetura%20-%20DoctorWay.png)  
[arquivo - Arquitetura.puml](./Projeto%20PlantUML%20API/plantuml_code/Arquitetura%20-%20DoctorWay.puml)  
**Descrição:** Modelo de três camadas baseado em ArchiMate, destacando os processos de negócio, os serviços de aplicação (como agendamento, prontuário e pagamento) e os componentes técnicos que compõem o sistema, como módulos web/mobile, API REST e banco de dados.

---

### Diagrama de Componentes
![Diagrama de Componentes](./Projeto%20PlantUML%20API/plantuml_diagrams/Diagrama%20de%20Componentes%20-%20DoctorWay.png)  
[arquivo - Diagrama de Componentes.puml](./Projeto%20PlantUML%20API/plantuml_code/Diagrama%20de%20Componentes.puml)  
**Descrição:** Detalha os principais componentes do sistema divididos em módulos (Paciente, Agendamento, Sistema Clínico e Infraestrutura), suas interfaces, conexões e interações com um serviço externo de pagamento.

---

### Implantação
![Implantação](./Projeto%20PlantUML%20API/plantuml_diagrams/Implantação%20-%20DoctorWay.png)  
[arquivo - Implantação.puml](./Projeto%20PlantUML%20API/plantuml_code/Implantação%20-%20DoctorWay.puml)  
**Descrição:** Esquematiza como o sistema DoctorWay é distribuído em ambiente real, incluindo servidores web e banco de dados, cache Redis, totem de autoatendimento, API de pagamento externo e dispositivos locais como impressora.

---

### Classes
![Classes](./Projeto%20PlantUML%20API/plantuml_diagrams/Classes%20-%20DoctorWay.png)  
[arquivo - Classes.puml](./Projeto%20PlantUML%20API/plantuml_code/Classes%20-%20DoctorWay.puml)  
**Descrição:** Mostra as principais classes do sistema, suas propriedades e métodos, com destaque para herança entre Pessoa, Paciente e Médico, além das relações entre Consulta, Receita e Prontuário.

---

### Comunicação
![Comunicação](./Projeto%20PlantUML%20API/plantuml_diagrams/Comunicação%20-%20DoctorWay.png)  
[arquivo - Comunicação.puml](./Projeto%20PlantUML%20API/plantuml_code/Comunicação%20-%20DoctorWay.puml)  
**Descrição:** Descreve como as entidades (paciente, atendente, serviços e banco de dados) trocam mensagens durante o agendamento de uma consulta. É útil para entender o fluxo de dados no sistema.

---

### Estados
![Estados](./Projeto%20PlantUML%20API/plantuml_diagrams/Estados.png)  
[arquivo - Estados.puml](./Projeto%20PlantUML%20API/plantuml_code/Estados%20-%20DoctorWay.puml)  
**Descrição:** Representa os estados possíveis de navegação do sistema desde a tela de login até o fluxo de agendamento de consultas, incluindo transições e ações de entrada e saída em cada estado.

---

### Modelo de Dados
![Modelo de Dados](./Projeto%20PlantUML%20API/plantuml_diagrams/Modelo%20de%20Dados%20-%20DoctorWay.png)  
[arquivo - Modelo de Dados.puml](./Projeto%20PlantUML%20API/plantuml_code/Modelo%20de%20Dados%20-%20DoctorWay.puml)  
**Descrição:** Define as principais entidades do sistema DoctorWay e seus relacionamentos. Esse modelo serve como base para a futura implementação do banco de dados relacional ou NoSQL.


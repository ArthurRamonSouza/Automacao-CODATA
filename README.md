# Automação SEAD PB

Este projeto foi desenvolvido para a **Secretaria de Administração do Estado da Paraíba (SEAD PB)** com o objetivo de automatizar o processo de conferência de dados entre planilhas Excel e o sistema interno da secretaria. A automação permite acessar o sistema, buscar informações com base em matrículas fornecidas, e verificar sua consistência com os dados contidos nas planilhas.

---

## 🛠 **Arquitetura**

### Versões do Fluxo de Arquitetura:
- [V 1.0](https://witeboard.com/6c8afcb0-d19e-11ee-9c5d-c924d7cf9b02)
- [V 2.0](https://witeboard.com/c68501c0-d58b-11ee-961c-eb7ab472700d)
- [V 3.0](https://witeboard.com/5a0e5200-d65b-11ee-b4fb-ddccdd1b1cd8)

---

## ⚙️ **Processos**

1. **Requisitar documento XLSX**.
2. Escolher a planilha específica (opções: `MRO`, `LRO`, `LRO Cedidos`).
3. Inserir a célula inicial (padrão: `G10`).
4. Solicitar as credenciais do usuário (usuário e senha).
5. Acessar o site do sistema: [SEAD Sistema](https://apx.sead.pb.gov.br/SEADApxPrd/hostLogin.jsp).
6. Realizar login com o usuário fornecido.
7. Verificar a tela inicial (SRH/SOP) de acordo com o acesso.
8. Executar a rotina de escolha no sistema (`01 -> 01 -> 01 -> 02`).
9. Abrir o arquivo XLSX.
10. Copiar as matrículas a partir da linha e coluna selecionadas (ex.: linha `02`, coluna `matrícula`).
11. Colar a matrícula no sistema.
12. Copiar os dados de cada página necessária.
13. Apagar os dados do registro escolhido.
14. Colar os dados nas colunas do registro.
15. Iterar para a próxima matrícula.
16. Voltar para a digitação de matrícula no sistema.
17. Repetir os passos a partir do passo **11**.
18. **Condição de parada automática**: linha vazia na planilha.

---

## 📋 **Login e Rotinas do Sistema**

### Login na Página Principal
- **URL**: [https://apx.sead.pb.gov.br/SEADApxPrd/hostLogin.jsp](https://apx.sead.pb.gov.br/SEADApxPrd/hostLogin.jsp)
- **Elementos de Login**:
  - Usuário: `//*[@id="GXUser"]`
  - Senha: `//*[@id="GXPassword"]`
  - Nova Senha: `//*[@id="GXNewPassword"]`
  - Botão Entrar: `//*[@id="GXLoginBtn"]`

### Segunda Tela: Escolha do Sistema
- **SRH**: `//*[@id="POS581"]`

### Login no SRH
- **Elementos de Login**:
  - Usuário: `//*[@id="POS1492"]`
  - Senha: `//*[@id="POS1572"]`
  - Nova Senha: `//*[@id="POS1593"]`
  - Enter.

### Rotina de Escolha no Sistema
1. **Opções do Sistema**:
   - 1 -> Enter: `//*[@id="POS1403"]`
   - 1 -> Enter: `//*[@id="POS1228"]`
   - 1 -> Enter: `//*[@id="POS1643"]`
   - 2 -> Enter: `//*[@id="POS1152"]`
   - 2: `//*[@id="POS1631"]`

2. **Matrícula**:
   - Número -> Enter: `//*[@id="POS1646"]`

---

## 📊 **Dados Extraídos**

### Dados Pessoais:
- **Sexo**: `//*[@id="POS597"]`
- **CPF**: `//*[@id="POS896"]`
- **RG**: `//*[@id="POS666"]`
- **PASEP**: `//*[@id="POS923"]`

### Dados Funcionais:
- **Regime**: `//*[@id="POS741"]`
- **Data de Admissão**: `//*[@id="POS1102"]`

---

## 🖥️ **Ferramentas e Requisitos**

- **Navegador Compatível**: Google Chrome.
- **Processos Realizados**:
  - Comparação de matrículas e dados pessoais/funcionais entre planilhas XLSX e o sistema interno.
- **Condição de Parada**:
  - Linha vazia na planilha selecionada.

---

## 💻 **Código-Fonte**
Repositório do projeto disponível no Replit: [Automação CODATA](https://replit.com/@arthur-ramon-sz/Automacao-CODATA).

---

## 📝 **Notas**
- Este projeto foi testado e está **completo e funcional**.
- Utilizado exclusivamente para fins internos da **SEAD PB**.

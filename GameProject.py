def menu_principal():
    while True:
        print("""Bem-vindo a Fortaleza Vermelha!
        Prepare-se para viver uma aventura de tirar o fôlego! Assuma o papel do personagem principal neste eletrizante jogo interativo e desafie seus limites. Derrote criaturas, encontre tesouros, desvende enigmas, explore cenários, salve o mundo e seja o herói! Mas cuidado! O perigo espreita em cada lugar! Conseguirá reunir coragem e determinação o bastante para atingir seus objetivos e alcançar a vitória? O destino está em suas mãos! Aventure-se!
                              Escrito por Athos Beuren""")
        print("Escolha uma opção:")
        print("1 - Regras e Instruções")
        print("2 - Jogar")
        print("0 - Sair")
        
        opcao = input("Opção escolhida: ")
        
        if opcao == "1":
            menu_1()
        elif opcao == "2":
            menu_2()
            break
        elif opcao == "0":
            print("Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

def menu_1():
    while True:
        print("""Regras:
    
    Antes de começar sua aventura, você deve criar seu personagem determinando seus valores de Habilidade, Vida e Convicção e escolhendo Talentos. Estes valores mudarão durante o jogo, então sugerimos que não escreva diretamente no livro, mas faça uma cópia da Folha de Aventuras onde irá anotar as informações. 
Determinando Habilidade, Vida, Convicção e Talentos:
    
    No início do jogo você recebe 10 créditos (CR) que pode gastar para melhorar suas características e adquirir Talentos, se desejar. Representa sua força e capacidade física. Sua Habilidade inicial é 7. Cada ponto extra custa 2 créditos. Habilidade Representa o seu vigor e saúde. Sua Vida inicial é 20. Dois pontos extras custam 1 crédito. Vida Representa sua confiança e força de vontade. Sua Convicção inicial é 7. Cada ponto extra custa 1 crédito. Convicção Representam habilidades especiais. A cada aventura você poderá usar uma vez cada Talento. Você inicia sem Talentos, mas pode adquiri-los. Cada Talento custa 2 créditos. Talentos : 
- Ataque Poderoso: Reduz automaticamente 5 pontos de Vida de um inimigo. 
- Regeneração Acelerada: Restaura 5 pontos de sua própria Vida. Regeneração 
- Avaliação Precisa: Obtém sucesso imediato em um teste de Habilidade ou Convicção.
    Seus valores mudarão durante o jogo. Entretanto, nunca podem ultrapassar os valores iniciais, a menos que especificamente instruído pelo texto. Se sua Vida for reduzida a zero, você morre e deve reiniciar sua aventura. Itens que restauram a Vida podem ser usados a qualquer momento do jogo, exceto durante um combate. 

    Testando Habilidade e Convicção:
Se tiver que testar sua Habilidade ou sua Convicção, role dois dados de seis faces. Se a soma da jogada for igual ou menor ao valor do índice testado, você teve sucesso. Se for maior, você falhou. | 
Itens e Equipamentos Em sua Folha de Aventuras há um espaço para anotar os itens com os quais você começa cada aventura. Anote também os itens que encontrar — eles podem ser cruciais para seu sucesso! Você pode descartar itens e usar provisões a qualquer momento, exceto em um combate ou quando tiver que testar sua Convicção, riscando-os de sua Folha de Aventuras. 

    Combates: 
    Para enfrentar seus adversários, proceda da seguinte maneira: Role dois dados e some a sua Habilidade. O resultado é a sua Jogada de Ataque. Role dois dados e some a Habilidade do oponente. O resultado é a Jogada de Ataque dele. Quem tiver a maior Jogada de Ataque fere o outro (veja abaixo). Em caso de empate, ambos erram — comece a próxima rodada de combate a partir do passo 1, acima. Quem foi ferido perde dois pontos de Vida. Após fazer as mudanças necessárias na Vida do oponente (ou na sua própria), repita os passos 1 a 4. O combate termina quando a Vida de um de vocês é reduzida a zero (morte). Se tiver que enfrentar mais de um adversário em um mesmo combate, escolha no início de cada rodada qual inimigo você irá atacar e resolva a rodada normalmente contra ele. Contra os outros, mesmo que a sua Jogada de Ataque seja maior, você não irá feri-los, mas apenas se defender do golpe. Porém, se Jogada de Ataque deles for maior, você será ferido. Acerto crítico Sempre que você tirar um duplo seis em sua Jogada de Ataque durante um combate, considere a rolagem um acerto crítico. Ao realizar um acerto crítico, você atinge o adversário mesmo que sua Jogada de Ataque seja menor que a dele – e causa o dobro de dano! O mesmo vale para o inimigo, se ele tirar um duplo seis. 

    Fuga: 
    Você poderá fugir de um combate, mas só quando especificamente instruído pelo texto. Para fugir, teste sua Convicção. Se tiver sucesso, você é ferido mas escapa. Se falhar, você é ferido e deve retomar o combate ou tentar fugir novamente. Ao ser ferido, reduza dois pontos de Vida. Dicas Você vai perceber que se ler as referências em sua ordem numérica elas não farão sentido. É essencial que você leia apenas as referências que for instruído a ler. Talvez seja necessária mais de uma tentativa para encontrar o caminho que pode levá-lo com sucesso ao final de cada jornada. Qualquer jogador, independente dos seus valores de Habilidade, Vida ou Convicção, pode concluir sua busca com sucesso — mas não pense que esta será uma tarefa fácil! Riquezas e glória esperam por você, mas também criaturas e armadilhas mortais
""")
        
        print("0 - Voltar ao Menu Principal")
        
        opcao = input("Opção escolhida: ")
        if opcao == "0":
            print("Voltando ao Menu Principal.\n")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

            
import random

#Simula a jogada de dois dados
def dadoRandomico ():
    import random

    return random.randint(2, 12)

#Combate

vidaInimigo = 1
habilidadeInimigo = 1

def combate(vida, habilidade, vidaInimigo, habilidadeInimigo):
    while vida > 0 or vidaInimigo > 0:
        print("Sua vida está em:", vida)
        print("Sua habilidade é:", habilidade)
        print("A vida do inimigo é:", vidaInimigo)
        print("A habilidade do seu inimigo é:", habilidadeInimigo)
        fugir = int(input("Continuar com o combate? Digite '1' para sim ou '2' para fugir: "))
        if fugir == 1:
                print("O monstro inicia atacando")
                ataqueInimigo = dadoRandomico() + habilidadeInimigo
                print("O ataque dele foi:", ataqueInimigo)
                print("Jogue o seu ataque!")
                ataquePersonagem = dadoRandomico() + habilidade
                print("O seu ataque foi:", ataquePersonagem)
                if ataqueInimigo > ataquePersonagem:
                    vida -= 2
                    print("\033[1;31mSeu inimigo tirou 2 pontos de sua vida\033[0;0m")
                    return vida, vidaInimigo
                elif ataquePersonagem > ataqueInimigo:
                    vidaInimigo -= 2
                    print("\033[1;32mVocê tirou 2 pontos de vida do seu inimigo\033[0;0m")
                    return vida, vidaInimigo
                elif ataquePersonagem == ataqueInimigo:
                    print("\033[1;30mEmpate!\033[0;0m")            
        elif fugir == 2:
                print("Você fugiu")
                break

        if vidaInimigo == 0 or vidaInimigo < 0:
            print("--- Você venceu o combate! ---\nVida restante:", vidaPersonagem)
        elif vidaPersonagem == 0 or vidaPersonagem < 0:
            print("--- Você morreu! ---")

    while vida > 0 or vidaInimigo > 0:
        vidaPersonagem,vidaInimigo = combate(vida, habilidade, vidaInimigo, habilidadeInimigo)

# Testar habilidade ou convicção
def test(ability, difficulty):
        roll = random.randint(1, 6) + random.randint(1, 6)
        if roll <= ability:
            print("Você passou no teste.")
        else:
            print("Você falhou no teste.")
            damage = random.randint(1, 6)
            print(f"Você sofreu {damage} de dano.")
            global vida
            vida -= damage
            if vida <= 0:
                print("Você morreu.")
                exit()

def menu_2():
    # Caracteristicas padrões do personagem
    cred = 10
    habilidade = 7
    vida = 20
    convicção = 7
    talentos = []
    while True:
        print("Bem-vindo à aventura! Crie seu personagem.")
        print(f"Você tem {cred} créditos para gastar.")
        print(f"Habilidade: {habilidade} (custo: 2CR para cada ponto extra)")
        print(f"Vida: {vida} (custo: 1CR para cada 2 pontos extras)")
        print(f"Convicção: {convicção} (custo: 1CR para cada ponto extra)")
        print(f"Talentos: {', '.join(talentos)} (custo: 2CR para cada talento)")
        choice = input("O que você deseja fazer? (habilidade / vida / convicção / talento / finalizar / sair) ")

        if choice == "habilidade":
            if cred >= 2:
                habilidade += 1
                cred -= 2
                print("Habilidade aumentada em 1 ponto.")
            else:
                print("Você não tem créditos suficientes.")
        elif choice == "habilidade":
            print(f"Sua habilidade atual é {habilidade}.")
        elif choice == "vida":
            if cred >= 1:
                vida += 2
                cred -= 1
                print("Vida aumentada em 2 pontos.")
            else:
                print("Você não tem créditos suficientes.")
        elif choice == "convicção":
            if cred >= 1:
                convicção += 1
                cred -= 1
                print("Convicção aumentada em 1 ponto.")
            else:
                print("Você não tem créditos suficientes.")
        elif choice == "talento":
            if cred >= 2:
                new_talento = input("Qual talento você deseja adquirir? (ataque poderoso/regeneração acelerada/avaliação precisa) ")
                if new_talento in talentos:
                    print("Você já possui esse talento.")
                else:
                    talentos.append(new_talento)
                    cred -= 2
                    print(f"Talento {new_talento} adquirido.")
            else:
                print("Você não tem créditos suficientes.")

        elif choice == "finalizar":
            if cred > 0:
                print ("Você ainda tem créditos!")
            else: 
                menu_historia()
                break
                


        elif choice == "sair":
            break

        else:
            print("Opção inválida.")       

def menu_historia():
    print("""A Fortaleza Vermelha
A vida agitada que leva desde muito jovem lhe trouxe inúmeras experiências. Você já pisou em terras distantes e admirou paisagens remotas, conheceu raças diferentes e teve contato com a verdadeira magia. Mas uma coisa sempre esteve presente onde quer que fosse, fizesse o que fizesse: problemas! Chegar a uma aldeia tão comum quanto qualquer outra não deveria surpreendê-lo. Desta vez, porém, você acaba de interromper um funeral. Olhos fundos e apreensivos o observam com desconfiança na medida em que se aproxima lentamente. Algumas mulheres tentam conter o choro, a primeira pá de terra é jogada na cova. Um homem, jovem demais para ser algo além de um sacerdote improvisado, recita algumas palavras enquanto o cadáver embrulhado em um lençol sujo desaparece sob o solo. E então está terminado. A multidão começa a se dispersar. Um homem usando muletas se aproxima de você e, reconhecendo-o como um guerreiro de valor, exclama para outros transeuntes. Eles vêm imediatamente ao seu encontro. Os humildes aldeões rogam para que você acabe com os planos de dois sujeitos tão malignos quanto poderosos, que passaram a se considerar donos dos mais fracos e senhores do povo. Ghanon e Drillgax são bastardos prepotentes com um particular interesse por alquimia. Pessoas têm sumido e atos fúnebres como o que presenciou em sua chegada à aldeia se tornaram rotina. Muitas são as vítimas da dupla sinistra. É seu dever de herói derrotar Ghanon e Drillgax, pois todos sabem que, na verdade, pretendem dominar a população apenas para usá-la como cobaias em experimentos medonhos e satisfazer seus propósitos sombrios. Além de ter uma boa espada adquirida nas florestas do norte, uma armadura de couro gasta e um fiel escudo de metal, você carrega consigo uma provisão que lhe restaura cinco pontos de Vida quando consumida. Você conhece ainda uma magia de fogo, que poderá lançar até três vezes durante sua busca para reduzir automaticamente cinco pontos de Vida do inimigo em um combate. Anote tudo em sua Folha de Aventuras. 
Os sujeitos apontados pelo povo se escondem na Fortaleza Vermelha, apelidada assim devido à cor que assume durante o pôr do sol – mesmo que hoje os aldeões insistam em dizer que seja porque ela é banhada em sangue. Para chegar até o local você terá de cruzar um campo de batalha devastado, onde foram travadas as primeiras tentativas de impedir o domínio A Fortaleza Vermelha dos dois. O lugar fica próximo à aldeia cujos habitantes clamam por socorro, mas a distância deve levar algumas horas para ser percorrida. Quando amanhece, você reúne suas coisas e parte. Sua aventura começa aqui! 
""")
    historia1 ()

def historia1 ():
    resposta = input("Logo uma planície verde e arborizada dá lugar a um campo estéril coberto de fuligem e pontilhado por despojos de guerra. Máquinas de cerco destruídas e lanças enfiadas na terra decoram o gigantesco cemitério a céu aberto, composto por uma centena de esqueletos enegrecidos. Você anda por entre os obstáculos imaginando que a dupla tenha usado catapultas para lançar barris de fogo alquímico sobre o batalhão de soldados que tentou destituí-los do poder. O campo é extremamente acidentado e cheio de trincheiras. Para seguir, você é obrigado a entrar em uma delas. Agora há três opções. Se quiser seguir pela esquerda na passagem, digite 19. Se resolver continuar pela direita, digite 36. Se preferir aproveitar uma escada de madeira escorada na terra, subir e pular para a próxima trincheira, digite 48.")   
    if resposta == 19:
        historia19 ()
    elif resposta == 36:
        historia36 ()
    elif resposta == 48:
        historia48 ()
    else:
        print("Opção inválida")

def historia2 (): 
    input("""Você continua pela trincheira e apressa o passo, mas, de repente, é barrado por um monstro insetoide. À sua frente há um apavorante gorgulho de fogo! Ele remexe a terra em busca de restos de fogo alquímico que não tenham entrado em combustão para se alimentar. Mas você também deve servir ao propósito da criatura. Você empunha sua espada e prepara-se para o combate. Lute! 
    Monstro Gorgulho Abrasador 
    Habilidade: 8 Vida: 9 
    Após duas rodadas de combate você poderá fugir do monstro, mas, se vencer, você limpa o sangue amarelado de sua espada e segue. De qualquer modo, vá para 12.""") 
    


#def historia3 ():
    #Usando os obstáculos do campo de batalha como camuflagem, você corre até as árvores carbonizadas. Elas formam uma barreira atrás da qual você fica escondido enquanto pensa em seus próximos movimentos. De repente, você percebe que está todo encardido, e isso lhe dá uma ideia. Se quiser sujar-se com carvão e aproximar-se sorrateiramente da fortaleza, vá para 16. Se preferir manter a estratégia atual e correr o mais rápido que pode até ela, vá para 38. 


#def historia4 ():
     #Uma substância é disparada da boca de cada um dos lagartos metálicos. Quando você se dá conta de que foi atingido pelo líquido corrosivo, boa parte de sua pele já está fumegando caída a seus pés. Ghanon e Drillgax então se revelam e sorriem admirando a eficácia de sua criação enquanto você olha para seus próprios membros sendo dolorosamente dissolvidos. Sua aventura termina aqui! 
#def historia5 ():
#     O objeto emerge do solo quando você pisa sobre ele. Você se abaixa e retira da terra algo que revela ser uma insígnia de pedra. A pequena chapa de rocha tem formato hexagonal e uma gravura que lembra um brasão de família, apesar de já não preservar grandes detalhes. Você resolve que ficará com ela. Anote a insígnia de pedra em sua Folha de Aventuras e vá para 29. 
#def historia6 ():
#     Você é ágil e bloqueia a nova rajada de setas com seu escudo de metal. Quando a carga termina, você arremessa longe o equipamento irrecuperavelmente danificado. Subtraia um ponto de suas Jogadas de Ataque e risque o item de sua Folha de Aventuras. O anão desembainha uma espada da cintura e gesticula em provocação, chamando-o para o combate. Você não hesita em atacá-lo. Lute! Habilidade Vida Anão Camuflado 7 11 Se vencer, você passa pelo anão pisando sobre seu corpo após dar uma cusparada de desdém sobre o cadáver do adversário inerte. Um traidor a menos a serviço de Ghanon e Drillgax. Vá para 12. 
#def historia7 (): 
#    O cheiro da tinta é agradável e bastante incomum. Atraído, você respira cada vez mais fundo para apreciar o aroma, mas não percebe que começa a ficar letárgico. Em breve você estará dócil como um cordeiro. Talvez a dupla de alquimistas o transforme em um serviçal, talvez em uma cobaia. Sua aventura termina aqui! 
#def historia8 (): 
#    — Eu sou o coveiro, mas você ainda não está morto — diz um velhote estranho que resfria sua testa com um pano úmido. Você leva um susto ao acordar e ver o homem à sua frente. Seus reflexos fazem com que você tente se jogar para trás, mas seu corpo dolorido o impede de tal movimento. — Acalme-se, sou um amigo. Faz parte de meu trabalho resgatar os corpos deste campo de carnificina e dar-lhes um enterro digno, mas suponho que você não necessite dos meus serviços. O velho conta que o encontrou inconsciente, semissoterrado por uma pilha de pedras, e o resgatou. Sua armadura de couro está arruinada e não lhe faltam cortes e escoriações por todo o corpo. Reduza seis pontos de Vida e um ponto de Habilidade pelos ferimentos. Você olha em volta e percebe que ainda está em uma trincheira, mas perdeu um tempo precioso. Se quiser ficar e conversar um pouco mais com o homem, vá para 23. Se resolver agradecer, despedir-se e partir de uma vez, vá para 30. 
#def historia9 (): 
#    Você terá que escalar o pilar que sustenta o arco de pedra no lado do fosso em que está. A tarefa seria mais fácil se não houvesse a necessidade constante de interromper a subida e ficar imóvel por minutos a cada vez que a sentinela em uma das torres desvia a atenção para seu lado. Teste sua Habilidade. Se tiver sucesso, vá para 40. Se falhar, vá para 17. 
#def historia10 (): 
#    A escada o conduz até uma espécie de masmorra malcheirosa. Uma abertura gradeada no alto é a única fonte de ar e luz, mas também parece ser o destino de toda sujeira que é removida do pátio da fortaleza, uma vez que fica na altura do chão do lado externo. Abaixo dela, uma mulher está acorrentada à parede do fundo, caída no chão. Seu estado é lastimável e ela não se move sob a pilha de trapos e cabelos que a escondem. Se quiser ajudá-la, vá para 28. Se preferir abandonar a mulher e continuar pela fortaleza, vá para 24. 
#def historia11 ():
#    Você agarra a corrente e a puxa. Em seguida, algumas pedras se deslocam para dentro da parede mais próxima e deslizam para o lado, revelando uma passagem secreta. Escondida em seu interior há uma escadaria. Você sobre os degraus até chegar diante de uma porta ornada com um símbolo de bronze em alto relevo. O desenho representa uma gota contendo um olho. Na pupila dele há um mecanismo de senha de dois dígitos que podem ser inseridos girando anéis metálicos e posicionando-os nos números escolhidos. Se souber a senha, vá para o número correspondente a ela. Caso contrário, vá para 43. 
#def historia12 ():
#    Depois de seguir tanto quanto pode pelas trincheiras, você sobe alguns degraus cavados na terra e corre esgueirando-se pelo campo assolado. Você andou bastante e já pode ver a Fortaleza Vermelha ao longe, cercada pelas ruínas de outras construções menores. O lugar possui torres altas, das quais um observador poderia visualizar todo o campo de batalha, então você terá que tomar cuidado e contar com a sorte para não ser visto antes de penetrar na fortificação. Ao longo do trajeto até ela há uma fileira de árvores das quais restam apenas os troncos carbonizados. Não muito longe há também os destroços de uma grande construção de madeira e pedra. Se quiser se aproximar da Fortaleza Vermelha seguindo pelas árvores de carvão, vá para 3. Se for pelo prédio arruinado, vá para 31. 
#def historia13 ():
#    Seu pé atravessa a tampa apodrecida de uma latrina e você afunda a perna quase até o joelho nos dejetos acumulados no buraco. O cheiro insuportável ficará impregnado em você e poderá ser sentido à distância, alertando seus inimigos e deixando-o enjoado até que possa lavar-se adequadamente. Reduza um ponto de Convicção e vá para 29. 
#def historia14 ():
#    Não há nada familiar entre as poções que vasculha na prateleira, somente a certeza de que nenhuma delas possui efeitos benéficos. Ainda assim, você pode decidir levar uma dentre três opções que lhe parecem úteis: uma poção verde, que pode ser ácido, uma laranja, que lembra fogo alquímico, ou uma preta, que sugere veneno. Anote a que escolher em sua Folha de Aventuras. Agora, se quiser arrancar os tubos dos indivíduos e interromper a experiência, vá para 33. Se preferir deixar a sala e seguir pela escada, vá para 10. 
#def historia15 ():
#    Você não escapa da rajada. Quando se dá conta de que foi atingindo, seu corpo já está todo cravejado de setas. Talvez algum outro herói faça o seu trabalho e salve os aldeões. Sua aventura termina aqui! 
#def historia16 ():
#    Coberto de carvão, você identifica o que julga ser o melhor trajeto até a fortaleza. Você sai de seu esconderijo nas árvores carbonizadas e se esgueira pelo campo de batalha até um carroção destruído, onde faz uma parada. Agora falta pouco. Teste sua Habilidade. Se tiver sucesso, vá para 20. Se falhar, vá para 49. 
#def historia17 ():
#    Você não escolhe os melhores pontos de apoio em sua subida. Como consequência, tem as palmas de suas mãos feridas e seus músculos judiados. Reduza dois pontos de Vida. Quando termina a escalada você alcança o topo do muro, corre pelo adarve e chega até a guarita da torre mais próxima sem ser visto. Vá para 22. 
#def historia18 ():
#    Você segue o coveiro para fora das trincheiras e começa a coletar os restos mortais que vê pela frente, depositando-os na carroça cem metros mais longe. Você não dá sorte até começar a arrastar um cadáver chamuscado, sob o qual encontra uma espada curta. Depois de deixar o corpo na carroça, você apanha a arma. Ela pode não ser tão eficiente quanto sua espada original, mas deverá servir para compensar a perda – assim você não precisará subtrair um ponto das suas Jogadas de Ataque pela perda dos equipamentos. Quando a carroça está cheia, o coveiro agradece a ajuda e parte. Você retoma seu caminho. Vá para 2
#def historia19 ():
#    Ao longo do trajeto na trincheira você pisa em algo oculto sob uma fina camada de terra. Teste sua Convicção. Se tiver sucesso, vá para 5. Caso contrário, vá para 13.
#def historia20 ():
#    Com grande astúcia você se aproxima dos muros da Fortaleza Vermelha sem ser visto, mas ainda há um fosso inundado que cerca o lugar. Uma ponte levadiça cuja corrente de tração está arrebentada parece ser o caminho comum para dentro da fortificação, mas há também um arco de pedra que cruza o fosso e tem a base fixada próxima a onde você está. Se quiser invadir a Fortaleza Vermelha pela ponte levadiça abaixada, vá para 45. Se preferir escalar o arco de pedra e entrar pelo alto, vá para 9.
#def historia21 (): 
#    Você corre, desvia de alguns obstáculos e salta por cima da pedra investindo contra o anão, mas ele é mais rápido recarregando a besta e disparando. As setas o atingem perfurando sua carne macia e alojando-se entre seus ossos. Você desaba. Enquanto agoniza, o anão se aproxima para acabar com seu sofrimento. Uma seta entre os olhos é o que lhe resta. Sua aventura termina aqui! 
#def historia22 ():
#    A guarita está vazia. Uma escada o leva até um pequeno pátio depois do portão de entrada da fortaleza. Alguns fungos crescem nas paredes externas e, com o sol se pondo, o lugar começa a assumir sua infame coloração vermelho-sangue. Você nota movimentação em uma das janelas altas, talvez um prisioneiro. Hora de entrar! Você empunha sua espada e abre uma porta que dá acesso ao interior da Fortaleza Vermelha. Depois dela, você se depara com uma parede repleta de pequenas decorações metálicas. São diversas cabeças de lagarto que olham em sua direção. Para sua surpresa, ao entrar, a armadilha dispara automaticamente! Role um dado. Se o resultado for 1, 2 ou 3, vá para 4. Se o resultado for 4, 5 ou 6, vá para 35.
#def historia23 ():
#    Ao longo da conversa o homem diz que não foi capaz de resgatar seus pertences. Eles ficaram perdidos sob as pedras. O único item que lhe resta agora é sua espada, mas o fio da arma está péssimo. Subtraia um ponto de suas Jogadas de Ataque A Fortaleza Vermelha e risque os outros itens de sua Folha de Aventuras. Sem seus equipamentos não será fácil derrotar Ghanon e Drillgax. — Você poderia me ajudar a colocar alguns desses infelizes na carroça para eu levá-los ao cemitério. Quem sabe não acaba encontrando algo útil? — sugere o coveiro. Se quiser ajudá-lo, reduza dois pontos de Vida pelo esforço e teste sua Convicção. Se tiver sucesso, vá para 18. Caso contrário, vá para 47. Se preferir poupar suas energias, você agradece ao homem que salvou sua vida e parte (vá para 2). 
#def historia24 (): 
#    Depois de mais algumas passagens, salas e corredores fortaleza adentro, o caminho finalmente termina em uma saleta. Nela não há muito, apenas uma porta de madeira com uma maçaneta de ferro e uma corrente que pende do teto. A ponta da corrente fica na altura de seus olhos e exibe um puxador em forma de cabeça de lagarto. Se quiser abrir a porta, vá para 34. Se preferir puxar a corrente, vá para 11. 
#def historia25 ():
#    Além da bolsa não há mais nada que valha a pena ou chame sua atenção. Você sai do abrigo e retorna, escolhendo um novo caminho. Se quiser seguir pela esquerda na passagem, vá para 19. Se resolver aproveitar uma escada de madeira escorada na terra, subir e pular para a próxima trincheira, vá para 48. 
#def historia26 (): 
#    A senha está correta! Após inseri-la a porta se abre lentamente para dentro de um novo aposento. A luz do sol poente que entra por uma janela ao fundo transforma Ghanon e Drillgax em meras silhuetas à sua frente. Enquanto seus olhos se acostumam à claridade, você empunha sua espada e se prepara para dar fim nos alquimistas. Se você estiver carregando alguma poção e quiser arremessá-la contra a dupla, esta é a hora! Se for uma poção verde, o frasco se quebra liberando uma substância viscosa que em contato com o ar se expande em forma de espuma e retarda os movimentos dos inimigos, reduzindo a Habilidade de ambos em um ponto. Se for uma poção negra, o frasco se quebra liberando um líquido que evapora em uma nuvem tóxica, reduzindo quatro pontos de Vida de cada membro da dupla. Se for uma poção laranja, nada acontece. Ela não passa de um conservante de alimentos. Lute! Habilidade Vida Ghanon 9 16 Drillgax 11 14 Se vencer, vá para 50. 
#def historia27 ():
#    Você é rápido o suficiente, desvia da rajada de setas e tem tempo de pensar no que fazer antes que o anão recarregue a arma e dispare novamente. Se quiser atacá-lo, vá para 21. Se preferir defender-se com seu escudo, vá para 6. A Fortaleza Vermelha 
#def historia28 (): 
#    Você tenta abrir os grilhões que prendem os punhos da prisioneira sem ligar para as unhas longas e aguçadas na ponta dos dedos dela. A mulher começa a acordar aos poucos, parecendo confusa, então você se aproxima e tenta confortá-la dizendo-lhe que ficará tudo bem. De repente, porém, ela o ataca enterrando as garras em seu pescoço! Reduza dois pontos de Vida. Você a empurra para longe e recua. Um corte horrendo acima dos olhos da mulher e uma dúzia de grampos cirúrgicos que seguram o topo do crânio dela confirmam que você chegou tarde para resgatar esta cobaia. O cérebro dela foi removido e substituído por o de uma fera assassina! Com força sobre-humana, ela arranca as correntes da parede e volta a atacá-lo. Lute! Habilidade Vida Garradora 8 8 Se vencer, você deixa a masmorra, retorna até a bifurcação e segue pela direita. Vá para 24. 
#def historia29 ():
#    Mais adiante há uma bifurcação. Enquanto o caminho à sua frente segue por metros incontáveis, uma passagem à direita, escavada como um túnel na terra, leva até a próxima trincheira. Se quiser continuar em frente, vá para 2. Se preferir seguir pelo túnel, vá para 41. 
#def historia30 ():
#    Antes de despedir-se, o velho diz que não foi capaz de resgatar seus pertences. Eles ficaram perdidos sob as pedras. O único item que lhe resta agora é sua espada, mas o fio da arma está péssimo. Subtraia um ponto de suas Jogadas de Ataque e risque os outros itens de sua Folha de Aventuras. Sem seus equipamentos não será fácil derrotar Ghanon e Drillgax, mas você está decidido a tentar. Você agradece ao homem que salvou sua vida e parte. Vá para 2. 
#def historia31 ():
#    Você corre até as ruínas usando os obstáculos do campo de batalha como camuflagem. O local em que chega parece um dia ter sido uma capela. Você cruza sob um arco e escora-se em uma parede de pedra ao lado de um grande sino de bronze caído e enegrecido pelo fogo. Próximo a ele há uma caixa de pedra. Você não encontra fechaduras, mas é incapaz de abrir a tampa dela. Um sulco com uma inscrição na lateral parece ser o encaixe de alguma peça. Se você possuir uma insígnia de pedra, vá para 37. Caso contrário, vá para 20. 
#def historia32 (): 
#    O símbolo da gota com o olho foi pintado no tecido com uma tinta especial, que parece brilhar de forma metálica dependendo do ângulo em que você observa o estandarte. Teste sua Convicção. Se tiver sucesso, vá para 39. Caso contrário, vá para 7. 
#def historia33 (): 
#    Você remove o tubo mais calibroso com um puxão, mas mal consegue contê-lo enquanto ele serpenteia jorrando um líquido escuro e quebrando uma boa quantidade de objetos de vidro. A criatura sobre a mesa começa a convulsionar, o homem engasga com um fluído viscoso que lhe escorre boca afora. Aturdido pelo caos inesperado e sem saber o que fez, você resolve fugir da sala e descer a escada. Vá para 10. 
#def historia34 ():  
#    Assim que você abre a porta, frascos de poção incendiária amarrados na ponta de algumas tiras voam como pêndulos contra você! Role um dado para descobrir quantos o atingem. Para cada frasco que o acertar, reduza dois pontos de Vida. Se ainda possuir seu escudo, ignore um dos frascos que o atingir. Depois, se ainda estiver vivo, você extingue o fogo das poções incendiárias e puxa a corrente. Vá para 11. 
#def historia35 (): 
#    Você desvia de uma substância corrosiva disparada da boca de cada um dos lagartos metálicos. O líquido chia e fumega ao atingir somente a parede. Depois de sobreviver à recepção que lhe aguardava na entrada da fortaleza, você chega a uma bifurcação em um dos corredores internos. Se quiser seguir pela direita, vá para 24. Se preferir ir pela esquerda, vá para 42. 
#def historia36 (): 
#    Mais adiante a trincheira termina na entrada de um abrigo escavado na terra. Uma parte do teto sustentado por vigas está desmoronada, mas ainda é possível entrar no local e explorá-lo. Embaixo de algumas tábuas, e próximo a um braço esquelético cujo dono está soterrado, há uma bolsa de couro. Parece haver algo dentro dela. Se quiser apanhá-la, vá para 44. Se preferir ignorá-la, vá para 25.
#def historia37 (): 
#    Assim que você insere a insígnia no sulco da caixa, a tampa destrava deslocando-se alguns centímetros. Você a abre e revela um forro de veludo no qual repousa um frasco de vidro cheio de um líquido azul. Uma poção de mana! Ao bebê-la, você poderá restaurar suas energias arcanas e utilizar mais duas vezes sua magia de fogo. Anote-a em sua Folha de Aventuras para consumi-la quando quiser. Vá para 20. 
#def historia38 (): 
#    Você dispara rumo à fortaleza, mas, quando está no meio do caminho, algo começa a reluzir no alto da torre principal. Uma grande lente capta e condensa os raios do sol em um feixe de luz fulminante que passa a varrer o campo de batalha tentando focar você! O raio incendeia tudo que atinge e, por mais que corra, você não consegue fugir para sempre. Seu corpo entra em combustão e você dura poucos segundos como uma tocha viva antes de ser completamente incinerado. Sua aventura termina aqui! 
#def historia39 (): 
#    O cheiro da tinta é agradável, mas bastante incomum. Você resolve cobrir o nariz para não arriscar cair em uma nova armadilha da dupla de alquimistas. Examinando a pintura de perto, você nota gravado na pupila do olho o número vinte e seis. Anote a informação em sua Folha de Aventuras. Agora, se quiser entrar na porta, vá para 46. Se preferir descer a escada, vá para 10. 
#def historia40 (): 
#    Você escolhe bons pontos de apoio e termina a escalada sem forçar excessivamente sua musculatura. Em seguida, você alcança o topo do muro, corre pelo adarve e chega até a guarita da torre mais próxima. Sua presença ainda não foi notada. Vá para 22. 
#def historia41 (): 
#    No interior do túnel você cruza por um buraco escavado em uma das laterais. Ele se parece com a entrada da toca de algum animal, então você apressa o passo. Quando está quase deixando a passagem, três hienas carniceiras surgem na saída, barrando seu caminho! Você empunha sua espada e recua alguns passos, mas então ouve rosnados às suas costas. Vindas da toca, outras duas hienas o cercam no túnel apertado. Lute! Habilidade Vida 1ª Hiena Carniceira 6 4 2ª Hiena Carniceira 5 6 3ª Hiena Carniceira 4 6 4ª Hiena Carniceira 6 6 5ª Hiena Carniceira 4 7 Se vencer, vá para 48. 
#def historia42 (): 
#    Ao longo do corredor, alguns estandartes nas paredes laterais exibem o símbolo de uma gota contendo um olho. No fim da passagem há uma escada que desce para o andar inferior, no subsolo. Antes dela há uma porta de madeira à direita. Se quiser investigar um dos estandartes, vá para 32. Se resolver entrar na porta, vá para 46. Se preferir descer a escada, vá para 10. 
#def historia43 (): 
#    Sem possuir a senha correta você é impedido de aprofundar- -se na Fortaleza Vermelha e derrotar Ghanon e Drillgax. Ao invés disso, ao inserir o código errado você dispara uma nova armadilha! O painel numérico recolhe-se para dentro do símbolo de bronze e em seu lugar surge uma mangueira com um bocal dentado que voa em sua direção e se crava em seu abdômen. Imediatamente ela começa a injetar uma espécie de veneno em seu organismo. Você fica paralisado, suas veias tornam-se visíveis sob a pele. Muito em breve você estará morto. Sua aventura termina aqui! 
#def historia44 (): 
#    Ao apanhar a bolsa de couro você descobre tarde demais que a alça dela estava presa em torno de uma viga de madeira rachada. Quando a puxa, a estrutura cede e o teto vem abaixo sobre você. Vá para 8.
#def historia45 (): 
#    Você é discreto ao aproximar-se da ponte e observar. Não há ninguém vigiando a entrada. Quando está atravessando, porém, um monstro lodoso emerge do fosso e usa seus tentáculos para A Fortaleza Vermelha enroscar seus braços e pernas antes que possa reagir! Você consegue arrebentar um ou dois deles, mas o restante é forte o bastante para arrastá-lo para baixo da água e mantê-lo submerso até que se afogue. Sua aventura termina aqui! 
#def historia46 ():
#    O aposento que se revela atrás da porta é uma espécie de laboratório. Frascos, tubos e aparatos alquímicos ocupam os balcões e prateleiras. Uma delas está repleta de poções. No entanto, o que torna a sala pequena são duas mesas grandes ao centro, nas quais repousam um homem e uma criatura horrenda, ambos inconscientes. Fluídos correm de um para o outro através de tubos ligados entre os dois, numa espécie de transfusão – um experimento abominável! Se quiser arrancar os tubos dos indivíduos e interromper a experiência, vá para 33. Se resolver pegar uma poção, vá para 14. Se preferir deixar a sala e seguir pela escada, vá para 10. 
#def historia47 (): 
#    Você segue o coveiro para fora das trincheiras e começa a coletar os restos mortais que vê pela frente, depositando-os na carroça cem metros mais longe. Para seu azar, além de não encontrar nada que lhe possa ser útil, você atrai a atenção de uma hiena carniceira que mordiscava os cadáveres aqui e ali. O animal prefere sua carne fresca e o ataca. Lute! A Fortaleza Vermelha Habilidade Vida Hiena Carniceira 6 8 Se vencer, você resolve que é hora de despedir-se do coveiro e retomar sua busca, seguindo de onde parou. Vá para 2. 
#def historia48 (): 
#    A trincheira seguinte permite que siga em apenas uma direção. A outra passagem está bloqueada pelos destroços de uma balista. No meio do caminho, um anão que estava camuflado com uma capa coberta de terra rola para trás de uma pedra ao perceber sua aproximação. Ele o espia com sua cara enrugada e barba e cabelos ruivos. De repente, ele apanha uma besta de repetição e, acreditando que descobriu seu segredo e veio para matá-lo, dispara uma sequência de setas em sua direção. Teste sua Habilidade. Se tiver sucesso, vá para 27. Se falhar, vá para 15. 
#def historia49 ():
#    Sua camuflagem e movimentos sorrateiros não são páreos para os olhos de uma sentinela que observa do alto de umas das torres da fortaleza. Assim que nota sua aproximação, o vigilante empunha um arco e dispara contra você. O projétil atravessa seu pescoço, matando-o na hora. Sua aventura termina aqui! 
#def historia50 (): 
#    Antes que o sol desapareça no horizonte a dupla de alquimistas está derrotada. A sala em que se encontra agora parece um pequeno pedaço do inferno. Experimentos desumanos estão por toda a parte, perdidos em meio ao espectro vermelho da fortaleza ao pôr do sol. Você retira um enorme funil da boca de um goblinoide obrigado a ingerir sabe-se lá o que, mas a criatura já está sem vida. Ao fim, sua busca por sobreviventes e prisioneiros é infrutífera, mas ao menos tem a certeza de que Ghanon e Drillgax não farão novas vítimas. Os poucos tesouros que encontra no lugar são suficientes para recompensá-lo por seu esforço, visto que jamais desejou algo além de ajudar os mais fracos. No entanto, entre os inúmeros experimentos deixados pelos alquimistas, é possível encontrar descobertas fantásticas que, se usadas para o bem, poderão resultar em grandes avanços e melhorias. Seu retorno à aldeia é marcado por choro, alegria e uma cama confortável em uma fazenda onde pode descansar antes de partir. Em alguns dias você está recuperado e segue seu caminho até esbarrar em novos problemas, tendo como sua fiel escudeira a certeza de que, por mais árduas que sejam as adversidades, o bem sempre triunfa! Fim!



menu_principal()
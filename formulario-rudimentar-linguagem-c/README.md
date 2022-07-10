<div align='center' id='top'>
<img src='./logo-c.png' alt='logo da linguagem C' width="100" />
 
&#xa0;
 
</div>
 
<h1 align='center'>Projeto de Código: Formulário Rudimentar em Linguagem C</h1>
 
<p align='center'>
 
<img alt="GitHub top language" src="https://img.shields.io/github/languages/top/fransilva0/formulario-rudimentar-linguagem-c?color=56BEB8&style=for-the-badge">
 
<img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/fransilva0/formulario-rudimentar-linguagem-c?color=56BEB8&style=for-the-badge">
 
<img alt="GitHub" src="https://img.shields.io/github/license/fransilva0/formulario-rudimentar-linguagem-c?color=56BEB8&style=for-the-badge">
  
</p>
 
<p align='center'>
<a href='#dart-situacional'>Situacional</a> &#xa0; | &#xa0;
<a href='#bulb-sobre-o-projeto'>Sobre o Projeto</a> &#xa0; | &#xa0;
<a href='#sparkles-implementações'>Implementações</a> &#xa0; | &#xa0;
<a href='#triangular_flag_on_post-o-código'>O Código</a> &#xa0; | &#xa0;
<a href='#computer-desenvolvedores'>Desenvolvedores</a> &#xa0; | &#xa0;
<a href='#memo-licença'>Licença</a> &#xa0; | &#xa0;
</p>
 
<br>
 
## :dart: Situacional ##
 
<p> 
   A empresa fictícia Start, produtora de aparelhos tecnológicos, está buscando entendender o que os seus clientes dizem sobre a empresa, para com isso,
   elaborar um plano para o futuro da empresa de modo que esteja alinhada com os clientes atuais e futuros. Para dar início a essse plano, a Start contratou uma equipe
   multidiciplinar e separou seus integrantes em equipes menores, com missões diferentes.
</p>

 
## :bulb: Sobre o Projeto ##
 
<p> 
   A ideia do projeto foi a elaboração de um programa em linguagem C, que apresenta-se um formulário rudimentar (sem nenhuma interface gráfica e com comandos simples da 
   linguagem). As implementações realizadas podem ser conferidas na seção a seguir, tais implementações foram de acordo com o que foi ensinado na matéria de Laboratório e 
   Programação 1, do curso de Bacharelado em Ciência da Computação pela UEPB, ministrado pelo professor Pablo Roberto. 
</p>
 
## :sparkles: Implementações ##
 
:heavy_check_mark: Lista Simples de Perguntas para o Usuário;<br>
:heavy_check_mark: Captação de Resposta usando Lista Encadeada;<br>
:heavy_check_mark: opção de editar resposta caso o usuário tenha escrito errado;<br>
:heavy_check_mark: Arquivo.txt com as Respostas armazenadas;

## :triangular_flag_on_post: O Código ##

<p>
 Começando pelo Main do Projeto, construímos uma lista do tipo char para armazenar todas as 10 perguntas do formulário da Empresa, que foram:
</p>

1) Qual o seu nome?

2) Quantos anos você tem?

3) Qual a sua localização?

4) Você costuma comprar produtos de forma online regularmente, às vezes ou nunca?

5) Como você avalia o atendimento prestado pela nossa equipe durante a pandemia?

6) Os nossos produtos estão abaixo, acima, ou atendem às suas expectativas?

7) Entre aparelhos (notebook, celular) e acessórios (fones de ouvido, teclados, mouse) eletrônicos, o que mais você costuma comprar?

8) O que motivou a compra deste produto?

9) Você recomendaria a empresa para amigos e familiares?

10) Você veio através de uma indicação ( Facebook, Instagram) ?

<p>
 Cada pergunta foi elaborada pensando em seguir uma linha do que a empresa precisaria saber. Sendo a primeira, para catalogar o usuário as suas respostas, a segunda   para entender qual o público majoritário que conhece e compra os produtos da empresa, a terceira pergunta tem o intuito de saber quais filiais da empresa estão próximas a localização do usuário. 
</p>
<p>
 A quarta pergunta, tem o objetivo de entender se o e-comece da empresa é uma opção para os clientes ou se a maioria ainda opta pelo modo loja física. A quinta pergunta situa a empresa no contexto da covid. A sexta, sétima e oitava perguntas foram elaboradas objetivando informações sobre os produtos da empresa de forma a entender como os clientes veem a qualidade, quais aparelhos são mais comprados e por qual motivo. A nona pergunta remetia a recomendação da empresa, o conhecido marketing boca a boca, e por fim, a última questão buscava saber se as mídias sociais estavam atingindo suas metas de captar clientes da melhor forma possível. 
</p>
<p>
 Após a lista de perguntas foi elaborado uma chamada de início para o usuário, utilizando dois printf() com as seguintes mensagens:
</p>

1) Olá, a empresa Start está passando por melhorias e precisa da sua opinião!

2) Por favor, responda as seguintes perguntas com o máximo de sinceridade possível.

<p>
 Após isso a função criar() foi chamada que retornava NULL para a lista encadeada que seria responsável por armazenar todas as respostas do usuário. A função foi construída fora do Main do programa. 
</p>

```
Lista * criar(){
  return NULL;
}

```

<p>
Após a função, foi adicionado um laço For que mostraria as perguntas ordenadamente (da 1° à 10°), receberia a resposta do usuário para a pergunta e por fim chamaria a função insere() que inseria as respostas na lista encadeada enquanto elas fossem diferentes de NULL.
</p>

```
Lista * insere (Lista * inicio,char r[]){
int i = 0;
  Lista *novo;
  novo = (Lista *) malloc(sizeof(Lista));

  while(r[i]!=NULL){
  novo->resposta[i] = r[i];
  i++;
}
if(inicio == NULL){
  novo->prox = NULL;
  return novo;
}
else{
  Lista *pAux = inicio;
  while(pAux->prox != NULL){
  pAux = pAux->prox;
}  
  novo->prox = NULL;
  pAux->prox = novo;
  
  return inicio;
}}

```

<p>
 Após mostrar todas as perguntas e receber todas as respostas do usuário, uma implementação foi realizada para que o usuário pudesse reescrever suas respostas caso ele tivesse errado algo durante o funcionamento do programa. Inicialmente aparece na tela, após o For, uma chamada sobre a possibilidade de reescrever as respostas, juntamente com um menu de escolha, onde o usuário deve optar por escrever ou finalizar o programa:
</p>

```
printf("Deseja reescrever alguma das suas respostas?\n1 - reescrever 2 - finalizar \n\n");

```

<p>
 A resposta do usuário será armazenada na variável questiona, sendo que enquanto questiona for igual a 1, o usuário recebe a lista das respostas seguidas de números onde ele precisará digitar o número correspondente para poder reescrever a resposta presente no número escolhido. Após o usuário reescrever a resposta e confirmar apertando ENTER, a função reescreve() é chamada, onde ela pega a lista, o número digtado pelo usuário e a variável CHAR reposta.
</p>

```
while(questiona==1){

demonstra(lista);
printf("Digite o valor que corresponde a resposta que deseja reescrever!\n");
scanf("%d",&excluivalor);
printf("Reescreva a sua resposta\n");
setbuf(stdin,NULL);
fgets(RecebeResposta,sizeof(RecebeResposta),stdin);
  
lista = reescreve(lista,excluivalor,RecebeResposta);

printf("1 - continuar\n2 - parar\n");
scanf("%d",&questiona);

}

```
<p>
 O programa reescreve a resposta "por cima" da resposta anterior, no mesmo local. Se o número digitado pelo usuário for igual a 1 ele faz apenas o que foi menciondado anteriormente, caso seja maior que 1 ( entre 2 até o 10) a função irá percorer a lista até chegar ao local da resposta ( se for a resposta for n=6, ele percore até n-1), após isso ele faz o que foi mencionado anteriormente (reescreve a resposta "por cima" da resposta anterior, no mesmo local).
</p>

```
Lista * reescreve(Lista * lista,int n,char resposta[]){
  Lista *pont = lista;

if(n==1){
  for(int i =0;i<50;i++){
    pont->resposta[i] = resposta[i];
}}else{
  for(int i =0;i<n-1;i++){
    pont = pont->prox;
  }for(int i =0;i<50;i++){
    pont->resposta[i] = resposta[i];
  }
  }
return lista;
}

```
<p>
 Após isso, o usuário será questionado se ele deseja continuar a modificar as respostas ou se ele concluiu as mudanças e deseja terminar o programa. Caso o usuário opte por continuar modificando as respostas o mesmo processo descrito anteriormente será recomeçado (as funções questiona() e reescreve() serão chamadas novamente ), caso ele opte por encerrar o programa, ele irá receber a lista com a(s) resposta(s) modificada(s) e não fará mais nada.
</p>

<p> 
 Porém, o programa ainda realizará mais três chamadas para concluir o funcionamento total do mesmo, sendo elas as descritas a seguir:
</p>

```
  arquiva(lista,arq);
  LiberaLista(lista);
  apresenta(arq);

```

<p>
 Primeiro as respostas do usuário serão armazenadas no arquivo e em seguida a lista será deletada ( liberando o espaço de armazenamento usado pela lista encadeada durante o funcionamento do programa) e logo ao final, a função apresenta() conclui o programa mostrando ao usuário a lista (que agora estará arquivada no arquivo.txt) com suas respostas finais. 
</p>

<p> O funcionamento do código pode ser verificado usando o site <a href="https://replit.com/">Replit.com</a>. Para isso basta acessar o código presente neste repositório, copiá-lo e colar em um Relps iniciado na plataforma.</p>

## :computer: Desenvolvedores ##
  
:wave: <a href='https://github.com/CarlosEduardo302' target='_blank'>Carlos Eduardo</a><br>
:wave: <a href='https://github.com/fransilva0' target='_blank'>Francileudo Oliveira</a><br>
:wave: <a href='https://github.com/TharcioCBM' target='_blank'>Tharcio</a>

## :memo: Licença ##
 
<p>Este projeto está sob licença MIT.</p>

'''
# coding: utf-8

# Created by Adriell Gomes on Tuesday, June 16, 2020.
# Copyright (c) 2020 @adriellgomes. All rights reserved.

# Lista de Vetores e Matrizes
# --------------------------------------------------------------------------
'''
#include<stdio.h>
#include"cabeçalho.h"
#include<stdlib.h>
int mattt[10][10];
int mattriz[3][3];
int vetor14[3];
int vetor[10];
int ka;
int ma = -999, me = 999;
int matriz2[2][3];
float numer[10];
int matriz4[4][4];
int main(void)
{
	int x,y,z,n,ku=0,m = 0;
	float j = 0, g;
	float k;
	
	
	
	printf("\nqual parte da lista voce deseja acessar:\ncaso digite 1:(questao 1 a 6)-matrizes\ncaso digite 2:(questao 7 a 14)-vetores");
	
		
		
			
		
			printf("\nqual questao deseja executar:\n");
			printf("\nquestao:");
			scanf_s("%d", &x);
			switch (x)
			{

				//----------------------------------------------------------------------------------------------------------
				// questão 1 da lista de vetores
				//maior valor de um vetor de 10 valores
			case 1:
				printf("\n\t\t\t\nquestao 1 da lista de vetores\n");
				printf("\nmaior valor de um vetor de 10 valores\n");

				
				montar10(vetor);
				printar10(vetor);
				ka = maior(vetor);
				
				printf("\n\no maior valor usando a funcao eh %i\n\n", ka);
				
				break;
				
				//-------------------------------------------------------------------------------------------------------------------
					//questão 2 da lista de vetores
				//maior valor, menor valor, e diferença entre estes de um vetor de 10 valores
			case 2:
				printf("\n\t\t\t\nquestao 2 da lista de vetores\n");
				printf("\nmaior valor , menor valor, e diferenca entre estes de um vetor de 10 valores\n");

			montar10(vetor);
			printar10(vetor);
			ma=maior(vetor);
			me=menor(vetor);
				
				printf("\no maior valor do vetor eh:%i\n", ma);
				printf("\no menor valor do vetor eh:%i\n", me);
				printf("\na diferenca eh: %i\n", maior(vetor)- menor(vetor));
				break;
				//-------------------------------------------------------------------------------------------------------------
					//questão 3 da lista de vetores
				//números impares do vetor de 10 valores
			case 3:
				printf("\n\t\t\t\nquestao 3 da lista de vetores\n");
				printf("\nnumeros impares do vetor de 10 valores\n");
				montar10(vetor);
				printar10(vetor);
				
				imp(vetor);
				break;
				//----------------------------------------------------------------------------------------------------------------

					//questão 4 da lista de vetores
				//números primos do vetor de 10 valores
			case 4:
				printf("\n\t\t\t\nquestao 4 da lista de vetores\n");
				printf("\nnumeros primos do vetor de 10 valores\n");
				int mprimo[10];
				int qprimo;

				for (n = 0; n < 10; n++)
				{
					printf("\nimprima o valor %i do vetor\n", n);
					scanf_s("%d", &mprimo[n]);
				}
				printf("\nos valores do vetor sao:\n");
				printf("\n[");
				for (n = 0; n < 10; n++)
				{
					
					printf(" %d,", mprimo[n]);

				}
				printf("\b]\n");
				printf("\nos valores primos sao:\n");
				for (n = 0; n < 10; n++)
				{

					qprimo = primo(mprimo[n]);
					if (qprimo == 1)
					{
						printf("\nvalor(%d):%d\n", n, mprimo[n]);
					}

				}
				break;
				//--------------------------------------------------------------------------------------------------------------
					//questão 5 da lista de vetores
				//pesquisa entre valores selecionados no vetor de 10 valores e printa
			case 5:
				printf("\n\t\t\t\nquestao 5 da lista de vetores\n");
				printf("\npesquisa entre valores selecionados no vetor de 10 valores e printa\n");

				int numeros[10];
				int digito;
				for (n = 0; n < 10; n++)
				{
					printf("\nimprima o valor %i do vetor\n", n);
					scanf_s("%d", &numeros[n]);
				}
				printf("\nos valores do vetor sao:\n");
				printf("\n[");
				for (n = 0; n < 10; n++)
				{
					
					printf(" %d,", numeros[n]);

				}
				printf("\b]\n");

				printf("\ndigite um numero\n");
				scanf_s("%d", &digito);
				for (n = 0; n < 10; n++)
				{
					if (digito == numeros[n])
					{
						printf("\nvalor(%d):%d\n", n, numeros[n]);
						ku++;
					}







				}
				if (ku == 0)
				{

					printf("\no numero solicitado nao se encontra alocado no vetor\n\n");
				}
				break;
				//--------------------------------------------------------------------------------------------------------------
					//questão 6 da lista de vetores
				//impede que número de repita no prenchimento do vetor de 10 valores
			case 6:
				printf("\n\t\t\t\nquestao 6 da lista de vetores\n");
				printf("\nimpede que numero de repita no prenchimento do vetor de 10 valores\n");
				
				for (n = 0; n < 10; n++)
				{
					printf("\nimprima o valor %i do vetor\n", n);
					scanf_s("%f", &numer[n]);
					

					for (ka = 1; ka < n; ka++)
					{
						if (numer[n] == numer[ka])
						{
							printf("\no valor digitado ja existe,imprima outro valor %i do vetor\n", n);
							scanf_s("%f", &numer[n]);
							if (numer[n] == numer[ka])
							{
								printf("\no valor digitado ja existe,imprima outro valor %i do vetor\n", n);
								scanf_s("%f", &numer[n]);
							}

						}
					}
				}
				printf("\n[");
				for (n = 0; n < 10; n++)
				{
					
					printf(" %.2f,", numer[n]);

				}
				printf("\b]\n");


				break;



			
			
				
				
				
			case 7:
					//--------------------------------------------------------------------------------------------------------------
				//questão 7 da lista (matrizes)
				//preencher matriz 3x3 e mostrar
				printf("\n\t\t\t\nquestao 7 da lista de matrizes\n");
				printf("\npreencher matriz 3x3 e mostrar\n");
					montar3x3(mattriz);
					printar3x3(mattriz);

				

					break;
					//--------------------------------------------------------------------------------------------------------------
					//questão 8 da lista (matrizes)
					//multiplica todos os elementos e uma matriz 3x3 por 2 e printa
				case 8:
					printf("\n\t\t\t\nquestao 8 da lista de matrizes\n");
					printf("\nmultiplica todos os elementos e uma matriz 3x3 por 2 e printa\n");
					montar3x3(mattriz);
					printar3x3(mattriz);
					
					
						dobro(mattriz);
					break;
					//--------------------------------------------------------------------------------------------------------------
					//questão 9 da lista (matrizes)
					//soma os 6 valores numéricos de uma matriz 2x3
				case 9:
					printf("\n\t\t\t\nquestao 9 da lista de matrizes\n");
					printf("\nsoma os 6 valores numericos de uma matriz 2x3\n");
					montar2x3(matriz2);
					printar2x3(matriz2);
					printf("\n\na soma de todos os elementos da matriz eh: (%i)\n\n",soma(matriz2));

					break;
					//--------------------------------------------------------------------------------------------------------------
					//questão 10 da lista (matrizes)
					//preencher matriz 4x4 e mostrar diagonal principal
				case 10:
					printf("\n\t\t\t\nquestao 10 da lista de matrizes\n");
					printf("\npreencher matriz 4x4 e mostrar diagonal principal\n");
					montar4x4(matriz4);
					printar4x4(matriz4);
					diagonal(matriz4);

					break;
					//--------------------------------------------------------------------------------------------------------------
					//questão 11 da lista (matrizes)
					//preenche matriz 3x3 e imprime todos os elementos exceto os da diagonal principal
				case 11:
					printf("\n\t\t\t\nquestao 11 da lista de matrizes\n");
					printf("\npreenche matriz 3x3 e imprime todos os elementos exceto os da diagonal principal\n");
					montar3x3(mattriz);
					printar3x3(mattriz);
					antidiagonal(mattriz);

					break;
					//--------------------------------------------------------------------------------------------------------------
					//questão 12 da lista (matrizes)
					//diz a pior nota dentre 3 provas de 10 alunos e mostra a contagem total
				case 12:

					printf("\n\t\t\t\nquestao 12 da lista de matrizes\n");
					printf("\ndiz a pior nota dentre 3 provas de 10 alunos e mostra a contagem total\n");
					int vetor[10][3];

					montar10x3(vetor);
					printar10x3(vetor);
					contar(vetor);
					system("pause");

					//return 0;
					
					break;
					//--------------------------------------------------------------------------------------------------------------
					//questão 13 da lista (matrizes)
					//imprime matriz conforme a formula para suas dimenções
				case 13:
					printf("\n\t\t\t\nquestao 13 da lista de matrizes\n");
					printf("\nimprime matriz conforme a formula para suas dimencoes\n");
					montar10x10(mattt);
					printar10x10(mattt);
					
					system("pause");

					break;
					//--------------------------------------------------------------------------------------------------------------
					//questão 14 da lista (matrizes)
					//soma as colunas da matriz e transpõe para um vetor
				case 14:
					printf("\n\t\t\t\nquestao 14 da lista de matrizes\n");
					printf("\nsoma as colunas da matriz e transpoe para um vetor\n");
					montar3x3(mattriz);
					printar3x3(mattriz);
					alocavetor(mattriz,vetor14);
					printalocavetor(vetor14);
					break;
				}



			
		
		
                












	system("pause");
	
	return(0);
}


# coding: utf-8

# Created by Adriell Gomes on Tuesday, June 16, 2020.
# Copyright (c) 2020 @adriellgomes. All rights reserved.

# --------------------------------------------------------------------------

#include<stdio.h>
#include<stdlib.h>
#include"funcoes.h"

int main(void)
{
	printf("\n \t\t\t** soma de dois valores **\n");
	float as, bs ;//soma( Exercício dado em sala, e no material de aula 2)

	printf("\ndigite o valor de a\n");
	scanf_s("%f", &as);
	printf("\ndigite o valor de b\n");
	scanf_s("%f", &bs);
	
	
	float x = soma(as, bs);

	printf("\n\n(a + b) : %.2f + %.2f = %.2f\n", as, bs, x);

	//--------------------------------------------------------------------------------------------------------------------------------------------------
	printf("\n \t\t\t** subtracao de dois valores **\n");
	float asu, bsu ;//subtração( Exercício dado em sala, e no material de aula 2)

	printf("\ndigite o valor de a\n");
	scanf_s("%f", &asu);
	printf("\ndigite o valor de b\n");
	scanf_s("%f", &bsu);
	
	float y = subtracao(asu, bsu);

	printf("\n(a - b) : %.2f - %.2f = %.2f\n", asu, bsu, y);

	//--------------------------------------------------------------------------------------------------------------------------------------------------
	printf("\n \t\t\t** divisao de dois valores **\n");
	float ad, bd ;//divisão( Exercício dado em sala, e no material de aula 2)

	printf("\ndigite o valor de a\n");
	scanf_s("%f", &ad);
	printf("\ndigite o valor de b\n");
	scanf_s("%f", &bd);
	printf("\ndigite o valor de c\n");
	

	float z = divisao(ad, bd);

	printf("\n(a / b) : %.2f / %.2f = %.2f\n", ad, bd, z);

	//--------------------------------------------------------------------------------------------------------------------------------------------------
	printf("\n \t\t\t** multiplicacao de dois valores **\n");
	float am, bm ;//multiplicação( Exercício dado em sala, e no material de aula 2)

	printf("\ndigite o valor de a\n");
	scanf_s("%f", &am);
	printf("\ndigite o valor de b\n");
	scanf_s("%f", &bm);
	

	float w = multiplicacao(am, bm);

	printf("\n(a * b) : %.2f * %.2f = %.2f\n\n", am, bm, w);

	//--------------------------------------------------------------------------------------------------------------------------------------------------
	printf("\n \t\t\t** fatorial de numero **\n");
	int fact1;//fatorial (Exercício no material da aula 2) e (Questão 9 da lista de exercícios sobre funções e biblioteca)
	

	printf("\ndigite o valor do numero que se deseja obter a fatorial\n");
	scanf_s("%d", &fact1);

	int e = fatorial(fact1);

	printf("\n%d! = %d\n", fact1, e);

	//--------------------------------------------------------------------------------------------------------------------------------------------------
	printf("\n \t\t\t** saber se o numero eh primo **\n");
	int prim;//número primo (Exercício no material da aula 2)
	
	printf("\ndigite o numero que deseja saber se e primo\n");
	scanf_s("%d", &prim); 

	if (primo(prim) == 1)
	{
		printf("\n %d = numero primo\n",prim);
	}
	else
	{
		printf("\n %d = numero nao primo\n",prim);
	}

	//--------------------------------------------------------------------------------------------------------------------------------------------------
	printf("\n \t\t\t** calculadora de cosseno **\n");
	float d;//cosseno (Exercício no material da aula 2 e na lista de execícios sobre funções e biblioteca)

	printf("\ndigite o valor do angulo para saber seu cosseno\n");
	scanf_s("%f", &d);
 
	float ang = d * 3.141593 / 180;

	
	printf("\n o cosseno de %.2f = %.3f\n", d, cosseno(ang));

	//--------------------------------------------------------------------------------------------------------------------------------------------------
	printf("\n \t\t\t** media de 2 notas **\n");
	float notaa, notab;//média das notas(Questão 3 da lista de exercícios sobre funções e biblioteca)

	printf("\n diga a nota 1\n");
	scanf_s("%f",&notaa);
	printf("\n diga a nota 2\n");
	scanf_s("%f",&notab);

	float media = medianotas(notaa, notab);
	printf("\n media : %.2f \n", medianotas(notaa, notab));
	if (media >=5) printf("situacao : aprovado\n");
	else printf("situacao :  reprovado\n");

	//--------------------------------------------------------------------------------------------------------------------------------------------------
	printf("\n \t** calculadora de raizes de equacao de segundo grau **\n");
	float va, vb, vc;//equação de segundo grau(Questão 4 da lista de exercícios sobre funções e biblioteca)
	printf("\n diga o valor de a \n");
	scanf_s("%f", &va);
	printf("\n diga o valor de b \n");
	scanf_s("%f", &vb);
	printf("\n diga o valor de c \n");
	scanf_s("%f", &vc);

	float valraiz1 = raizx1(va, vb, vc);
	float valraiz2 = raizx2(va, vb, vc);

	printf("\n a raiz 1 e %.4f\n",valraiz1 );
	printf("\n a raiz 2 e %.4f\n",valraiz2 );

	//--------------------------------------------------------------------------------------------------------------------------------------------------
	printf("\n \t\t\t** diferenciador de triangulos **\n");
	float l1, l2, l3;//lados do triângulo(Questão 5 da lista de exercícios sobre funções e biblioteca)
	printf("\ndiga os lados do triangulo\n");
	printf("\n diga o lado 1\n");
	scanf_s("%f", &l1);
	printf("\n diga o lado 2\n");
	scanf_s("%f", &l2);
	printf("\n diga o lado 3\n");
	scanf_s("%f", &l3);

	int resp = triangulo(l1, l2, l3);

	switch (resp)
	{
	case 0: printf("\n nao existe triangulo com lado zero\n");
		break;
	case 1: printf("\n triangulo equilatero\n");
		break;
	case 2: printf("\n triangulo isoceles\n");
		break;
	case 3: printf("\n triangulo escaleno\n");
		break;
	case 4: printf("\n os lados nao podem formar um triangulo\n");
		break;
	case 5: printf("\n nao existe triangulo com valor negativo\n");
		break;
	}

	//--------------------------------------------------------------------------------------------------------------------------------------------------
	printf("\n \t\t\t** calculadora de media ponderada **\n");
	float nota1, nota2;//media ponderada(Questão 6 da lista de exercícios sobre funções e biblioteca)
	printf("\n diga a nota da n1(peso 2)\n");
	scanf_s("%f", &nota1);	
	printf("\n diga a nota da n2(peso 3)\n");
	scanf_s("%f", &nota2);
	

	float mediaponde = tresnotas(nota1, nota2);
	
	if (mediaponde >= 7)
	{
		printf("\n nota: %.1f \n", mediaponde);
		printf("\n situacao: aprovado\n");
	}
	else
	{
		printf("\n nota: %.1f \n", mediaponde);
		printf("\n situacao: reprovado\n");
	}
	//--------------------------------------------------------------------------------------------------------------------------------------------------
	printf("\n \t\t** quanto o aluno precisa tirar na af **\n");//complemento na af(Questão 8 da lista de exercícios sobre funções e biblioteca)
	
	float complemento, valaf;
	
	if (mediaponde < 7)
	{
		 valaf = af(mediaponde);
		printf("\n o aluno vai precisar tirar %.1f para passar na af\n\n", valaf);
	}

	//--------------------------------------------------------------------------------------------------------------------------------------------------
	printf("\n \t\t\t** comparador de crescimento anual entre duas cidades **\n"); //(Questão 10 da lista de exercícios sobre funções e biblioteca)


	float cidadea, cidadeb, crescimentoa, crescimentob;//comparador de crescimento de cidades
	
	printf("\n ponha a populacao da cidade a(em milhares de habitantes)\n");
	scanf_s("%f", &cidadea);
	printf("\n ponha a populacao da cidade b(em milhares de habitantes)\n");
	scanf_s("%f", &cidadeb);
	printf("\n ponha a taxa de crescimento anual da cidade a ( de 0 a 100 por cento)\n");
	scanf_s("%f", &crescimentoa);
	printf("\n ponha a taxa de crescimento anual da cidade b ( de 0 a 100 por cento)\n");
	scanf_s("%f", &crescimentob);
	float ka = cidades(cidadea, crescimentoa, cidadeb, crescimentob);//no primeiro ano não tem crescimento

	printf("\n ira demorar %.0f anos para a populacao da cidade a ser maior que a populacao da cidade b\n",ka);
	//--------------------------------------------------------------------------------------------------------------------------------------------------
		   // Questão 11
	double serie(double nserie)
	{
		double serieres = 0;
		int j = 0;

		for (int i = 25; i >= 1; i--)
		{
			j++;
				if ((i % 2) == 1)
				{
					serieres = serieres + (pow(nserie, i) / j);
				}
				else
				{
					serieres = serieres - (pow(nserie, i) / j);
				}
		}

		return serieres;

	}

	// Questão 12
	double seriedes()
	{
		double respserie = 0;
		double j = 0;

		for (double i = 100; i >= 1; i--)
		{
	
			respserie = respserie + (i / fatorial(j));
			j++;

		}

		return respserie;
	}

	// Questão 13
	double serie13(double entradauser)
	{
		double resserie13 = entradauser;
		int posneg = 0;

		for (int i = 3; i <= 13; i += 2)
		{
			if (posneg == 0)
			{
				resserie13 -= pow(entradauser, i) / fatorial(i);
				posneg = 1;
			}
			else
			{
				resserie13 += pow(entradauser, i) / fatorial(i);
				posneg = 0;
			}

		}
		return resserie13;
	}

	// Questão 14
	double serie14(double userentrada)
	{
		double resserie14 = 0;
		int i = 0;

		for ( i = 0; i <= 20; i++)
		{
			resserie14 += pow(userentrada, i) / fatorial(i);
		}

		return resserie14;
	}

	// Questão 15
	double serie15(double valusuario)
	{
		double resserie15 = 0;
		int posneg = 0;

		for (int i = 0; i <= 20; i += 2)
		{
			if (posneg == 0)
			{
				resserie15 -= pow(valusuario, i) / fatorial(i);
				posneg = 1;
			}
			else
			{
				resserie15 += pow(valusuario, i) / fatorial(i);
				posneg = 0;
			}
		}
		return resserie15;
}
	
	
	system("pause");
	return(0);
}
#include<stdio.h>
int maior(int var1[10])
{
	int n;
	int p = -999;
	for (n = 0; n < 10; n++)
	{
		if (var1[n] > p)
		{
			p = var1[n];


		}

	}
	return(p);
}
int menor(int var1[10])
{
	int n;
	int p = 999;
	for (n = 0; n < 10; n++)
	{
		if (var1[n] < p)
		{
			p = var1[n];


		}

	}
	return(p);



}
int imp(int var1[10])
{
	int n;
	
	int a;
		
		printf("\nos valores impar do vetor sao:\n");
				printf("\n[");
for (a = 0; a < 10; a++)
{

	if ((var1[a] % 2)==1)
	 {
		printf(" %i,", var1[a]);
	 }
	
					

}
printf("\b]\n");
				return(0);
}
int primo(int var1)
{
	int valor = var1,cont = 0;
	while (valor > 1)
	{
		int primo = var1 % valor;
		valor--;
		if (primo==0)
		{
			cont++;
		}
	}
	if (var1 == 4)
	{
		return(0);
	}
	if (cont <= 2)
	{
		return(1);
	}
	
	
	
}
int dobro(int var1[3][3])
{
	int a,b;
	int vetor[3][3];
	for(a=0;a<3;a++)
	{
		for(b=0;b<3;b++)
		{
			vetor[a][b]=2*var1[a][b];

		}
	}
	printf("\no dobro da matriz printada eh:\n");
		
		for (a = 0; a <3; a++)
		{
			printf("\n[");
			for (b = 0; b <3; b++)
			{
				printf(" %i ", vetor[a][b]);
				printf("\t");
			}
			printf("]");
		}
		printf("\n\n");
		return(0);

	

}
int soma(int var1[2][3])
{
	int n, m;
	int soma=0;
	for (n = 0; n < 2; n++)
	{
		for (m = 0; m < 3; m++)
		{
			soma = soma + var1[n][m];
 
		}
	}
	return(soma);
}
int diagonal(int var1[4][4])
{
	printf("\n\na matriz diagonal formada eh:\n\n");
	
	int a,b;
	for(a=0;a<4;a++)
	{
		printf("\n[");
		for(b=0;b<4;b++)
		{
			if (a == b)
			{
              printf(" %i ",  var1[a][b]);
				
			}
			else
			{
				printf("\t");
			}
			

		}
		printf("\t");
	    printf("]");
	
	}
	printf("\n\n");
		
			return(0);		

				

}
int antidiagonal(int var1[3][3])
{
	printf("\n\na matriz  formada eh:\n\n");
	
	int a,b;
	for(a=0;a<3;a++)
	{
		printf("\n[");
		for(b=0;b<3;b++)
		{
			if (a == b)
			{
				if (a == 2 && b == 2)
					printf("   ");
				else
					printf("\t");
				
			}
			else
			{
				if (b == 2)
					printf(" %i ",  var1[a][b]);
				else
					printf(" %i\t",  var1[a][b]);
			}
			

		}
	    printf("]");
	
	}
	printf("\n\n");
			return(0);		
}
int montar10x3(int var1[10][3])
{
	int entrada;
	int a, b;
	for (a = 0; a < 10; a++)
	{
		for (b = 0; b < 3; b++)
		{
			printf("\ndiga a nota [%i] do aluno [%i]\n", b + 1, a + 1);
			scanf_s("%d", &entrada);
			var1[a][b] = entrada;
		}

	}
	return(var1[10][3]);
}
	int printar10x3(int var1[10][3])
	{
		printf("\na matriz printada eh:\n");
		int a, b;
		for (a = 0; a < 10; a++)
		{
			printf("\n[");
			for (b = 0; b < 3; b++)
			{
				printf(" %i ", var1[a][b]);
				printf("\t");
			}
			printf("]");
		}
		printf("\n\n");
		return(var1[10][3]);
	}
	int contar(int var1[10][3])
	{
		printf("\n");
		int a, conta = 0, contc = 0, contb = 0;
		for (a = 0; a < 10; a++)
		{
			if ((var1[a][0] < var1[a][1]) && (var1[a][0] < var1[a][2]))
			{
				conta++;
				printf("\no aluno(%i) teve como pior nota a nota da prova 1\n",a+1);

			}
			if ((var1[a][1] < var1[a][0]) && (var1[a][1] < var1[a][2]))
			{
				contb++;
				printf("\no aluno(%i) teve como pior nota a nota da prova 2\n",a+1);

			}
			if ((var1[a][2] < var1[a][1]) && (var1[a][2] < var1[a][0]))
			{
				contc++;
				printf("\no aluno(%i) teve como pior nota  a nota da prova 3\n",a+1);

			}
			

		}
		printf("\no resultado foi:\n");
		printf("\n %i alunos tiveram a primeira nota como pior nota das 3 provas\n", conta);
		printf("\n %i alunos tiveram a segunda nota como pior nota das 3 provas\n", contb);
		printf("\n %i alunos tiveram a terceira nota como pior nota das 3 provas\n\n", contc);
		return(0);
	}
	int montar10x10(int var1[10][10])
{
	int entrada;
	int a, b;
	for (a = 0; a < 10; a++)
	{
		for (b = 0; b < 10; b++)
		{
			//printf("\ndiga o valor [%i][%i]\n", a + 1, b + 1);
			//scanf_s("%d", &entrada);
			//var1[a][b] = entrada;
			if(a < b)
			{var1[a][b] = 2*(a) + 7*(b)- 2;}
			if(a == b)
			{var1[a][b] = 3*(a)*2 - 1;}
			if(a > b)
			{var1[a][b]= 4*(a)*3 + 5*(b)*2 + 1;}
			


			
		}

	}
	
	return(var1[10][10]);
}
	int printar10x10(int var1[10][10])
	{
		printf("\na matriz printada eh:\n");
		int a, b;
		for (a = 0; a < 10; a++)
		{
			printf("\n[");
			for (b = 0; b < 10; b++)
			{
				
				printf("%i\t", var1[a][b]);
				
				
			}
			printf("]");
		}
		return(var1[10][10]);
	}
	int montar3x3(int var1[3][3])
{
	int entrada;
	int a, b;
	for (a = 0; a < 3; a++)
	{
		for (b = 0; b < 3; b++)
		{
			printf("\ndiga o valor [%i][%i]\n", a + 1, b + 1);
			scanf_s("%d", &entrada);
			var1[a][b] = entrada;
		}

	}
	return(var1[3][3]);
}
	int printar3x3(int var1[3][3])
	{
		printf("\na matriz printada eh:\n");
		int a, b;
		for (a = 0; a <3; a++)
		{
			printf("\n[");
			for (b = 0; b <3; b++)
			{
				
					printf(" %i \t", var1[a][b]);
			}
			printf("]");
		}
		printf("\n\n");
		return(var1[3][3]);
	}
	int alocavetor(int var1[3][3],int var2[3])
	{
		int a,b,valor;
		for(a=0;a<3;a++)
		{
			var2[a] =var1[0][a]+var1[1][a]+var1[2][a]; 
		}
		return(var2[3]);


	}
	int printalocavetor(int var1[3])
	{
		printf("\na matriz criada da soma das colunas eh:\n");
		int a;
		printf("\n[");
				for (a = 0; a <3; a++)
				{
					
					printf(" %i,",var1[a]);

				}
				printf("\b]\n");

				return(0);

	}
	int montar10(int var1[10])
{
	int entrada;
	int a ;
	for (a = 0; a < 10; a++)
	{
	
			
			printf("\ndiga o valor %d da matriz\n", a);
					scanf_s("%i", &var1[a]);
		
			
			
			
		

	}
	return(var1[10]);
}
	int printar10(int var1[10])
	{
		int a;
		
		printf("\nos valores do vetor sao:\n");
				printf("\n[");
				for (a = 0; a < 10; a++)
				{
				
					printf(" %i,", var1[a]);

				}
				printf("\b]\n");
				return(var1[10]);
	}
	int montar2x3(int var1[2][3])
{
	int entrada;
	int a, b;
	for (a = 0; a < 2; a++)
	{
		for (b = 0; b < 3; b++)
		{
			printf("\ndiga o valor [%i][%i]\n", a + 1, b + 1);
			scanf_s("%d", &entrada);
			var1[a][b] = entrada;
		}

	}
	return(var1[2][3]);
}
	int printar2x3(int var1[2][3])
	{
		printf("\na matriz printada eh:\n");
		int a, b;
		for (a = 0; a <2; a++)
		{
			printf("\n[");
			for (b = 0; b <3; b++)
			{
				printf(" %i ", var1[a][b]);
				printf("\t");
			}
			printf("]");
		}
		printf("\n\n");
		return(var1[2][3]);
	}
	int montar4x4(int var1[4][4])
{
	int entrada;
	int a, b;
	for (a = 0; a < 4; a++)
	{
		for (b = 0; b < 4; b++)
		{
			printf("\ndiga o valor [%i][%i]\n", a + 1, b + 1);
			scanf_s("%d", &entrada);
			var1[a][b] = entrada;
		}

	}
	return(var1[4][4]);
}
	int printar4x4(int var1[4][4])
	{
		printf("\na matriz printada eh:\n");
		int a, b;
		for (a = 0; a <4; a++)
		{
			printf("\n[");
			for (b = 0; b <4; b++)
			{
				printf(" %i ", var1[a][b]);
				printf("\t");
			}
			printf("]");
		}
		printf("\n\n");
		return(var1[4][4]);
	}

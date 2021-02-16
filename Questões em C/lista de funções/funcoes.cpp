#include<math.h>

float soma(float var1, float var2)
{
return (var1 + var2);
}
float subtracao(float var1, float var2)
{
return(var1 - var2);
}
float divisao(float var1, float var2)
{
return(var1 / var2);
}
float multiplicacao(float var1, float var2)
{
return(var1*var2);
}
int fatorial(int var1)
{
	
	if (var1 < 0)
	{
		return(0);
	}
	if ((var1 == 1) || (var1 == 0))
	{
		return(1);
	}
		if (var1 > 1)
		{
			int n = var1-1, fatorial = var1;
			for (n; n > 1; n--)
			{
				fatorial = fatorial*n;
			}
		return(fatorial);
		}
	
}
int primo(int var1)
{
	int decre = var1,cont=0;
	while(var1>1)
	{
  		int primo = decre % var1;
		var1--;
		  if (primo == 0)
		  {
			cont++;

			
		  }
	}
	if (decre == 4)
	{
		return(0);
	}

		if (cont <= 2)
		{
			return(1);

		}
	
	
}
float cosseno(float var1)
{
	int n;
	float c= 0.0;
	for (n = 0; n < 5; n++)
	{
		c = c + pow(-1, n)*pow(var1, 2 * n) / fatorial(2 * n);

	}
	return c;
}
float medianotas(float var1, float var2)
{
	float media = (var1 + var2) / 2;
	if (media >= 5) return media;
	
	else return media;
}
float raizx1(float a, float b, float c)
{
	
	float delta = (b*b) - (4 * a * c);
	float x1 = ((-1*b) + sqrt(delta)) / (2 * a);
	
	
	return (x1);
}
float raizx2(float a, float b, float c)
{
	
	float delta = (b*b) - (4 * a * c);
	
	float x2 = ((-1*b)- sqrt(delta)) / (2 * a);
	
	return  (x2);
}
float triangulo(float l1, float l2, float l3)
{
	int va0 = 0,va1 = 1, va2 = 2, va3 = 3, va4 = 4,va5 = 5;
	if((l1 == 0)||(l2 == 0)||(l3 == 0))
	{
		return va0;
	}
	else
	{
		if ((l1 > 0) && (l2 > 0) && (l3 > 0))
		{
			if ((((l1 + l2) > l3)&&(l3 > fabs(l1-l2))) && (((l1 + l3) > l2)&&(l2 > fabs(l1 - l3))) && (((l2 + l3) > l1)&&(l1 > fabs(l2 - l3))))//condição de existência do triângulo
			{

				if ((l1 == l2) && (l2 == l3) && (l3 == l1))
				{
					return va1;
				}


				if (((l1 == l2) && (l1 != l3)) || ((l2 == l1) && (l2 != l3)) || ((l3 == l2) && (l3 != l1)))
				{
					return va2;
				}
				if ((l1 != l2) && (l2 != l3) && (l1 != l3))
				{

					return va3;
				}

			}
			return va4;
		}
		return va5;
	}
}
float tresnotas(float nota1, float nota2)
{
	float ponderada = ((nota1*2) + (nota2 *3))  / 5;
	if (ponderada >= 7)
	{
		return ponderada;
	}
	else
	{

		return ponderada;
	}
}
float af(float complemento)
{
	float x;
	x = 14 - complemento;
	return x;
}
float cidades(float var1, float var2, float var3, float var4)
{
	float n = 1;
	while(var1 < var3)
	{
		var1 =  var1 + (var1 * var2*0.01);
		var3 = var3 + (var3 * var4*0.01);
		n++;
	} 
		return n;
}
/* C Programming Language
 * Juan Carlos F Pereira
 * URI Problem - SBC
 * Number - 1245
 * Created: 2018-04-29 : 14h40
 * Finished 2018-04-29 : 15h30
 */
#include <stdio.h>

int main()
{
	int tamanhos_direito[65], tamanhos_esquerdo[65]; 
	int n;

	while(scanf("%d", &n) != EOF)
	{
		int tamanho;
		char lado[3];
		int i, count = 0;
		for(i = 0; i < 63; i++)
		{
			tamanhos_direito[i] = 0;
			tamanhos_esquerdo[i] = 0;
		}
		for(i = 0; i < n; i++)
		{
			scanf("%d%s", &tamanho, lado);
			if(lado[0] == 'D')
				tamanhos_direito[tamanho]++;
			else
				tamanhos_esquerdo[tamanho]++;

			if(tamanhos_esquerdo[tamanho] != 0 && tamanhos_direito[tamanho] != 0)
			{
				count++;
				tamanhos_direito[tamanho]--;
				tamanhos_esquerdo[tamanho]--;	
			}
		}
		/*for(i = 30; i<63; i++)
		{
			while(tamanhos_esquerdo[i] != 0 && tamanhos_direito[i] != 0)
			{
				count++;
				tamanhos_direito[i]--;
				tamanhos_esquerdo[i]--;
			}
		}*/
		printf("%d\n",count);
	}
	return 0;
}
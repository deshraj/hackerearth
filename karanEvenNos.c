#include <stdio.h>

int main()
{
	long long int i,temp=0;
	for(i=0;temp!=-1;i++)
	{
			scanf("%lld",&temp);
			if(temp%2==0)
				printf("%lld\n",temp);
		}
    return 0;
}

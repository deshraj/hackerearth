#include<stdio.h>
int main()
{
	int n,m;
	long long int l;
	float p,d;
	scanf("%d",&n);
	while(n--)
	{
		scanf("%d",&m);
		if(m==2)
			m=28;
		else if(m==8 || m==4 || m==6 || m==9 || m==11)
			m=30;
		else 
			m=31;
		scanf("%f",&p);
		d = p*m;
		l = d*3*2500;
		m = d;
		printf("%d \n",m);
		printf("%lld\n",l);

	}
	return 0;
}
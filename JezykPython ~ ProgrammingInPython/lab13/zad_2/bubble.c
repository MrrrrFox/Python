void BubbleSortC(int * a, int b)
{
	for(int i = 0; i<b;++i)
	{
		for(int j = 0; j<b-1; ++j)
		{
			if(a[j]>a[j+1])
			{
				int tmp = a[j];
				a[j] = a[j+1];
				a[j+1] = tmp;
			}
		}
	}
}

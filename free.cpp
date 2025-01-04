#include <stdlib.h>
#include <stdio.h>
int main()
{
    int n, i, *p;
    printf("Enter the size of an array: ");
    scanf("%d", &n);
    p = (int *)calloc(n, sizeof(int));
    if (p == NULL)
        printf("\nMemory is not available");
    printf("\nEnter the elements in array a: ");
    for (i = 0; i < n; i++)
        scanf("%d", p + i);
    printf("\nThe elements in array a: ");
    for (i = 0; i < n; i++)
        printf("%d\t", *(p + i));
    printf("\n%d", p);
    free(p);
    p = NULL;
    printf("\n%d", p);
}
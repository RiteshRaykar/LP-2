#include<bits/stdc++.h>
#include <iostream>
using namespace std;
int main()
{
    int i,j,n,minindx, arr[30];
    cout<<"Enter the size of array: ";
    cin>>n;
    cout<<"\nEnter the elements\n";

    for(i=0;i<n;i++)
    {
        cin>>arr[i];
    }

    for(i=0;i<n-1;i++)
    {
       minindx=i;
       for(j=i+1;j<n;j++)
       {
           if(arr[j]<arr[minindx])
           {
               minindx=j;
           }
       }
       swap(arr[minindx],arr[i]);
    }

    cout<<"Array after selection sort: ";
    for(i=0;i<n;i++)
    {
        cout<<arr[i]<<" ";
    }
    
    return 0;
}
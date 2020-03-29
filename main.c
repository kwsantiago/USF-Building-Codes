#include <stdio.h>
#include <ctype.h>
#include <string.h>

void getBuildingName(char *str);

void getBuildingName(char *str){
    if(strncmp(str, "RBE", 3) == 0)
	    printf("Beta\n");
	else if(strncmp(str, "RBC", 3) == 0)
	    printf("Castor\n");
	else if(strncmp(str, "RKO", 3) == 0)
	    printf("Kosove\n");
	else if(strncmp(str, "RJH", 3) == 0)
	    printf("Juniper\n");
	else if(strncmp(str, "RPH", 3) == 0)
	    printf("Poplar\n");
	else if(strncmp(str, "MAA", 3) == 0)
	    printf("Magnolia A\n");
	else if(strncmp(str, "MAB", 3) == 0)
	    printf("Magnolia B\n");
	else if(strncmp(str, "MAC", 3) == 0)
	    printf("Magnolia C\n");
	else if(strncmp(str, "MAD", 3) == 0)
	    printf("Magnolia D\n");
	else if(strncmp(str, "MAE", 3) == 0)
	    printf("Magnolia E\n");
	else if(strncmp(str, "MAF", 3) == 0)
	    printf("Magnolia F\n");
	else if(strncmp(str, "MAG", 3) == 0)
	    printf("Magnolia G\n");
	else if(strncmp(str, "HAA", 3) == 0)
	    printf("Holly A\n");
	else if(strncmp(str, "HAB", 3) == 0)
	    printf("Holly B\n");
	else if(strncmp(str, "HAC", 3) == 0)
	    printf("Holly C\n");
	else if(strncmp(str, "HAD", 3) == 0)
	    printf("Holly D\n");
	else if(strncmp(str, "HAE", 3) == 0)
	    printf("Holly E\n");
	else if(strncmp(str, "HAF", 3) == 0)
	    printf("Holly F\n");
	else if(strncmp(str, "HAG", 3) == 0)
	    printf("Holly G\n");
	else if(strncmp(str, "RCA", 3) == 0)
	    printf("Cypress A (Suites)\n");
	else if(strncmp(str, "RCB", 3) == 0)
	    printf("Cypress B (Suites)\n");
	else if(strncmp(str, "RCC", 3) == 0)
	    printf("Cypress C (Apartments)\n");
	else if(strncmp(str, "RCD", 3) == 0)
	    printf("Cypress D (Apartments)\n");
	else if(strncmp(str, "MPA", 3) == 0)
	    printf("Maple A\n");
	else if(strncmp(str, "MPB", 3) == 0)
	    printf("Maple B\n");
	else if(strncmp(str, "RBN", 3) == 0)
	    printf("Beacon\n");
	else if(strncmp(str, "RSU", 3) == 0)
	    printf("Summit\n");
	else if(strncmp(str, "RPN", 3) == 0)
	    printf("Pinnacle\n");
	else if(strncmp(str, "REN", 3) == 0)
	    printf("Endeavor\n");
	else if(strncmp(str, "RHN", 3) == 0)
	    printf("Horizon\n");
	else if(strncmp(str, "GVA", 3) == 0)
	    printf("Alpha Delta Pi\n");
	else if(strncmp(str, "GVB", 3) == 0)
	    printf("Gamma Phi Beta\n");
	else if(strncmp(str, "GVC", 3) == 0)
	    printf("Sigma Delta Tau\n");
	else if(strncmp(str, "GVD", 3) == 0)
	    printf("Zeta Tau Alpha\n");
	else if(strncmp(str, "GVE", 3) == 0)
	    printf("Delta Chi\n");
	else if(strncmp(str, "GVF", 3) == 0)
	    printf("Sigma Chi\n");
	else if(strncmp(str, "GVG", 3) == 0)
	    printf("Delta Gamma\n");
	else if(strncmp(str, "GVH", 3) == 0)
	    printf("Delta Delta Delta\n");
	else if(strncmp(str, "GVI", 3) == 0)
	    printf("Sigma Nu\n");
	else if(strncmp(str, "GVJ", 3) == 0)
	    printf("Zeta Beta Tau\n");
	else if(strncmp(str, "GVK", 3) == 0)
	    printf("Chi Omega\n");
	else if(strncmp(str, "GVL", 3) == 0)
	    printf("Sigma Phi Epsilon\n");
	else if(strncmp(str, "GVM", 3) == 0)
	    printf("Kappa Delta\n");
	else if(strncmp(str, "GVN", 3) == 0)
	    printf("Alpha Omicron Pi\n");
	else
	    printf("Invalid building code.\n");
}

int main(){
    int c, i = 0;
    char str[4];
    while(1){
        printf("Enter the building code: ");
        while((c = getchar()) != EOF && c != '\n'){
        	str[i++] = toupper(c);
        }
    	getBuildingName(str);
        printf("\n");
    	i = 0;
    }
	
	return 0; 
}

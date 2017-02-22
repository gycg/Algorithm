#include <stdio.h>
#include <string.h>
#include <openssl/evp.h>

static const char alphabet[] = "abcdefghijklmnopqrstuvwxyz";
static const int alphabetSize = sizeof(alphabet) - 1;
char* digest(char* mess, char* argv1);
void bruteImpl(char* str, int index, int maxDepth, char* argv1, char* argv2);
void bruteSequential(int maxLen, char* argv1, char* argv2);

unsigned char md_value[EVP_MAX_MD_SIZE];

void bruteImpl(char* str, int index, int maxDepth, char* argv1, char* argv2)
{
    for (int i = 0; i < alphabetSize; ++i)
    {
        str[index] = alphabet[i];
        if (index == maxDepth - 1) //printf("%s\n", str);
	    {
		    unsigned char *md_v;
		    md_v = digest(str, argv1);
		
            char outword[7];
            for(int j = 0; j<3; j++){
                sprintf(outword+j*2, "%02x", md_v[j]);
            }

            int X = 1;
		    for(int k = 0; k < 6; ++k)
		    {
    		    if(outword[k] != argv2[k])
			    {	
                    X = 0;
	                //printf("%02x\n", outword[k]);
                    break;	
                }
		    }
		    if(X == 1)
			    printf("%s\n", str);
	    }
        else bruteImpl(str, index + 1, maxDepth, argv1, argv2);
    }
}

void bruteSequential(int maxLen, char* argv1, char* argv2)
{
    char* buf = malloc(maxLen + 1);

    for (int i = 1; i <= maxLen; ++i)
    {
        memset(buf, 0, maxLen + 1);
        bruteImpl(buf, 0, i, argv1, argv2);
    }

    free(buf);
}



char* digest(char* mess, char* argv1)
{
	EVP_MD_CTX *mdctx;
	const EVP_MD *md;
	int md_len, i;
	
	OpenSSL_add_all_digests();

	md = EVP_get_digestbyname(argv1);

    	if(!md) {
        	printf("Unknown message digest %s\n", argv1);
	        exit(1);
	}	

	mdctx = EVP_MD_CTX_create();
	EVP_DigestInit_ex(mdctx, md, NULL);



	EVP_DigestUpdate(mdctx, mess, strlen(mess));
   	EVP_DigestFinal_ex(mdctx, md_value, &md_len);
   	EVP_MD_CTX_destroy(mdctx);
	EVP_cleanup();
	return md_value;	
}

int main(int argc, char *argv[])
{
	if(!argv[1]) {
        	printf("Usage: mdtest digestname hashvalue\n");
	        exit(1);
    	}
	char* argv1 = argv[1];
	char* argv2 = argv[2];
		
	bruteSequential(2, argv1, argv2);

	exit(0);
}

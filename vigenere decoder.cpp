#include <stdio.h>
#include <vector>
#include <iostream>
#include <fstream>
#include <stdio.h> 
#include <math.h>  

using namespace std;

int mod(int a, int b){
    int r = a % b;
    return r < 0 ? r + b : r;
}


int main(int argc, char **argv){

	vector<char> crypted;
	int ab[26] = { 0 };
	vector<char> key;

	FILE *file;
	file = fopen(argv[1], "r");
	char c = fgetc(file);

	while (!feof(file)) {
		crypted.push_back(c);
		ab[c-65]++; // because all are capital
		c = fgetc(file);
	}
	double Itext = 0;
	int n = crypted.size();
	for(int i=0; i<26; i++){
		double fi = 1.0 * ab[i];
		Itext+= fi*(fi-1)/(n*(n-1));
	}
	cout << "Itext = " << Itext << endl;

	double r = (0.065-0.038) / (Itext-0.038);

	cout << "r = " << r << endl;

	int r1;
	Itext = 0.0;

	for(int r2 = 1; r2 <= 20 ; r2++){
		int ab[26] = { 0 };
		int n = 0;
		for(int j = 0; j<crypted.size(); j=j+r2){
			ab[crypted[j]-65]++;
			n++;
		}

		double IC = 0.0;
		for(int i=0; i<26; i++){
			double fi = 1.0 * ab[i];
			IC+= fi*(fi-1)/(n*(n-1));
		}
		if (IC > Itext) {
			r1 = r2;
			Itext = IC;
		}
	}

	cout << "the true r = " << r1 << endl; 

	int fs[r1][26] = { 0 };
	int C[r1] = { 0 }, olis[r1] = { 0 };
	double olis2[r1] = { 0 };

	for(int j = 0; j<r1; j++){
		for(int i = j; i<crypted.size(); i=i+r1){
			fs[j][crypted[i]-65]++;
			C[j]++;
		}
	}

	for(int k = 1; k<r1; k++){
		cout << "1h me " << k+1 << "h sthlh" << endl;
		for(int j=0; j<26; j++){

			double sum = 0.0;

			for(int i=0; i<26; i++){
				sum = sum + (1.0 * fs[0][mod(i-j,26)] * fs[k][i]) / (1.0 * C[0]*C[k]);
			}
			cout << "Gia olisthisi " << j << " exoume mutual coincidence " << sum << endl;
			if (sum > olis2[k]) {
				olis[k] = j;
				olis2[k] = sum;
			}
		}
		cout << endl;
	}
	//char decrypted[crypted.size()];
	olis[2]=24;
	olis[3]=13;
	for(int i=0;i<r1;i++) cout << "olisth tou " << i << " einai : " << olis[i] << endl;

	cout << endl;

	for(int k = 0; k < 26 ; k++){
		cout << "For 1st character " << (char) (k+65) << endl;
		for(int i=0; i<crypted.size();i++){
			cout << (char) (mod((crypted[i] - 65 - olis[i%r1] - k), 26) + 65);	
		}
		cout << endl << endl;
	}

	cout << "The key was ";
	for(int i=0;i<r1;i++){
		cout << (char) ((olis[i]+2)%26 + 65);
	}
	cout << endl;

}
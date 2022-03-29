#include <stdio.h>

int main() {
	int u, v = 0;
	int count = 0, flag = 0, k = 0;
	int check[500][500] = { 0, };
	int check_v[500] = { 0, };
	int isCheck[500] = { 0, };
	int isCount = 0;

	while (1) {
		scanf("%d %d", &u, &v);
		if (u == -1 && v == -1) break;
		else if (u == 0 && v == 0) {
			k++;
			if (flag == 0 && (isCount - count == 1 || isCount == 0)) printf("Case %d is a tree.\n", k);
			else printf("Case %d is not a tree.\n", k);

			flag = 0;
			count = 0;
			isCount = 0;
			for (int i = 0; i < 500; i++) {
				isCheck[i] = 0;
				check_v[i] = 0;
			}
			for (int i = 0; i < 500; i++) {
				for (int j = 0; j < 500; j++) check[i][j] = 0;
			}
		}
		else {
			if (isCheck[u] == 0) {
				isCheck[u] = 1;
				isCount++;
			}
			if (isCheck[v] == 0) {
				isCheck[v] = 1;
				isCount++;
			}
			if (check[u][v] == 0 && check[v][u] == 0) {
				check[u][v] = 1;
				check[v][u] = 1;
			}
			else flag = 1;
			if (check_v[v] == 0) {
				check_v[v] = 1;
				count++;
			}
			else flag = 1;
		}
	}
}
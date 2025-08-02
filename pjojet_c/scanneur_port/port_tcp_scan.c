#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>

int main() {
    char target_ip[100];
    int start_port, end_port;

    printf("Scanneur de port \n");
    printf("Entrez l'adresse IP cible : ");
    scanf("%s", target_ip);
    printf("Entrez le port de début : ");
    scanf("%d", &start_port);
    printf("Entrez le port de fin : ");
    scanf("%d", &end_port);

    printf("Scan des ports de %d à %d sur %s...\n", start_port, end_port, target_ip);

    for (int port = start_port; port <= end_port; port++) {
        int sockfd = socket(AF_INET, SOCK_STREAM, 0);
        if (sockfd < 0) {
            perror("Erreur de création de socket");
            exit(EXIT_FAILURE);
        }

        struct sockaddr_in target;
        memset(&target, 0, sizeof(target));
        target.sin_family = AF_INET;
        target.sin_port = htons(port);
        inet_pton(AF_INET, target_ip, &target.sin_addr);

        if (connect(sockfd, (struct sockaddr *)&target, sizeof(target)) < 0) {
            close(sockfd);
            continue; 
        }

        printf("Port %d ouvert\n", port);
        close(sockfd);
    }

    return 0;
}
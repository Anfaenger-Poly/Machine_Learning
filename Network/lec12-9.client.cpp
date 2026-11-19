#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

#define TIME_SERVER "192.168.108.119"
#define TIME_PORT   5010

int main() {
        int sock, buf_len;
        struct sockaddr_in server;
        char buf[256];

        if ((sock = socket(AF_INET, SOCK_DGRAM, 0)) == -1)
                exit(1);

        server.sin_family = AF_INET;
        server.sin_addr.s_addr = inet_addr(TIME_SERVER);
        server.sin_port = htons(TIME_PORT);

        strcpy(buf, "time");
        buf_len = sendto(sock, buf, strlen(buf) + 1, 0,
                        (struct sockaddr *)&server, sizeof(server));
        if (buf_len == -1)
                exit(1);

        buf_len = recvfrom(sock, buf, 256, 0, (struct sockaddr *)0, (socklen_t *)0);
        if (buf_len == -1)
                exit(1);
        printf("Time information from server is %s", buf);
        close(sock);
}

#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define TIME_SERVER "127.0.0.1"
#define TIME_PORT 5010

int main()
{
  int sock;
  struct sockaddr_in server;
  char buf[256];
  int buf_len;

  server.sin_family = AF_INET;
  server.sin_addr.s_addr = inet_addr(TIME_SERVER);
  server.sin_port = htons(TIME_PORT);

  if ((sock = socket(AF_INET, SOCK_STREAM, 0)) == -1)
      exit(1);

  if (connect(sock, (struct sockaddr *)&server, sizeof(server)) < 0)
      exit(1);

  buf_len = recv(sock, buf, 256, 0);
  if (buf_len < 0)
      exit(1);
  printf("Time information from server is %s", buf);
  close(sock);
}
